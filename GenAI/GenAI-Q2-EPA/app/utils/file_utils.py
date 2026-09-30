"""
Utility helpers for saving uploaded files and extracting raw text
from PDF / DOCX employee documents.
"""
import os
import uuid
from pathlib import Path

from fastapi import UploadFile

from app.config import settings
from app.core.exceptions import FileProcessingException

ALLOWED_EXTENSIONS = {".pdf", ".docx"}


def save_upload(file: UploadFile) -> str:
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise FileProcessingException(f"Unsupported file type '{ext}'. Only PDF/DOCX allowed.")

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    unique_name = f"{uuid.uuid4().hex}{ext}"
    dest_path = os.path.join(settings.UPLOAD_DIR, unique_name)

    with open(dest_path, "wb") as out_file:
        content = file.file.read()
        out_file.write(content)

    return dest_path


def extract_text(file_path: str) -> str:
    ext = Path(file_path).suffix.lower()
    try:
        if ext == ".pdf":
            return _extract_pdf_text(file_path)
        if ext == ".docx":
            return _extract_docx_text(file_path)
    except Exception as exc:
        raise FileProcessingException(f"Failed to extract text: {exc}")
    raise FileProcessingException(f"Unsupported file type '{ext}'.")


def _extract_pdf_text(file_path: str) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader  # fallback
    reader = PdfReader(file_path)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def _extract_docx_text(file_path: str) -> str:
    import docx
    document = docx.Document(file_path)
    return "\n".join(p.text for p in document.paragraphs)
