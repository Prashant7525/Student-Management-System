from student_management.models.student import Student
from student_management.repositories.sqlite_student_repository import (
    SQLiteStudentRepository,
)


def create_student(
    student_id: str = "STU001",
    name: str = "Rahul Kumar",
    age: int = 20,
    email: str = "rahul@example.com",
    course: str = "Computer Science",
    marks: dict[str, float] | None = None,
) -> Student:
    """Create a test student."""
    return Student(
        student_id=student_id,
        name=name,
        age=age,
        email=email,
        course=course,
        marks=marks or {},
    )


def test_database_and_table_are_created(tmp_path):
    """The repository should create the database and table."""
    database_path = tmp_path / "students.db"

    repository = SQLiteStudentRepository(database_path)

    assert database_path.exists()
    assert repository.get_all_students() == {}


def test_add_and_get_student(tmp_path):
    """A student should be saved and retrieved correctly."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")
    student = create_student()

    repository.add_student(student)

    result = repository.get_student("STU001")

    assert result == student


def test_get_student_returns_none_when_not_found(tmp_path):
    """A missing student should return None."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    result = repository.get_student("STU999")

    assert result is None


def test_get_all_students(tmp_path):
    """The repository should return all stored students."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student_one = create_student()
    student_two = create_student(
        student_id="STU002",
        name="Amit Sharma",
        email="amit@example.com",
        course="Artificial Intelligence",
    )

    repository.add_student(student_one)
    repository.add_student(student_two)

    students = repository.get_all_students()

    assert len(students) == 2
    assert students["STU001"] == student_one
    assert students["STU002"] == student_two


def test_update_student(tmp_path):
    """An existing student should be updated correctly."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student = create_student()
    repository.add_student(student)

    updated_student = create_student(
        name="Rahul Singh",
        age=21,
        email="rahul.singh@example.com",
        course="Data Science",
    )

    result = repository.update_student(updated_student)

    assert result is True
    assert repository.get_student("STU001") == updated_student


def test_update_nonexistent_student(tmp_path):
    """Updating a missing student should return False."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student = create_student()

    result = repository.update_student(student)

    assert result is False


def test_delete_student(tmp_path):
    """An existing student should be deleted correctly."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student = create_student()
    repository.add_student(student)

    result = repository.delete_student("STU001")

    assert result is True
    assert repository.get_student("STU001") is None


def test_delete_nonexistent_student(tmp_path):
    """Deleting a missing student should return False."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    result = repository.delete_student("STU999")

    assert result is False


def test_marks_persist_correctly(tmp_path):
    """Student marks should persist correctly in SQLite."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student = create_student(
        marks={
            "Python": 90.0,
            "Database": 85.0,
        }
    )

    repository.add_student(student)

    loaded_student = repository.get_student("STU001")

    assert loaded_student is not None
    assert loaded_student.marks == {
        "Python": 90.0,
        "Database": 85.0,
    }


def test_updated_marks_persist_correctly(tmp_path):
    """Updated marks should persist correctly."""
    repository = SQLiteStudentRepository(tmp_path / "students.db")

    student = create_student(
        marks={
            "Python": 90.0,
        }
    )

    repository.add_student(student)

    student.marks["Python"] = 95.0
    student.marks["Mathematics"] = 88.0

    result = repository.update_student(student)

    assert result is True

    loaded_student = repository.get_student("STU001")

    assert loaded_student is not None
    assert loaded_student.marks == {
        "Python": 95.0,
        "Mathematics": 88.0,
    }