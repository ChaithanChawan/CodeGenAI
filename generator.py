"""Gemini API integration and streaming code generation."""

import os
import time

from google import genai
from config import MODEL

def stream_gemini_response(requirement, on_chunk=None):
    """
    Ask Gemini to generate code and stream text as it arrives.

    Args:
        requirement: User's natural-language software requirement.
        on_chunk: Optional callback receiving the accumulated response.

    Returns:
        (answer_text, elapsed_seconds)
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY was not found. Check your local .env file."
        )

    prompt = f"""
You are CodeGen AI, an expert Python developer.

Convert the user's software requirement into a useful Python 3 code snippet.

Instructions:
- Write complete, readable code with sensible names.
- Include necessary imports.
- Handle relevant edge cases.
- Include a short usage example when appropriate.
- Keep the answer focused and avoid unnecessary explanation.
- Do not include secrets or credentials.
- Do not claim code was tested unless it was actually tested.
- Do not use dangerous operations.

Return one Python code block followed by a short explanation.

User requirement:
{requirement}
"""

    client = genai.Client(api_key=api_key)
    chunks = []
    start_time = time.time()

    stream = client.interactions.create(
        model=MODEL,
        input=prompt,
        stream=True,
    )

    for event in stream:
        if getattr(event, "event_type", "") == "step.delta":
            delta = getattr(event, "delta", None)
            if getattr(delta, "type", None) == "text":
                chunk = getattr(delta, "text", "")
                if chunk:
                    chunks.append(chunk)
                    if on_chunk:
                        on_chunk("".join(chunks))

    return "".join(chunks).strip(), time.time() - start_time
