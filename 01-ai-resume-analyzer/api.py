"""Job-ready Resume Analyzer API logic."""
from pathlib import Path
import re

SKILLS = ["python","django","fastapi","react","javascript","typescript","sql","postgresql","machine learning","scikit-learn","pytorch","tensorflow","docker","git","aws","rest api","nlp"]

def extract_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()

def analyze_resume(resume_text: str, job_description: str) -> dict:
    resume = extract_text(resume_text).lower()
    job = extract_text(job_description).lower()
    required = [s for s in SKILLS if s in job]
    matched = [s for s in required if s in resume]
    missing = [s for s in required if s not in resume]
    score = round((len(matched) / len(required)) * 100, 2) if required else 0
    return {"match_score": score, "matched_skills": matched, "missing_skills": missing, "recommendation": "Strong match" if score >= 75 else "Improve missing skills" if score >= 50 else "Needs improvement"}
