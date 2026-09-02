from typing import Protocol

from student_management.models.student import Student


class StudentRepositoryProtocol(Protocol):
    """Define the storage operations required by the service layer."""

    def add_student(self, student: Student) -> None:
        """Add a student to storage."""
        ...

    def get_student(self, student_id: str) -> Student | None:
        """Return a student by ID, or None if not found."""
        ...

    def get_all_students(self) -> dict[str, Student]:
        """Return all stored students."""
        ...

    def update_student(self, student: Student) -> bool:
        """Update an existing student."""
        ...

    def delete_student(self, student_id: str) -> bool:
        """Delete a student."""
        ...