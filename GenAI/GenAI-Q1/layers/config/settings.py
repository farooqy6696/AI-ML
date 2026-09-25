"""
Configuration Layer
--------------------
Centralizes all environment/config values so no other layer reads
os.environ directly. Keeping this in its own module also makes the
app easy to reconfigure for tests (e.g. swap in a fake Mongo URI).
"""

import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    gemini_api_key: str
    gemini_model: str
    mongo_uri: str
    mongo_db_name: str
    mongo_collection_name: str
    document_path: str


def load_settings() -> Settings:
    return Settings(
        gemini_api_key=os.getenv("GEMINI_API_KEY", ""),
        gemini_model=os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
        mongo_uri=os.getenv("MONGO_URI", "mongodb://localhost:27017"),
        mongo_db_name=os.getenv("MONGO_DB_NAME", "document_analyzer"),
        mongo_collection_name=os.getenv("MONGO_COLLECTION_NAME", "document_analysis"),
        document_path=os.getenv("DOCUMENT_PATH", "sample_document.txt"),
    )
