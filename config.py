"""Project configuration and sample requirements."""

import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = "CodeGen AI"
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

EXAMPLES = {
    "Functions": (
        "Create a Python function that checks whether a number is prime. "
        "Handle numbers less than 2 and include a usage example."
    ),
    "Data Processing": (
        "Write a pandas function that loads a CSV file, removes duplicate "
        "rows, handles missing values, and saves the cleaned file."
    ),
    "Algorithms": (
        "Implement binary search in Python. Return the index of the target "
        "or -1 when it is not found."
    ),
    "File Handling": (
        "Create a Python function that counts the lines, words, and "
        "characters in a text file. Handle missing files."
    ),
    "API Development": (
        "Create a simple Flask API with a GET /hello endpoint that "
        "returns a JSON greeting."
    ),
    "Testing": (
        "Write a Python factorial function and pytest test cases for zero, "
        "positive numbers, and invalid input."
    ),
}
