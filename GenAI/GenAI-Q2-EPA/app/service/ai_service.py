"""
AI Service
Wraps the Google Gemini API to power all AI features:
- Summarize employee documents
- Extract technical skills
- Recommend learning paths
- Generate personalized interview questions
- Compare employee skill profiles
- Suggest career growth plans
"""
import json
from typing import List, Dict, Any

import google.generativeai as genai

from app.config import settings
from app.core.exceptions import AIServiceException
from app.mongodb import ai_outputs_collection

if settings.GEMINI_API_KEY:
    genai.configure(api_key=settings.GEMINI_API_KEY)


class AIService:
    def __init__(self):
        self.model_name = settings.GEMINI_MODEL

    def _get_model(self):
        if not settings.GEMINI_API_KEY:
            raise AIServiceException(
                "GEMINI_API_KEY is not configured. Set it in your .env file."
            )
        return genai.GenerativeModel(self.model_name)

    def _generate(self, prompt: str) -> str:
        try:
            model = self._get_model()
            response = model.generate_content(prompt)
            return (response.text or "").strip()
        except AIServiceException:
            raise
        except Exception as exc:
            raise AIServiceException(f"Gemini API call failed: {exc}")

    def _log_output(self, employee_id: int, feature: str, output: Any):
        ai_outputs_collection.insert_one(
            {"employee_id": employee_id, "feature": feature, "output": output}
        )

    # ---- Feature: Summarize employee documents ----
    def summarize_document(self, employee_id: int, document_text: str) -> str:
        prompt = (
            "Summarize the following employee document in 4-6 concise sentences, "
            "highlighting role-relevant experience, achievements, and skills:\n\n"
            f"{document_text[:12000]}"
        )
        summary = self._generate(prompt)
        self._log_output(employee_id, "document_summary", summary)
        return summary

    # ---- Feature: Extract technical skills ----
    def extract_skills(self, employee_id: int, document_text: str) -> List[str]:
        prompt = (
            "Extract a JSON array of distinct technical skills (programming languages, "
            "frameworks, tools, platforms) mentioned in the text below. "
            "Respond with ONLY a JSON array of strings, nothing else.\n\n"
            f"{document_text[:12000]}"
        )
        raw = self._generate(prompt)
        skills = self._safe_json_list(raw)
        self._log_output(employee_id, "extracted_skills", skills)
        return skills

    # ---- Feature: Recommend learning paths ----
    def recommend_learning_path(self, employee_id: int, current_skills: List[str], designation: str) -> List[str]:
        prompt = (
            f"An employee working as a '{designation}' has these current skills: "
            f"{', '.join(current_skills) if current_skills else 'none listed'}. "
            "Recommend a JSON array of 5 specific learning paths / courses / certifications "
            "that would advance their career. Respond with ONLY a JSON array of strings."
        )
        raw = self._generate(prompt)
        recs = self._safe_json_list(raw)
        self._log_output(employee_id, "learning_path", recs)
        return recs

    # ---- Feature: Generate personalized interview questions ----
    def generate_interview_questions(self, employee_id: int, designation: str, skills: List[str]) -> List[str]:
        prompt = (
            f"Generate a JSON array of 8 personalized interview questions for a '{designation}' "
            f"candidate with skills in {', '.join(skills) if skills else 'general areas'}. "
            "Mix technical and behavioral questions. Respond with ONLY a JSON array of strings."
        )
        raw = self._generate(prompt)
        questions = self._safe_json_list(raw)
        self._log_output(employee_id, "interview_questions", questions)
        return questions

    # ---- Feature: Compare employee skill profiles ----
    def compare_skill_profiles(self, employee_a: Dict[str, Any], employee_b: Dict[str, Any]) -> str:
        prompt = (
            "Compare these two employee skill profiles and summarize strengths, overlaps, "
            "and unique differentiators in 4-6 sentences.\n\n"
            f"Employee A ({employee_a.get('name')}): {employee_a.get('skills')}\n"
            f"Employee B ({employee_b.get('name')}): {employee_b.get('skills')}"
        )
        comparison = self._generate(prompt)
        self._log_output(employee_a.get("employee_id"), "skill_comparison", comparison)
        return comparison

    # ---- Feature: Suggest career growth plans ----
    def suggest_career_growth(self, employee_id: int, designation: str, performance_score: float, experience: float) -> str:
        prompt = (
            f"An employee is a '{designation}' with {experience} years of experience and a "
            f"performance score of {performance_score}/100. Suggest a concise 6-12 month "
            "career growth plan with concrete milestones."
        )
        plan = self._generate(prompt)
        self._log_output(employee_id, "career_growth_plan", plan)
        return plan

    @staticmethod
    def _safe_json_list(raw: str) -> List[str]:
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = cleaned.strip("`")
            cleaned = cleaned.replace("json\n", "", 1).replace("json", "", 1)
        try:
            parsed = json.loads(cleaned)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            pass
        # Fallback: split by newlines/commas if the model didn't return clean JSON
        return [line.strip("-• ").strip() for line in cleaned.splitlines() if line.strip()]


ai_service = AIService()
