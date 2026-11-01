# CodeGen AI – Code Snippet Generator

An AI-powered Python code snippet generator that converts natural-language requirements into Python code using Google's Gemini API.

## Overview

CodeGen AI helps developers translate feature requirements into Python code snippets quickly. Users enter a requirement in plain English, and the application generates relevant Python code along with an explanation.

## Features

* Natural-language requirement input
* AI-powered Python code generation using Gemini API
* Streaming output
* Python syntax validation
* Code explanation
* Download generated code
* Generation history
* Dark-themed Streamlit interface

## Tech Stack

* Python
* Streamlit
* Google Gemini API
* Google GenAI SDK
* Python AST
* python-dotenv

## Project Structure

```text
CodeGenAI/
├── app.py
├── generator.py
├── styles.py
├── config.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ChaithanChawan/CodeGenAI.git
cd CodeGenAI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

4. Run the application:

```bash
python -m streamlit run app.py
```

## Security

Never upload your `.env` file or expose your Gemini API key publicly.

## Author

Chaithan Chawan

GitHub: https://github.com/ChaithanChawan
