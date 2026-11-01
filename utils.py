"""Helpers for parsing and validating generated Python code."""

import ast
import re

def extract_code_and_explanation(answer):
    """Extract the first fenced code block and the remaining explanation."""
    match = re.search(
        r"```(?:python)?\s*(.*?)```",
        answer,
        re.DOTALL | re.IGNORECASE,
    )

    if not match:
        return answer.strip(), "No separate explanation was returned. Review the code."

    code = match.group(1).strip()
    explanation = answer[match.end():].strip()

    explanation = re.sub(
        r"^Explanation:\s*",
        "",
        explanation,
        flags=re.IGNORECASE,
    )

    if not explanation:
        explanation = answer[:match.start()].strip()

    return code, explanation or "No explanation was provided."

def check_python_syntax(code):
    """Return (is_valid, message); does not execute generated code."""
    try:
        ast.parse(code)
        return True, "Python syntax check passed."
    except SyntaxError as error:
        return False, f"Syntax error on line {error.lineno}: {error.msg}"
