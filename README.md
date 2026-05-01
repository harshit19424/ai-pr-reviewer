Set-Content -Path "README.md" -Encoding utf8 -Value @"
# AI PR Reviewer

An AI-powered code review tool that automatically analyzes git diffs 
using LLM APIs and provides instant feedback on security vulnerabilities, 
bugs, and best practices.

## What It Does
- Detects your latest git changes automatically
- Sends the diff to an LLM for analysis  
- Returns structured feedback on security, bugs, and code quality
- Catches issues like hardcoded secrets, SQL injection, and missing error handling

## Tech Stack
- Python
- Groq API (LLaMA 3.3 70B)
- Git

## Setup
pip install groq

Set your API key:
GROQ_API_KEY=your-key-here

## Usage
python reviewer.py

## Example Output
The tool identified these issues in a sample file:
- Hardcoded password exposed in source code
- SQL injection vulnerability via string concatenation
- Unused imports
- Missing error handling and docstrings
"@