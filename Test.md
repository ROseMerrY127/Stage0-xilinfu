# OCL

Implement an OCL-based object category classification inference experiment.

Set up your own Python environment by downloading and installing **Miniforge / uv / Python**, and then begin the experiment.

## References

1. OCL paper: **Beyond Object Recognition: A New Benchmark towards Object Concept Learning**

2. **OCL dataset preparation**

   - The official data preparation scripts are provided in the OCL GitHub repository: [https://github.com/silicx/ObjectConceptLearning/tree/main/data](https://github.com/silicx/ObjectConceptLearning/tree/main/data)
   - Please read and understand the provided scripts and dataset structure before implementing the DataLoader.
   - In particular, the repository provides `prepare_data.sh`, `download_web_images.py`, and the `resources` directory for dataset preparation.
   - After downloading the dataset, inspect the image data and annotation files carefully and understand how **category**, **attribute**, and **affordance** annotations are represented.

3. Download and prepare the required test data using the scripts provided in the official OCL GitHub repository.

4. CLIP paper/repository: **Contrastive Language-Image Pre-Training**

   [https://github.com/openai/CLIP](https://github.com/openai/CLIP)

## Step 1: Prepare the DataLoader

1. Implement a custom dataset class by inheriting from PyTorch's native `Dataset`:

   - Load the dataset and corresponding annotations;
   - Filter the data by sorting category labels according to the number of samples, and keep only the **10 categories with the largest number of samples**;
   - Perform image preprocessing and text tokenization.

2. Create a test data loader using PyTorch's native `DataLoader`:

   - Set `batch_size = 4`.

## Step 2: Prepare the CLIP Model

1. Load a pretrained CLIP model using the available API.

## Step 3: Inference and Evaluation

1. Instantiate the dataset and model, and move the model to GPU, including:

   - `load_dataset`
   - `load_model`
   - `model.to(device)`

2. Set the model to inference mode and freeze all model parameters:

   - Iterate over all model parameters and set gradient computation to `False`.

3. Iterate over the test set and perform inference:

   - Each image may contain multiple objects.
   - Compute the cosine similarity between each object and the candidate **category** labels.
   - Use the cosine similarity scores for ranking.
   - Compute the model's **Top-k accuracy**.
   - Perform forward inference batch by batch and report the average accuracy over the entire test set.

4. Evaluate the prediction performance for **attribute** and **affordance** labels using the **mAP (mean Average Precision)** metric.
