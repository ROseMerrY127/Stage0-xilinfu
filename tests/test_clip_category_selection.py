"""Offline regression checks with tiny generated images and no CLIP weights."""

import json
import pickle
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import torch
from PIL import Image
from transformers import CLIPImageProcessor

from clip_dataset import OCLClipDataset, load_dataset
from clip_inference import run_inference


class StubTokenizer:
    model_max_length = 77

    def __call__(self, texts, **kwargs):
        tokens = torch.arange(len(texts)).unsqueeze(1).repeat(1, 2)
        return {"input_ids": tokens, "attention_mask": torch.ones_like(tokens)}


class StubImageProcessor:
    def __call__(self, images, **kwargs):
        return {"pixel_values": torch.ones(1, 3, 4, 4)}


class StubModel:
    """Always predict the first category to make the accuracy denominator observable."""

    def eval(self):
        return self

    def get_text_features(self, input_ids, **kwargs):
        return torch.nn.functional.one_hot(input_ids[:, 0], num_classes=10).float()

    def get_image_features(self, pixel_values):
        features = torch.zeros(len(pixel_values), 10)
        features[:, 0] = 1
        return features


class CategorySelectionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        resources = self.root / "resources"
        resources.mkdir()
        self.head = [f"head_{index:02d}" for index in range(10)]
        vocabularies = {
            "object": self.head + ["test_only"],
            "attribute": ["round"],
            "affordance": [{"word": ["carry"], "define": "have with oneself"}],
        }
        for name, labels in vocabularies.items():
            (resources / f"OCL_class_{name}.json").write_text(json.dumps(labels))

        def record(split, label, count):
            return {
                "name": f"{split}/{label}.jpg",
                "objects": [
                    {"obj": label, "attr": [0], "aff": [0]} for _ in range(count)
                ],
            }

        splits = {
            "train": [record("train", label, 10) for label in self.head],
            "val": [record("val", self.head[0], 3)],
            "test": [record("test", label, 1) for label in self.head]
            + [record("test", "test_only", 9)],
        }
        for split, records in splits.items():
            with (resources / f"OCL_annot_{split}.pkl").open("wb") as handle:
                pickle.dump(records, handle)
            for record in records:
                path = self.root / record["name"]
                path.parent.mkdir(parents=True, exist_ok=True)
                Image.new("RGB", (8, 8), "white").save(path)
        self.processor = SimpleNamespace(
            image_processor=StubImageProcessor(), tokenizer=StubTokenizer()
        )

    def test_all_annotations_supply_counts_and_evaluation_objects(self):
        dataset, loader = load_dataset(
            self.root, self.processor, num_workers=0, pin_memory=False
        )
        self.assertEqual(dataset.category_classes, self.head)
        self.assertEqual(dataset.selection_category_counts[self.head[0]], 14)
        self.assertEqual(dataset.selection_category_counts[self.head[-1]], 11)
        self.assertEqual(len(dataset), 113)
        self.assertEqual(dataset.num_images, 21)
        self.assertEqual(dataset.evaluation_category_counts, dataset.selection_category_counts)
        self.assertEqual(loader.batch_size, 4)
        self.assertFalse(loader.drop_last)

    def test_invalid_box_remains_in_ranking_and_is_reported_before_evaluation(self):
        path = self.root / "resources" / "OCL_annot_train.pkl"
        with path.open("rb") as handle:
            records = pickle.load(handle)
        records.append(
            {
                "name": "train/invalid.jpg",
                "objects": [
                    {"obj": self.head[0], "attr": [0], "aff": [0], "box": [0, 2, 4, 2]}
                ],
            }
        )
        with path.open("wb") as handle:
            pickle.dump(records, handle)
        dataset = OCLClipDataset(self.root, self.processor)
        self.assertEqual(dataset.selection_category_counts[self.head[0]], 15)
        self.assertEqual(dataset.evaluation_category_counts[self.head[0]], 14)
        self.assertEqual(dataset.num_selected_objects, 114)
        self.assertEqual(len(dataset), 113)
        self.assertEqual(len(dataset.excluded_objects), 1)
        self.assertEqual(dataset.excluded_objects[0]["image_name"], "train/invalid.jpg")

    def test_missing_image_skips_its_objects_and_metrics_use_remaining_objects(self):
        (self.root / "train" / f"{self.head[0]}.jpg").unlink()
        dataset, loader = load_dataset(
            self.root, self.processor, num_workers=0, pin_memory=False
        )
        self.assertEqual(dataset.category_classes, self.head)
        self.assertEqual(dataset.selection_category_counts[self.head[0]], 14)
        self.assertEqual(dataset.evaluation_category_counts[self.head[0]], 4)
        self.assertEqual(len(dataset), 103)
        self.assertEqual(dataset.num_images, 20)
        self.assertEqual(dataset.exclusion_counts, {"missing_image": 10})
        self.assertEqual(
            {obj["object_index"] for obj in dataset.excluded_objects}, set(range(10))
        )
        self.assertEqual([len(batch["category_id"]) for batch in loader], [4] * 25 + [3])

        results = run_inference(StubModel(), dataset, loader, torch.device("cpu"), (1,))
        self.assertEqual(results["num_objects"], 103)
        self.assertEqual(results["num_selected_objects"], 113)
        self.assertEqual(results["num_excluded_objects"], 10)
        self.assertEqual(results["num_selected_images"], 21)
        self.assertEqual(results["num_images"], 20)
        self.assertEqual(results["exclusion_counts"], {"missing_image": 10})
        self.assertAlmostEqual(results["category"]["top_1_accuracy"], 4 / 103)
        self.assertEqual(results["attribute"]["mAP"], 1.0)
        self.assertEqual(results["affordance"]["mAP"], 1.0)

    def test_category_with_no_remaining_images_stays_in_candidate_labels(self):
        for split in ("train", "val", "test"):
            (self.root / split / f"{self.head[0]}.jpg").unlink()
        dataset = OCLClipDataset(self.root, self.processor)
        self.assertEqual(dataset.category_classes, self.head)
        self.assertEqual(dataset.selection_category_counts[self.head[0]], 14)
        self.assertEqual(dataset.evaluation_category_counts[self.head[0]], 0)
        self.assertEqual(len(dataset), 99)

    def test_unreadable_image_and_empty_crop_preserve_other_objects(self):
        (self.root / "train" / f"{self.head[0]}.jpg").write_bytes(b"not an image")
        path = self.root / "resources" / "OCL_annot_train.pkl"
        with path.open("rb") as handle:
            records = pickle.load(handle)
        records[1]["objects"][0]["box"] = [20, 20, 24, 24]
        records[1]["objects"][1]["box"] = [-2, -2, 4, 4]
        with path.open("wb") as handle:
            pickle.dump(records, handle)

        dataset, loader = load_dataset(
            self.root, self.processor, num_workers=0, pin_memory=False
        )
        self.assertEqual(dataset.exclusion_counts, {"unreadable_image": 10, "empty_crop": 1})
        self.assertEqual(dataset.evaluation_category_counts[self.head[1]], 10)
        self.assertEqual(len(dataset), 102)
        self.assertEqual(sum(len(batch["category_id"]) for batch in loader), 102)

    def test_no_available_images_reports_data_root_error(self):
        for path in self.root.rglob("*.jpg"):
            path.unlink()
        with self.assertRaisesRegex(ValueError, "No usable objects.*"):
            OCLClipDataset(self.root, self.processor)

    def test_missing_annotations_still_raise(self):
        (self.root / "resources" / "OCL_annot_test.pkl").unlink()
        with self.assertRaisesRegex(FileNotFoundError, "OCL_annot_test.pkl"):
            OCLClipDataset(self.root, self.processor)

    def test_invalid_labels_are_not_silently_skipped(self):
        path = self.root / "resources" / "OCL_annot_train.pkl"
        with path.open("rb") as handle:
            records = pickle.load(handle)
        records[0]["objects"][0]["attr"] = [99]
        with path.open("wb") as handle:
            pickle.dump(records, handle)
        dataset = OCLClipDataset(self.root, self.processor)
        with self.assertRaisesRegex(ValueError, "Label IDs outside"):
            dataset[0]

    def test_small_rgb_crops_preserve_channels_and_pixel_values(self):
        path = self.root / "resources" / "OCL_annot_train.pkl"
        with path.open("rb") as handle:
            records = pickle.load(handle)
        records[0]["name"] = "train/rgb.png"
        Image.new("RGB", (8, 8), (255, 0, 0)).save(self.root / "train/rgb.png")
        sizes = ((5, 1), (5, 3), (5, 5), (1, 5), (3, 5), (3, 3), (1, 1))
        for index, (width, height) in enumerate(sizes):
            records[0]["objects"][index]["box"] = [1, 1, 1 + width, 1 + height]
        with path.open("wb") as handle:
            pickle.dump(records, handle)

        image_processor = CLIPImageProcessor()
        self.processor.image_processor = image_processor
        dataset = OCLClipDataset(self.root, self.processor)
        expected = (
            (torch.tensor([1., 0., 0.]) - torch.tensor(image_processor.image_mean))
            / torch.tensor(image_processor.image_std)
        )[:, None, None].expand(3, 224, 224)

        for index, (width, height) in enumerate(sizes):
            with self.subTest(width=width, height=height):
                with self.assertNoLogs("transformers.image_utils", level="WARNING"):
                    pixels = dataset[index]["pixel_values"]
                torch.testing.assert_close(pixels, expected)


if __name__ == "__main__":
    unittest.main()
