"""
Custom exceptions for the Intelligent Document Analyzer.

Using dedicated exception types (instead of letting raw library
exceptions bubble up) lets the presentation layer show clear,
specific error messages for each stage of the pipeline.
"""


class DocumentAnalyzerError(Exception):
    """Base class for all application-specific errors."""


class DocumentReadError(DocumentAnalyzerError):
    """Raised when the source document cannot be read."""


class GeminiServiceError(DocumentAnalyzerError):
    """Raised when the Gemini API call fails or returns bad data."""


class MongoRepositoryError(DocumentAnalyzerError):
    """Raised when storing/reading data from MongoDB fails."""
