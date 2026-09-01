import json
from pathlib import Path

from student_management.models.student import Student


class StudentRepository:
    """Handle persistent storage of student records using JSON."""

    def __init__(self, file_path: str | Path = "data/students.json"):
        self.file_path = Path(file_path)

    def save_students(self, students: dict[str, Student]) -> None:
        """Save all students to the JSON file."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            student_id: {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "email": student.email,
                "course": student.course,
                "marks": student.marks,
            }
            for student_id, student in students.items()
        }

        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_students(self) -> dict[str, Student]:
        """Load all students from the JSON file."""
        if not self.file_path.exists():
            return {}

        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

        students = {}

        for student_id, student_data in data.items():
            students[student_id] = Student(
                student_id=student_data["student_id"],
                name=student_data["name"],
                age=student_data["age"],
                email=student_data["email"],
                course=student_data["course"],
                marks=student_data.get("marks", {}),
            )

        return students

    def add_student(self, student: Student) -> None:
        """Add a student to persistent storage."""
        students = self.load_students()

        students[student.student_id] = student

        self.save_students(students)

    def get_student(self, student_id: str) -> Student | None:
        """Return a student by ID, or None if not found."""
        students = self.load_students()

        return students.get(student_id)

    def get_all_students(self) -> dict[str, Student]:
        """Return all stored students."""
        return self.load_students()

    def update_student(self, student: Student) -> bool:
        """Update an existing student.

        Returns True if the student existed and was updated.
        """
        students = self.load_students()

        if student.student_id not in students:
            return False

        students[student.student_id] = student

        self.save_students(students)

        return True

    def delete_student(self, student_id: str) -> bool:
        """Delete a student.

        Returns True if the student existed and was deleted.
        """
        students = self.load_students()

        if student_id not in students:
            return False

        del students[student_id]

        self.save_students(students)

        return True