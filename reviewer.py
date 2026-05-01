from groq import Groq
import subprocess
import sys
import os

# Read .env file manually
env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
with open(env_path) as f:
    for line in f:
        if '=' in line:
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

API_KEY = os.environ.get("GROQ_API_KEY")
print(f"Key loaded: {API_KEY[:8] if API_KEY else 'NOT FOUND'}")

def get_diff():
    try:
        diff = subprocess.check_output(
            ['git', 'diff', 'HEAD~1', 'HEAD'],
            stderr=subprocess.STDOUT
        ).decode('utf-8')
        if not diff:
            diff = subprocess.check_output(
                ['git', 'diff', '--staged'],
                stderr=subprocess.STDOUT
            ).decode('utf-8')
        return diff
    except subprocess.CalledProcessError:
        return None

def review_code(diff):
    client = Groq(api_key=API_KEY)

    prompt = f"""You are a senior software engineer reviewing a pull request.
Analyze this code diff and provide feedback on:
1. Security vulnerabilities
2. Bugs or logical errors
3. Performance issues
4. Best practices violations

Be specific and actionable. Reference exact line changes.

Code diff:
{diff}"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1024
    )
    return response.choices[0].message.content

def main():
    print("AI PR Reviewer - Analyzing your changes...\n")

    diff = get_diff()

    if not diff:
        print("No changes found to review.")
        sys.exit(0)

    print("Found changes. Sending to AI for review...\n")
    print("-" * 50)

    review = review_code(diff)
    print(review)
    print("-" * 50)

if __name__ == "__main__":
    main()