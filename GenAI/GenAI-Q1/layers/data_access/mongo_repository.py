"""
Data Access Layer - MongoDB Repository
----------------------------------------
Responsible ONLY for persistence. Knows nothing about how the
summary/questions were generated, just how to store and fetch them.
"""

from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from layers.exceptions import MongoRepositoryError


class MongoRepository:
    def __init__(self, uri: str, db_name: str, collection_name: str):
        try:
            self._client = MongoClient(uri, serverSelectionTimeoutMS=5000)
            # Force a round trip so connection issues surface immediately.
            self._client.admin.command("ping")
            self._db = self._client[db_name]
            self._collection = self._db[collection_name]
        except PyMongoError as e:
            raise MongoRepositoryError(f"Could not connect to MongoDB: {e}") from e

    def save_analysis(
        self,
        document_path: str,
        summary: str,
        interview_questions: List[str],
    ) -> str:
        """Persists the analysis result and returns the inserted document's id."""
        try:
            record: Dict[str, Any] = {
                "document_path": document_path,
                "summary": summary,
                "interview_questions": interview_questions,
                "created_at": datetime.now(timezone.utc),
            }
            result = self._collection.insert_one(record)
            return str(result.inserted_id)
        except PyMongoError as e:
            raise MongoRepositoryError(f"Failed to save analysis to MongoDB: {e}") from e

    def find_latest(self) -> Optional[Dict[str, Any]]:
        try:
            return self._collection.find_one(sort=[("created_at", -1)])
        except PyMongoError as e:
            raise MongoRepositoryError(f"Failed to read from MongoDB: {e}") from e

    def close(self) -> None:
        self._client.close()
