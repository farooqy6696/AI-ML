"""
Business Layer - Gemini AI Service
------------------------------------
Responsible ONLY for talking to the Gemini API: summarizing text
and generating interview questions from it.
"""

import re
from typing import List

import google.generativeai as genai

from layers.exceptions import GeminiServiceError


class GeminiService:
    def __init__(self, api_key: str, model_name: str = "gemini-1.5-flash"):
        if not api_key:
            raise GeminiServiceError("GEMINI_API_KEY is missing. Set it in your .env file.")
        try:
            genai.configure(api_key=api_key)
            self._model = genai.GenerativeModel(model_name)
        except Exception as e:
            raise GeminiServiceError(f"Failed to initialize Gemini model: {e}") from e

    def _generate(self, prompt: str) -> str:
        try:
            response = self._model.generate_content(prompt)
            text = (response.text or "").strip()
            if not text:
                raise GeminiServiceError("Gemini returned an empty response.")
            return text
        except GeminiServiceError:
            raise
        except Exception as e:
            raise GeminiServiceError(f"Gemini API call failed: {e}") from e

    def generate_summary(self, document_text: str) -> str:
        prompt = (
            "Summarize the following document in a concise, well-structured "
            "paragraph (4-6 sentences). Focus on the key ideas only.\n\n"
            f"Document:\n{document_text}"
        )
        return self._generate(prompt)

    def generate_interview_questions(self, document_text: str, num_questions: int = 5) -> List[str]:
        prompt = (
            f"Based on the following document, generate exactly {num_questions} "
            "insightful interview questions that test a candidate's understanding "
            "of the material. Return ONLY the questions as a numbered list, "
            "with no extra commentary.\n\n"
            f"Document:\n{document_text}"
        )
        raw_text = self._generate(prompt)
        return self._parse_questions(raw_text)

    @staticmethod
    def _parse_questions(raw_text: str) -> List[str]:
        """Turns a numbered-list response into a clean list of question strings."""
        lines = raw_text.strip().splitlines()
        questions = []
        for line in lines:
            cleaned = re.sub(r"^\s*[\d]+[\.\)]\s*", "", line).strip()
            cleaned = re.sub(r"^[-*]\s*", "", cleaned).strip()
            if cleaned:
                questions.append(cleaned)

        if not questions:
            raise GeminiServiceError("Could not parse any interview questions from Gemini's response.")
        return questions
