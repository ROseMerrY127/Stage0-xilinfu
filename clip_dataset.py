"""Object crops and candidate-label tokens for the OCL CLIP experiment."""

from __future__ import annotations

import json
import math
import pickle
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import torch
from PIL import Image
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms.functional import pil_to_tensor
from tqdm.auto import tqdm

if TYPE_CHECKING:
    from transformers import CLIPProcessor


NUM_CATEGORIES = 10
BATCH_SIZE = 4


@dataclass(frozen=True)
class ObjectInstance:
    image_name: str
    object_index: int
    category_id: int
    box: tuple[float, float, float, float] | None
    attribute_ids: tuple[int, ...]
    affordance_ids: tuple[int, ...]


class OCLClipDataset(Dataset):
    """One sample per annotated object in the ten most frequent categories."""

    def __init__(
        self,
        data_root: str | Path,
        processor: CLIPProcessor,
    ) -> None:
        self.data_root = Path(data_root).expanduser().resolve()
        self.image_processor = processor.image_processor
        resources = self.data_root / "resources"

        def load_classes(name: str) -> list:
            with (resources / f"OCL_class_{name}.json").open(encoding="utf-8") as handle:
                return json.load(handle)

        object_classes = load_classes("object")
        self.attribute_classes = load_classes("attribute")
        self.affordance_classes = load_classes("affordance")
        annotations = []
        # Merge all supplied annotations into one evaluation dataset.
        for filename in ("OCL_annot_train.pkl", "OCL_annot_val.pkl", "OCL_annot_test.pkl"):
            annotation_path = resources / filename
            if not annotation_path.is_file():
                raise FileNotFoundError(
                    f"Missing {annotation_path}. Extract data/resources/OCL_annot.tgz first."
                )
            with annotation_path.open("rb") as handle:
                annotations.extend(pickle.load(handle))

        counts = Counter(obj["obj"] for image in annotations for obj in image["objects"])
        unknown = set(counts) - set(object_classes)
        if unknown:
            raise ValueError(f"Categories missing from OCL_class_object.json: {sorted(unknown)}")
        if len(counts) < NUM_CATEGORIES:
            raise ValueError(f"Need {NUM_CATEGORIES} categories; found {len(counts)}.")
        # Alphabetical tie-breaking makes class IDs independent of annotation order.
        ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        self.selection_category_counts = dict(ranked[:NUM_CATEGORIES])
        self.category_classes = list(self.selection_category_counts)
        category_to_id = {name: index for index, name in enumerate(self.category_classes)}

        self.instances = [
            ObjectInstance(
                image_name=image["name"],
                object_index=object_index,
                category_id=category_to_id[obj["obj"]],
                box=tuple(obj["box"]) if "box" in obj else None,
                attribute_ids=tuple(obj["attr"]),
                affordance_ids=tuple(obj["aff"]),
            )
            for image in annotations
            for object_index, obj in enumerate(image["objects"])
            if obj["obj"] in category_to_id
        ]
        self.num_selected_objects = len(self.instances)
        self.num_selected_images = len({instance.image_name for instance in self.instances})
        self.excluded_objects = []
        valid_instances = []

        def exclude(instance: ObjectInstance, reason: str, detail: str) -> None:
            self.excluded_objects.append(
                {
                    "image_name": instance.image_name,
                    "object_index": instance.object_index,
                    "category": self.category_classes[instance.category_id],
                    "box": repr(instance.box),
                    "reason": reason,
                    "detail": detail,
                }
            )

        # Resolve each image once before batching so skipped objects do not shrink batches.
        image_info = {}
        for instance in tqdm(self.instances, desc="Preparing objects", unit="object"):
            box = instance.box
            if box is not None and (
                len(box) != 4
                or not all(math.isfinite(value) for value in box)
                or box[2] <= box[0]
                or box[3] <= box[1]
            ):
                exclude(
                    instance, "invalid_box",
                    "non-finite, malformed or non-positive-area box",
                )
                continue

            if instance.image_name not in image_info:
                try:
                    with Image.open(self.data_root / instance.image_name) as image:
                        image.load()
                        image.convert("RGB")
                        image_info[instance.image_name] = (image.size, None, None)
                except FileNotFoundError as error:
                    image_info[instance.image_name] = (None, "missing_image", str(error))
                except (OSError, ValueError, SyntaxError, Image.DecompressionBombError) as error:
                    image_info[instance.image_name] = (None, "unreadable_image", str(error))

            size, reason, detail = image_info[instance.image_name]
            if reason is not None:
                exclude(instance, reason, detail)
                continue
            try:
                self._crop_box(size, instance)
            except ValueError as error:
                exclude(instance, "empty_crop", str(error))
                continue
            valid_instances.append(instance)

        self.instances = valid_instances
        if not self.instances:
            raise ValueError(
                f"No usable objects from the selected categories in {self.data_root}. "
                "Check --data-root and the uploaded image directories."
            )
        self.exclusion_counts = dict(Counter(obj["reason"] for obj in self.excluded_objects))
        evaluation_counts = Counter(instance.category_id for instance in self.instances)
        self.evaluation_category_counts = {
            name: evaluation_counts[index] for index, name in enumerate(self.category_classes)
        }
        self.num_images = len({instance.image_name for instance in self.instances})

        self.prompts = {
            "category": list(self.category_classes),
            "attribute": list(self.attribute_classes),
            # Keep one entry per affordance ID, even when labels share the same word.
            "affordance": [label["word"][0] for label in self.affordance_classes],
        }
        self.text_inputs = {
            name: dict(
                processor.tokenizer(
                    prompts,
                    padding=True,
                    truncation=True,
                    max_length=processor.tokenizer.model_max_length,
                    return_tensors="pt",
                )
            )
            for name, prompts in self.prompts.items()
        }

    @staticmethod
    def _multi_hot(indices: tuple[int, ...], size: int) -> torch.Tensor:
        if any(index < 0 or index >= size for index in indices):
            raise ValueError(f"Label IDs outside [0, {size}): {indices}")
        target = torch.zeros(size, dtype=torch.float32)
        if indices:
            target[list(indices)] = 1.0
        return target

    @staticmethod
    def _crop_box(
        image_size: tuple[int, int], instance: ObjectInstance,
    ) -> tuple[int, int, int, int]:
        width, height = image_size
        box = instance.box if instance.box is not None else (0, 0, width, height)
        if len(box) != 4 or not all(math.isfinite(value) for value in box):
            raise ValueError(
                f"Invalid box in {instance.image_name}, object {instance.object_index}: {box}"
            )
        # OCL already stores xyxy coordinates, including for its COCO images.
        left, top, right, bottom = box
        left, top = max(0, left), max(0, top)
        right, bottom = min(width, right), min(height, bottom)
        if right <= left or bottom <= top:
            raise ValueError(
                f"Empty box in {instance.image_name}, object {instance.object_index}: {box}"
            )
        return math.floor(left), math.floor(top), math.ceil(right), math.ceil(bottom)

    @staticmethod
    def _crop_object(image: Image.Image, instance: ObjectInstance) -> Image.Image:
        return image.crop(OCLClipDataset._crop_box(image.size, instance)).convert("RGB")

    def __len__(self) -> int:
        return len(self.instances)

    def __getitem__(self, index: int) -> dict:
        instance = self.instances[index]
        image_path = self.data_root / instance.image_name
        with Image.open(image_path) as image:
            crop = self._crop_object(image, instance)
        # Use torchvision's explicit CHW conversion, keeping uint8 for CLIP rescaling.
        pixel_values = self.image_processor(
            images=pil_to_tensor(crop),
            input_data_format="channels_first",
            return_tensors="pt",
        )["pixel_values"][0]
        return {
            "pixel_values": pixel_values,
            "category_id": instance.category_id,
            "attributes": self._multi_hot(instance.attribute_ids, len(self.attribute_classes)),
            "affordances": self._multi_hot(instance.affordance_ids, len(self.affordance_classes)),
            "image_name": instance.image_name,
            "object_index": instance.object_index,
        }


def load_dataset(
    data_root: str | Path,
    processor: CLIPProcessor,
    num_workers: int = 4,
    pin_memory: bool = True,
) -> tuple[OCLClipDataset, DataLoader]:
    if num_workers < 0:
        raise ValueError("num_workers must be non-negative")
    dataset = OCLClipDataset(data_root, processor)
    loader = DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=False,
        drop_last=False,
        num_workers=num_workers,
        pin_memory=pin_memory,
        persistent_workers=num_workers > 0,
    )
    return dataset, loader
