"""Evaluate frozen Hugging Face CLIP on the ten largest OCL categories."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.metrics import average_precision_score
from torch.utils.data import DataLoader
from tqdm.auto import tqdm
from transformers import CLIPModel, CLIPProcessor

from clip_dataset import BATCH_SIZE, NUM_CATEGORIES, OCLClipDataset, load_dataset


def load_model(
    model_name: str,
    device: torch.device,
    local_files_only: bool = False,
) -> tuple[CLIPModel, CLIPProcessor]:
    processor = CLIPProcessor.from_pretrained(
        model_name, local_files_only=local_files_only, use_fast=False
    )
    model = CLIPModel.from_pretrained(model_name, local_files_only=local_files_only)
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    model.to(device)
    model.eval()
    return model, processor


@torch.inference_mode()
def encode_candidate_labels(
    model: CLIPModel,
    text_inputs: dict[str, dict[str, torch.Tensor]],
    device: torch.device,
) -> dict[str, torch.Tensor]:
    embeddings = {}
    for task, tokens in text_inputs.items():
        chunks = []
        for start in range(0, tokens["input_ids"].shape[0], 64):
            inputs = {key: value[start : start + 64].to(device) for key, value in tokens.items()}
            features = model.get_text_features(**inputs)
            chunks.append(F.normalize(features.float(), dim=-1))
        embeddings[task] = torch.cat(chunks)
    return embeddings


def multilabel_metrics(
    targets: np.ndarray,
    scores: np.ndarray,
    labels: list,
) -> dict:
    if targets.ndim != 2 or targets.shape != scores.shape or targets.shape[1] != len(labels):
        raise ValueError(
            "Multi-label targets, scores and label vocabulary must have matching shapes."
        )
    if not np.isfinite(scores).all():
        raise ValueError("Non-finite CLIP similarity scores encountered.")
    per_label = []
    valid_aps = []
    for index, label in enumerate(labels):
        positives = int(targets[:, index].sum())
        # Match the OCL evaluator: labels with no positives do not contribute to mAP.
        ap = (
            float(average_precision_score(targets[:, index], scores[:, index]))
            if positives else None
        )
        if ap is not None:
            valid_aps.append(ap)
        per_label.append({"id": index, "label": label, "positives": positives, "AP": ap})
    return {
        "mAP": float(np.mean(valid_aps)) if valid_aps else None,
        "num_evaluated_labels": len(valid_aps),
        "num_labels": len(labels),
        "labels_without_positives": "excluded",
        "per_label": per_label,
    }


@torch.inference_mode()
def run_inference(
    model: CLIPModel,
    dataset: OCLClipDataset,
    loader: DataLoader,
    device: torch.device,
    top_k: tuple[int, ...] = (1, 5),
) -> dict:
    top_k = tuple(sorted(set(top_k)))
    if not top_k or any(k < 1 or k > len(dataset.category_classes) for k in top_k):
        raise ValueError(
            f"top_k must contain values between 1 and {len(dataset.category_classes)}."
        )
    model.eval()
    text_features = encode_candidate_labels(model, dataset.text_inputs, device)
    correct = {k: 0 for k in top_k}
    num_objects = 0
    attribute_scores, affordance_scores = [], []
    attribute_targets, affordance_targets = [], []

    for batch in tqdm(loader, desc="CLIP inference", unit="batch"):
        pixel_values = batch["pixel_values"].to(device, non_blocking=device.type == "cuda")
        features = model.get_image_features(pixel_values=pixel_values)
        image_features = F.normalize(features.float(), dim=-1)
        # Unit-length embeddings turn dot products into cosine similarities.
        category_scores = image_features @ text_features["category"].T
        ranking = category_scores.topk(max(top_k), dim=-1).indices
        targets = batch["category_id"].to(device)
        for k in top_k:
            correct[k] += int((ranking[:, :k] == targets[:, None]).any(dim=1).sum().item())
        num_objects += targets.numel()

        # Multi-label AP uses independent scores; softmax would couple unrelated labels.
        attribute_scores.append((image_features @ text_features["attribute"].T).cpu())
        affordance_scores.append((image_features @ text_features["affordance"].T).cpu())
        attribute_targets.append(batch["attributes"])
        affordance_targets.append(batch["affordances"])

    if num_objects == 0 or num_objects != len(dataset):
        raise RuntimeError(f"Expected {len(dataset)} objects, evaluated {num_objects}.")
    return {
        "evaluation_scope": "available_objects_from_top_ten_categories",
        "num_objects": num_objects,
        "num_selected_objects": dataset.num_selected_objects,
        "num_selected_objects_before_box_filter": dataset.num_selected_objects,
        "num_excluded_objects": len(dataset.excluded_objects),
        "exclusion_counts": dataset.exclusion_counts,
        "excluded_objects": dataset.excluded_objects,
        "num_selected_images": dataset.num_selected_images,
        "num_images": dataset.num_images,
        "metric_scale": "0..1",
        "category": {f"top_{k}_accuracy": correct[k] / num_objects for k in top_k},
        "attribute": multilabel_metrics(
            torch.cat(attribute_targets).numpy(),
            torch.cat(attribute_scores).numpy(),
            dataset.attribute_classes,
        ),
        "affordance": multilabel_metrics(
            torch.cat(affordance_targets).numpy(),
            torch.cat(affordance_scores).numpy(),
            dataset.affordance_classes,
        ),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, default=Path("./data"))
    parser.add_argument(
        "--model",
        default="openai/clip-vit-base-patch32",
        help="Hugging Face ID or local model directory",
    )
    parser.add_argument("--device", default="cuda", help="For example cuda, cuda:1, or cpu")
    parser.add_argument("--num-workers", type=int, default=4)
    parser.add_argument("--top-k", type=int, nargs="+", default=[1, 5])
    parser.add_argument(
        "--local-files-only",
        action="store_true",
        help="Load model and processor from local files/cache only",
    )
    parser.add_argument("--output", type=Path, default=Path("logs/clip_inference/metrics.json"))
    args = parser.parse_args()
    if args.num_workers < 0:
        parser.error("--num-workers must be non-negative")
    if any(k < 1 or k > NUM_CATEGORIES for k in args.top_k):
        parser.error(f"--top-k values must be between 1 and {NUM_CATEGORIES}")
    return args


def main() -> None:
    args = parse_args()
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    device = torch.device(args.device)
    if device.type == "cuda" and not torch.cuda.is_available():
        raise RuntimeError(
            f"CUDA is unavailable (PyTorch {torch.__version__}, CUDA build {torch.version.cuda}). "
            "Run bash setup_clip_gpu.sh on the GPU server and check its NVIDIA driver."
        )
    device_name = torch.cuda.get_device_name(device) if device.type == "cuda" else str(device)
    print(f"Device: {device} ({device_name}); PyTorch: {torch.__version__}; CUDA: {torch.version.cuda}")
    model, processor = load_model(args.model, device, args.local_files_only)
    dataset, loader = load_dataset(
        args.data_root,
        processor,
        num_workers=args.num_workers,
        pin_memory=device.type == "cuda",
    )
    print(
        f"Images: {dataset.num_images}; objects: {len(dataset)}; batch size: {BATCH_SIZE}"
    )
    if dataset.excluded_objects:
        print(
            f"Skipped {len(dataset.excluded_objects)} of {dataset.num_selected_objects} "
            f"selected objects: {dataset.exclusion_counts}. "
            "Details will be saved in the metrics JSON."
        )
    for category, count in dataset.selection_category_counts.items():
        print(
            f"  {category}: ranking objects={count}, "
            f"evaluation objects={dataset.evaluation_category_counts[category]}"
        )

    results = run_inference(model, dataset, loader, device, tuple(args.top_k))
    results.update(
        {
            "model": args.model,
            "device": str(device),
            "device_name": device_name,
            "torch_version": torch.__version__,
            "cuda_build": torch.version.cuda,
            "data_root": str(dataset.data_root),
            "count_unit": "object_instance",
            "batch_size": BATCH_SIZE,
            "selected_categories": [
                {
                    "id": index,
                    "name": name,
                    "selection_samples": dataset.selection_category_counts[name],
                    "evaluation_samples": dataset.evaluation_category_counts[name],
                }
                for index, name in enumerate(dataset.category_classes)
            ],
            "prompts": dataset.prompts,
        }
    )
    output = args.output.expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, allow_nan=False)
        handle.write("\n")

    for name, accuracy in results["category"].items():
        print(f"{name}: {accuracy:.2%}")
    for task in ("attribute", "affordance"):
        metrics = results[task]
        value = "N/A" if metrics["mAP"] is None else f"{metrics['mAP']:.2%}"
        print(
            f"{task} mAP: {value} "
            f"({metrics['num_evaluated_labels']}/{metrics['num_labels']} labels with positives)"
        )
    print(f"Metrics saved to {output}")


if __name__ == "__main__":
    main()
