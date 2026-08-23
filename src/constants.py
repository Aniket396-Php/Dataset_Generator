"""Constants and templates for the Viking QA Dataset Generator."""

# File Configuration
CSV_COLUMNS = ["question", "answer"]
FILE_ENCODING = "utf-8"

# JSON Keys
KEY_QUESTION = "question"
KEY_ANSWER = "answer"

# Logging Messages
MSG_INIT = "Initializing Viking QA Dataset Generator..."
MSG_START_BATCH = "Starting generation for batch {batch_num}..."
MSG_BATCH_SUCCESS = "Successfully generated {count} valid pairs in batch {batch_num}."
MSG_BATCH_ERROR = "Error generating batch {batch_num}: {error}"
MSG_BATCH_RETRY = "Retrying batch {batch_num} (Attempt {attempt}/{max_retries})..."
MSG_BATCH_FAILED = "Batch {batch_num} failed completely after {retries} retries."
MSG_DUPLICATE_SKIPPED = "Skipped duplicate question: {question}"
MSG_VALIDATION_FAILED = "Validation failed: {reason}"
MSG_SAVED_CHECKPOINT = "Saved checkpoint: {count} questions generated."
MSG_COMPLETE = "Generation complete. Total questions: {total}"

# System Prompt
SYSTEM_PROMPT = (
    "You are a world-class historian and dataset generation expert specializing "
    "in the Viking Age. You write professional, historically accurate educational content."
)

# User Prompt Template
USER_PROMPT_TEMPLATE = """Generate {batch_size} NEW, UNIQUE, and HISTORICALLY ACCURATE Viking history question-answer pairs.

Topics to focus on for this batch:
{topics}

Question styles to incorporate:
{styles}

Strict Requirements:
1. Every question MUST be unique and completely different from previous questions.
2. Every answer MUST be historically accurate. Absolutely no hallucinations.
3. Answer length MUST be strictly between {min_words} and {max_words} words.
4. Return ONLY a valid JSON array.
5. NO markdown formatting, NO explanations, NO extra text.

Previously generated questions to AVOID (Do not repeat or paraphrase these):
{recent_questions}

Expected JSON Output Format:
[
 {{
   "question": "...",
   "answer": "..."
 }}
]"""
