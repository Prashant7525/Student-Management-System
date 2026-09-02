from pathlib import Path

from student_management.repositories.sqlite_student_repository import (
    SQLiteStudentRepository,
)
from student_management.repositories.student_repository import (
    StudentRepository,
)


def migrate_json_to_sqlite(
    json_path: str | Path = "data/students.json",
    sqlite_path: str | Path = "data/students.db",
) -> int:
    """Migrate students from JSON storage to SQLite storage."""

    json_repository = StudentRepository(json_path)
    sqlite_repository = SQLiteStudentRepository(sqlite_path)

    students = json_repository.get_all_students()

    migrated_count = 0

    for student in students.values():
        if sqlite_repository.get_student(student.student_id) is None:
            sqlite_repository.add_student(student)
            migrated_count += 1

    return migrated_count


def main() -> None:
    """Run the JSON-to-SQLite migration."""
    migrated_count = migrate_json_to_sqlite()

    print(
        f"Migration complete. "
        f"{migrated_count} student(s) migrated to SQLite."
    )


if __name__ == "__main__":
    main()