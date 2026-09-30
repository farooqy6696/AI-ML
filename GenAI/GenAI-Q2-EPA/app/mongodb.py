"""
MongoDB connection.
Used for unstructured data: uploaded document metadata, extracted text,
and AI-generated outputs (summaries, skill extraction, recommendations).
"""
from pymongo import MongoClient
from app.config import settings

_client = MongoClient(settings.MONGO_URI, serverSelectionTimeoutMS=3000)
_db = _client[settings.MONGO_DB_NAME]

documents_collection = _db["employee_documents"]
ai_outputs_collection = _db["ai_outputs"]


def get_mongo_db():
    return _db
