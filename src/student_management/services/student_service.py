from student_management.models.student import Student
from student_management.repositories.student_repository import StudentRepository
from student_management.utils.validators import (
    validate_age,
    validate_course,
    validate_email,
    validate_mark,
    validate_name,
    validate_student_id,
)


class StudentService:
    """Provide business operations for managing students."""

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def add_student(
        self,
        student_id: str,
        name: str,
        age: int,
        email: str,
        course: str,
    ) -> Student:
        """Validate and add a new student."""

        student_id = student_id.strip()
        name = name.strip()
        email = email.strip()
        course = course.strip()

        if not validate_student_id(student_id):
            raise ValueError("Invalid student ID.")

        if not validate_name(name):
            raise ValueError("Invalid student name.")

        if not validate_age(age):
            raise ValueError("Invalid age.")

        if not validate_email(email):
            raise ValueError("Invalid email address.")

        if not validate_course(course):
            raise ValueError("Invalid course.")

        if self.repository.get_student(student_id) is not None:
            raise ValueError(
                f"Student with ID '{student_id}' already exists."
            )

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            course=course,
        )

        self.repository.add_student(student)

        return student

    def get_student(self, student_id: str) -> Student | None:
        """Return a student by ID."""
        return self.repository.get_student(student_id.strip())

    def get_all_students(self) -> dict[str, Student]:
        """Return all students."""
        return self.repository.get_all_students()

    def search_students(self, query: str) -> list[Student]:
        """Search students by ID, name, email, or course."""
        query = query.strip().lower()

        if not query:
            return []

        students = self.repository.get_all_students()

        return [
            student
            for student in students.values()
            if (
                query in student.student_id.lower()
                or query in student.name.lower()
                or query in student.email.lower()
                or query in student.course.lower()
            )
        ]

    def update_student(
        self,
        student_id: str,
        name: str,
        age: int,
        email: str,
        course: str,
    ) -> Student:
        """Validate and update an existing student."""

        student_id = student_id.strip()
        name = name.strip()
        email = email.strip()
        course = course.strip()

        existing_student = self.repository.get_student(student_id)

        if existing_student is None:
            raise ValueError(
                f"Student with ID '{student_id}' does not exist."
            )

        if not validate_student_id(student_id):
            raise ValueError("Invalid student ID.")

        if not validate_name(name):
            raise ValueError("Invalid student name.")

        if not validate_age(age):
            raise ValueError("Invalid age.")

        if not validate_email(email):
            raise ValueError("Invalid email address.")

        if not validate_course(course):
            raise ValueError("Invalid course.")

        updated_student = Student(
            student_id=student_id,
            name=name,
            age=age,
            email=email,
            course=course,
            marks=existing_student.marks.copy(),
        )

        self.repository.update_student(updated_student)

        return updated_student

    def delete_student(self, student_id: str) -> bool:
        """Delete a student by ID."""
        student_id = student_id.strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        return self.repository.delete_student(student_id)

    def add_marks(
        self,
        student_id: str,
        subject: str,
        mark: float,
    ) -> Student:
        """Add or update a student's mark for a subject."""

        student_id = student_id.strip()
        subject = subject.strip()

        student = self.repository.get_student(student_id)

        if student is None:
            raise ValueError(
                f"Student with ID '{student_id}' does not exist."
            )

        if not subject:
            raise ValueError("Subject cannot be empty.")

        if not validate_mark(mark):
            raise ValueError("Mark must be between 0 and 100.")

        student.marks[subject] = mark

        self.repository.update_student(student)

        return student

    def remove_marks(
        self,
        student_id: str,
        subject: str,
    ) -> Student:
        """Remove a subject mark from a student."""

        student_id = student_id.strip()
        subject = subject.strip()

        student = self.repository.get_student(student_id)

        if student is None:
            raise ValueError(
                f"Student with ID '{student_id}' does not exist."
            )

        if subject not in student.marks:
            raise ValueError(
                f"Subject '{subject}' does not exist for this student."
            )

        del student.marks[subject]

        self.repository.update_student(student)

        return student