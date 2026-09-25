"""
Presentation Layer - Entry Point
-----------------------------------
Wires up all layers (config -> data access -> business) and drives
the use case. This is the only file that should ever be "run".

Layered Architecture:
    main.py                                 (presentation)
    layers/business/                        (business logic)
        gemini_service.py
        document_analyzer_service.py
    layers/data_access/                     (data access)
        file_reader.py
        mongo_repository.py
    layers/config/settings.py               (configuration)
    layers/exceptions.py                    (shared exception types)
"""

from layers.config.settings import load_settings
from layers.data_access.file_reader import FileReader
from layers.data_access.mongo_repository import MongoRepository
from layers.business.gemini_service import GeminiService
from layers.business.document_analyzer_service import DocumentAnalyzerService
from layers.exceptions import DocumentAnalyzerError


def main() -> None:
    settings = load_settings()
    mongo_repository = None

    try:
        # --- Wire up dependencies (simple manual DI) ---
        file_reader = FileReader()
        gemini_service = GeminiService(
            api_key=settings.gemini_api_key,
            model_name=settings.gemini_model,
        )
        mongo_repository = MongoRepository(
            uri=settings.mongo_uri,
            db_name=settings.mongo_db_name,
            collection_name=settings.mongo_collection_name,
        )

        analyzer_service = DocumentAnalyzerService(
            file_reader=file_reader,
            gemini_service=gemini_service,
            mongo_repository=mongo_repository,
        )

        # --- Run the use case ---
        result = analyzer_service.analyze(settings.document_path)

        # --- Display expected output ---
        print("Operation Completed Successfully.")
        print("\n--- Summary ---")
        print(result.summary)

        print("\n--- Interview Questions ---")
        for i, question in enumerate(result.interview_questions, start=1):
            print(f"{i}. {question}")

        print(f"\nSaved MongoDB Record ID: {result.mongo_record_id}")

    except DocumentAnalyzerError as e:
        # Any known, application-specific failure (file/Gemini/Mongo)
        print(f"Operation Failed: {e}")
    except Exception as e:
        # Safety net for anything unexpected
        print(f"Unexpected Error: {e}")
    finally:
        if mongo_repository is not None:
            mongo_repository.close()


if __name__ == "__main__":
    main()
