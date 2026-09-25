"""
Data Access Layer - File Reader
--------------------------------
Responsible ONLY for reading the source document off disk.
Knows nothing about AI or the database.
"""

import os
from layers.exceptions import DocumentReadError


class FileReader:
    def read(self, file_path: str) -> str:
        """
        Reads a text document from disk and returns its contents.
        Raises DocumentReadError on any failure.
        """
        try:
            if not os.path.exists(file_path):
                raise DocumentReadError(f"File not found: {file_path}")

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            if not content:
                raise DocumentReadError(f"File is empty: {file_path}")

            return content

        except DocumentReadError:
            raise
        except OSError as e:
            raise DocumentReadError(f"Could not read file '{file_path}': {e}") from e
