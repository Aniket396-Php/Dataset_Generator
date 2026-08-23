# Viking History QA Dataset Generator

An LLM-powered, modular data-generation pipeline for automatically creating **validated, deduplicated, domain-specific question-answer datasets** using a locally hosted Qwen model through Ollama.

The pipeline is designed to scale from thousands to **10K–20K+ QA pairs**, making it suitable for building specialized training datasets for downstream AI/ML applications.

## 🚀 Overview

Manually creating thousands of high-quality QA pairs is time-consuming and difficult to scale.

This project automates the complete workflow:

**Topic → LLM Generation → JSON Parsing → Validation → Deduplication → CSV Dataset**

The current implementation uses **Viking History** as the demonstration domain, but the pipeline can be adapted to other specialized domains.

## 🏗️ Architecture

```text
                 ┌─────────────────┐
                 │  Topic / Prompt │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Prompt Builder │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │  Ollama + Qwen  │
                 │   Local LLM     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   JSON Parser   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │    Validator    │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │    Duplicate    │
                 │    Detector     │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │   CSV Manager   │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Training-Ready  │
                 │     Dataset     │
                 └─────────────────┘
```

## ✨ Key Features

### Automated QA Generation

Generates large batches of domain-specific question-answer pairs using a locally hosted LLM.

### JSON Validation

Parses and validates structured LLM output before adding records to the dataset.

### Fuzzy Duplicate Detection

Uses **RapidFuzz** similarity matching to identify questions that are identical or highly similar.

### Checkpoint-Based Resumability

The generation process maintains checkpoints so interrupted jobs can resume instead of starting from zero.

### Retry & Error Handling

Failed LLM requests and malformed responses can be retried automatically, improving reliability during long-running generation jobs.

### Progress Tracking

Uses `tqdm` to provide real-time generation progress.

### Modular Architecture

The pipeline separates generation, parsing, validation, deduplication, checkpointing, logging, and CSV management into independent modules.

### Local LLM Inference

Uses Ollama to run the model locally, avoiding dependency on a paid cloud inference API for the generation pipeline.

## 🧰 Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Core pipeline               |
| Ollama     | Local LLM inference         |
| Qwen       | QA generation model         |
| OpenAI SDK | Client interface for Ollama |
| RapidFuzz  | Fuzzy duplicate detection   |
| tqdm       | Progress tracking           |
| CSV        | Dataset storage             |
| pytest     | Validation/testing          |

## 📁 Project Structure

```text
Dataset_Generator/
│
├── assets/
│   └── screenshots
│
├── data/
│   └── viking_dataset.csv
│
├── src/
│   ├── checkpoint.py
│   ├── config.py
│   ├── constants.py
│   ├── csv_manager.py
│   ├── duplicate_detector.py
│   ├── generator.py
│   ├── json_parser.py
│   ├── logger.py
│   ├── main.py
│   ├── ollama_client.py
│   ├── prompt_builder.py
│   └── validator.py
│
├── tests/
│   └── test_validator.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aniket396-Php/Dataset_Generator.git
cd Dataset_Generator
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Install and start Ollama from the official website:

https://ollama.com/

Then download the required model. For example:

```bash
ollama pull qwen3:8b
```

Make sure Ollama is running before starting the generator.

## ▶️ Usage

Start the dataset generation pipeline:

```bash
python -m src.main
```

The pipeline will:

1. Generate QA pairs using Qwen.
2. Parse the LLM response.
3. Validate the generated records.
4. Detect duplicate questions.
5. Save valid records to CSV.
6. Update the checkpoint.
7. Retry failed generations when necessary.

The generated dataset is stored in:

```text
data/viking_dataset.csv
```

## 📊 Results

The pipeline has been used to generate **2,000+ Viking History QA pairs** while applying validation and duplicate detection.

The architecture is designed to scale toward **10K–20K+ domain-specific QA pairs** without requiring a fundamental redesign of the pipeline.

## 🔬 Why This Project Matters

The same architecture can be adapted from Viking History to specialized domains such as:

* Internal company knowledge
* Customer-support datasets
* Legal-domain QA
* Financial-domain QA
* Educational datasets
* Product documentation
* Industry-specific assistants

This makes the pipeline useful as a **synthetic data generation layer for specialized AI/ML systems**.

## 🔮 Future Improvements

* Support multiple LLM backends.
* Add stronger semantic duplicate detection using embeddings.
* Add automated factuality evaluation.
* Add configurable dataset schemas.
* Add parallel batch generation.
* Add experiment tracking and generation metrics.
* Support JSONL and Parquet output.
* Add configurable domain/topic templates.
* Add automated quality scoring.

## 👨‍💻 Author

**Aniket Jadhav**

AI/ML Engineering

## 📄 License

This project is licensed under the **MIT License**.
