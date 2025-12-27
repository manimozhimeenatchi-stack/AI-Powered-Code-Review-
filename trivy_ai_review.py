import json, os, sys, requests
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("trivy-report.json") as f:
    report = json.load(f)

prompt = f"""
You are a DevSecOps engineer.

Summarize the vulnerabilities with severity counts and fixes.
Mark if CRITICAL exists.

Report:
{json.dumps(report)[:12000]}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user","content":prompt}]
)

result = response.choices[0].message.content
print(result)

with open("ai-security-summary.txt", "w") as f:
    f.write(result)

if "CRITICAL" in result:
    sys.exit(1)
