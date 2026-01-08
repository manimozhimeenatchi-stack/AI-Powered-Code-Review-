<<<<<<< HEAD
# AI DevSecOps Pipeline

This project combines:
- AI Code Review
- Trivy Vulnerability Scan
- AI Security Summary
- GitOps-style PR enforcement

## Features
- Blocks merge on CRITICAL issues
- Uploads AI security report as artifact
- Cloud AI powered (OpenAI)

## Interview Pitch
"I built an AI-powered DevSecOps pipeline that combines static code review and container security scanning, summarized by an LLM and enforced via GitOps policies in GitHub Actions."
=======
# AI-Powered-Code-Review-
>>>>>>> 40aa23e8539b39be42384b2c452e06c2b03bdcb6


AI CODE REVIEW PROJECT USING OPENAI

https://github.com/manimozhimeenatchi-stack/AI-Powered-Code-Review-.git

✅STEP1:CREATE A SECRET KEY IN OPENAI 

directly visit:  https://platform.openai.com/api-keys
Click “Create new secret key”
Give it a name (example): ai-code-review
Click Create
⚠️ Important:
You will see the key only once.
👉 Copy it immediately and store it safely.

✅STEP2:SAVE IT IN GIT HUB

Go to Repo → Settings → Secrets and variables → Actions
Click New repository secret
Name: OPENAI_API_KEY
Paste the key → Save

✅STEP3:MAKE CHANGES IN THE REPO

git clone https://github.com/manimozhimeenatchi-stack/AI-Powered-Code-Review-.git
cd AI-Powered-Code-Review-
git pull origin main
git checkout -b changefile
git branch
ls 
vi requirement.txt
		django>=4.2.10
		OPENAI_API_KEY=sk-test123456789
git add .
git commit -m "Update README with project architecture"
git push origin changefile

✅STEP4:Create a Pull Request (GitHub)

Go to GitHub
Click Compare & Pull Request
Add description
Create PR

now change the ai-risk-score theshold limit
failing threshold
SECURITY_SCORE=8
MAINTAINABILITY_SCORE=6
PERFORMANCE_SCORE=5
working threshold
SECURITY_SCORE=4
MAINTAINABILITY_SCORE=4
PERFORMANCE_SCORE=3
