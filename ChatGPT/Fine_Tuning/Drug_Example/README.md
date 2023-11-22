# AI Enabled Drug Classification System

## Introduction

This project harnesses the capabilities of OpenAI's GPT-3.5 for Drug Classification through Machine Learning. The goal is to enhance the precision of drug classification by using a curated dataset of 2000 drug examples. This initiative is aimed at training a computer system to accurately identify the illnesses that specific medicines are intended to treat.

## Design

### Step 1: Data Preparation

Convert the XLSX data file into JSONL format, suitable for model fine-tuning, using Pandas and OpenAI tools. The data should be structured with prompts and completions for drug names and corresponding illnesses, ensuring each completion starts with a whitespace.

### Step 2: Preparing Data for Training

Use the OpenAI `fine_tunes.prepare_data` command to analyze and split the data into training and validation sets.

### Step 3: Model Training

Train the model with the `fine_tunes.create` command, specifying parameters like training and validation data files, model type (ada), and classification metrics.

### Step 4: Monitoring Progress

In case of disconnection during fine-tuning, utilize the provided command to check the job's progress.

### Step 5: Fine-Tuning Completion

Once fine-tuning is complete, an output confirming the job's completion, cost, and additional details will be generated.

## Implementation:

### Step 1: Setting Up the Environment

Create a virtual environment and activate it:

```shell
python3 -m venv venv
. venv/bin/activate
workon chatgpt
```
### Step 2 : Install the necessary packages:

```bash
pip install pandas openpyxl openai==0.28
```

### Step3 : Prepare the data for fine-tuning:

```bash
openai tools fine_tunes.prepare_data -f drug_malady_data.jsonl
```

### Step 4: Exporting openAI Key

```bash
export OPENAI_API_KEY="your_api_key"
```

### Step 5: Commence model fine-tuning:

```bash
 openai api fine_tunes.create \
  -t "drug_malady_data_prepared_train.jsonl" \
  -v "drug_malady_data_prepared_valid.jsonl" \
  --compute_classification_metrics \
  --classification_n_classes 7 \
  -m ada \
  --suffix "drug_malady_data"
```

### Step 6: Monitor the fine-tuning progress:

```bash
openai api fine_tunes.follow -i <JOB ID>
```

### Step 7: Run the test script:

```bash
python3 test.py
```

