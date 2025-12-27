import os, sys, requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("changed_code.txt", "r") as f:
    code = f.read()

prompt = f"""
You are a senior DevOps engineer.

Review the code and respond in this format:
Severity: LOW | MEDIUM | CRITICAL
Summary:
- points

Code:
{code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)

result = response.choices[0].message.content
print(result)

if "CRITICAL" in result:
    sys.exit(1)
