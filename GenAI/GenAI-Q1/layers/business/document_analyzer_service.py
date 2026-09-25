"""
Business Layer - Document Analyzer Service
---------------------------------------------
Orchestrates the use case: read document -> summarize -> generate
interview questions -> persist. This is the only layer that knows
about the full workflow; it delegates the actual work to the data
access layer (FileReader, MongoRepository) and the GeminiService.
"""

from dataclasses import dataclass
from typing import List

from layers.data_access.file_reader import FileReader
from layers.data_access.mongo_repository import MongoRepository
from layers.business.gemini_service import GeminiService


@dataclass
class AnalysisResult:
    document_path: str
    summary: str
    interview_questions: List[str]
    mongo_record_id: str


class DocumentAnalyzerService:
    def __init__(
        self,
        file_reader: FileReader,
        gemini_service: GeminiService,
        mongo_repository: MongoRepository,
    ):
        self._file_reader = file_reader
        self._gemini_service = gemini_service
        self._mongo_repository = mongo_repository

    def analyze(self, document_path: str) -> AnalysisResult:
        # Step 1: Read the document
        document_text = self._file_reader.read(document_path)
        print("Document Read Successfully.")

        # Step 2: Generate summary
        summary = self._gemini_service.generate_summary(document_text)
        print("Document Summary Generated Successfully.")

        # Step 3: Generate interview questions
        interview_questions = self._gemini_service.generate_interview_questions(document_text)
        print("Interview Questions Generated Successfully.")

        # Step 4: Persist to MongoDB
        record_id = self._mongo_repository.save_analysis(
            document_path=document_path,
            summary=summary,
            interview_questions=interview_questions,
        )
        print("Analysis Saved to MongoDB.")

        return AnalysisResult(
            document_path=document_path,
            summary=summary,
            interview_questions=interview_questions,
            mongo_record_id=record_id,
        )
