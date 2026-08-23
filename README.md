# Viking History QA Dataset Generator


## Overview
A scalable production-grade Python LLM-powered data generation pipeline that can produce 10K–20K+ validated, deduplicated domain-specific QA pairs, transforming raw knowledge into training-ready datasets for specialized AI models.


## Project:

Viking History QA Dataset Generator

### Problem

Generating thousands of high-quality question-answer pairs manually is slow and difficult.

### Solution

A Python pipeline using a locally hosted LLM through Ollama to generate, validate, deduplicate, and save QA pairs into CSV format.

### Architecture
Prompt Builder
      ↓
Ollama / Qwen
      ↓
JSON Parser
      ↓
Validator
      ↓
Duplicate Detector
      ↓
CSV Manager
      ↓
Dataset

## Features
- **Automated Generation**: Iteratively creates QA pairs based on a defined topic.
- **Duplicate Detection**: Uses RapidFuzz for fuzzy similarity detection to ensure question uniqueness.
- **Resumability**: Built-in checkpointing system to pause and resume generation seamlessly.
- **Robust Error Handling**: Configurable retry mechanisms and robust logging for API reliability.
- **Progress Tracking**: Real-time progress visualization using `tqdm`.
- **Modular Architecture**: Well-separated components for prompt building, validation, and data management.


## Tech Stack
- **Python** (Core language)
- **Ollama** (Local LLM Server)
- **OpenAI SDK** (Client to connect to Ollama)
- **RapidFuzz** (String matching & similarity)
- **tqdm** (Progress tracking)

## Installation
1. Ensure you have [Ollama](https://ollama.ai/) installed and running locally with the required model:
   ```bash
   ```
2. Clone the repository and navigate to the project directory.
3. Install the required Python dependencies:
   ```bash
   pip install -r 13_requirements.txt
   ```

## Usage
Run the main script to start or resume the generation process:
```bash
python -m src.main
```
The generated dataset will be iteratively saved to `viking_dataset.csv`.

## API Endpoints
*N/A - This project operates as a local CLI tool connecting to a local Ollama endpoint.*

## Results
- Successfully generates a curated, duplicate-free `viking_dataset.csv` file.
- Detailed operation logs are stored in `generator.log`.

## Screenshots
![alt text](assets/architecture.png)  # progress bar
![alt text](assets/demo.png)  # dataset generated 2000 Q&A pairs on vikings history .

## Future Improvements
- Expand dataset domains beyond Viking History.
- Integrate additional model backends alongside Ollama.
- Add advanced QA validation algorithms.

## Author
Aniket Jadhav
