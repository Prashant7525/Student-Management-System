import os
from pathlib import Path


DEFAULT_DATABASE_PATH = Path("data/students.db")


def get_database_path() -> Path:
    """Return the SQLite database path.

    The path can be configured using the
    STUDENT_DATABASE_PATH environment variable.
    """
    configured_path = os.getenv("STUDENT_DATABASE_PATH")

    if configured_path:
        return Path(configured_path)

    return DEFAULT_DATABASE_PATH