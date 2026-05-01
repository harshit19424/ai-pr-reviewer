# AI PR Reviewer

An AI-powered code review tool that automatically analyzes git diffs using LLM APIs and provides instant feedback on security vulnerabilities, bugs, and best practices — directly in your terminal.

---

## What It Does

- Detects your latest git changes automatically
- Sends the diff to an LLM (LLaMA 3.3 70B via Groq) for analysis
- Returns structured feedback on:
  - Security vulnerabilities (hardcoded secrets, SQL injection, etc.)
  - Bugs and logical errors
  - Performance issues
  - Best practices violations

---

## Example Output

```
AI PR Reviewer - Analyzing your changes...
Found changes. Sending to AI for review...

--------------------------------------------------
Security Vulnerabilities:
1. Hardcoded password 'admin123' detected on line 4.
   Recommendation: Use environment variables or a secrets manager.

2. SQL Injection vulnerability on line 5.
   The query is built via string concatenation with user input.
   Recommendation: Use parameterized queries instead.

Best Practices Violations:
1. Unused import 'logging' on line 2. Remove it or use it.
2. Missing docstring on function get_user(). Add documentation.
--------------------------------------------------
```

---

## Tech Stack

- **Language:** Python
- **LLM:** LLaMA 3.3 70B via Groq API
- **Libraries:** groq, python-dotenv
- **Tools:** Git

---

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/harshit19424/ai-pr-reviewer.git
cd ai-pr-reviewer
```

### 2. Install dependencies
```bash
pip install groq python-dotenv
```

### 3. Get a free Groq API key
Sign up at [console.groq.com](https://console.groq.com) — no credit card required.

### 4. Create a `.env` file
```bash
GROQ_API_KEY=your-key-here
```

### 5. Run it inside any git repository
```bash
python reviewer.py
```

---

## How It Works

1. Runs `git diff HEAD~1 HEAD` to capture your latest commit changes
2. Sends the raw diff to LLaMA 3.3 70B with a structured prompt
3. The model analyzes the changes and returns categorized feedback
4. Output is printed directly to your terminal

---

## Security

- API keys are stored in `.env` which is excluded via `.gitignore`
- No code or diffs are stored — everything is processed in memory and discarded

---

## Future Improvements

- [ ] GitHub Actions integration to run automatically on every PR
- [ ] Post review comments directly to GitHub Pull Requests via API
- [ ] Support for multiple file diffs in a single review
- [ ] Severity scoring (Critical / Warning / Info) for each finding
