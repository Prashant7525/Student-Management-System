import json
import sqlite3
from pathlib import Path

from student_management.models.student import Student


class SQLiteStudentRepository:
    """Handle persistent student storage using SQLite."""

    def __init__(self, database_path: str | Path = "data/students.db"):
        self.database_path = Path(database_path)
        self.database_path.parent.mkdir(parents=True, exist_ok=True)

        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Create and return a SQLite database connection."""
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row

        return connection

    def _create_table(self) -> None:
        """Create the students table if it does not exist."""
        with self._get_connection() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS students (
                    student_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    course TEXT NOT NULL,
                    marks TEXT NOT NULL
                )
                """
            )

            connection.commit()

    @staticmethod
    def _student_from_row(row: sqlite3.Row) -> Student:
        """Convert a database row into a Student object."""
        return Student(
            student_id=row["student_id"],
            name=row["name"],
            age=row["age"],
            email=row["email"],
            course=row["course"],
            marks=json.loads(row["marks"]),
        )

    def add_student(self, student: Student) -> None:
        """Add a student to the database."""
        with self._get_connection() as connection:
            connection.execute(
                """
                INSERT INTO students (
                    student_id,
                    name,
                    age,
                    email,
                    course,
                    marks
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    student.student_id,
                    student.name,
                    student.age,
                    student.email,
                    student.course,
                    json.dumps(student.marks),
                ),
            )

            connection.commit()

    def get_student(self, student_id: str) -> Student | None:
        """Return a student by ID, or None if not found."""
        with self._get_connection() as connection:
            row = connection.execute(
                """
                SELECT
                    student_id,
                    name,
                    age,
                    email,
                    course,
                    marks
                FROM students
                WHERE student_id = ?
                """,
                (student_id,),
            ).fetchone()

        if row is None:
            return None

        return self._student_from_row(row)

    def get_all_students(self) -> dict[str, Student]:
        """Return all students."""
        with self._get_connection() as connection:
            rows = connection.execute(
                """
                SELECT
                    student_id,
                    name,
                    age,
                    email,
                    course,
                    marks
                FROM students
                ORDER BY student_id
                """
            ).fetchall()

        return {
            row["student_id"]: self._student_from_row(row)
            for row in rows
        }

    def update_student(self, student: Student) -> bool:
        """Update an existing student.

        Returns True if the student existed and was updated.
        """
        with self._get_connection() as connection:
            cursor = connection.execute(
                """
                UPDATE students
                SET
                    name = ?,
                    age = ?,
                    email = ?,
                    course = ?,
                    marks = ?
                WHERE student_id = ?
                """,
                (
                    student.name,
                    student.age,
                    student.email,
                    student.course,
                    json.dumps(student.marks),
                    student.student_id,
                ),
            )

            connection.commit()

        return cursor.rowcount > 0

    def delete_student(self, student_id: str) -> bool:
        """Delete a student.

        Returns True if the student existed and was deleted.
        """
        with self._get_connection() as connection:
            cursor = connection.execute(
                """
                DELETE FROM students
                WHERE student_id = ?
                """,
                (student_id,),
            )

            connection.commit()

        return cursor.rowcount > 0