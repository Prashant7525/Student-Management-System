from student_management.models.student import Student
from student_management.repositories.student_repository import StudentRepository


def create_student(student_id: str = "STU001") -> Student:
    """Create a sample student for testing."""
    return Student(
        student_id=student_id,
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
        marks={
            "Mathematics": 85,
            "Science": 78,
            "English": 92,
        },
    )


def test_load_students_when_file_does_not_exist(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    students = repository.load_students()

    assert students == {}


def test_save_and_load_students(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student = create_student()

    repository.save_students({
        student.student_id: student
    })

    loaded_students = repository.load_students()

    assert "STU001" in loaded_students
    assert loaded_students["STU001"].name == "Rahul Kumar"
    assert loaded_students["STU001"].age == 20
    assert loaded_students["STU001"].course == "Computer Science"
    assert loaded_students["STU001"].marks["Mathematics"] == 85


def test_add_student(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student = create_student()

    repository.add_student(student)

    loaded_student = repository.get_student("STU001")

    assert loaded_student is not None
    assert loaded_student.student_id == "STU001"


def test_get_all_students(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student1 = create_student("STU001")
    student2 = create_student("STU002")

    repository.save_students({
        student1.student_id: student1,
        student2.student_id: student2,
    })

    students = repository.get_all_students()

    assert len(students) == 2
    assert "STU001" in students
    assert "STU002" in students


def test_update_student(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student = create_student()

    repository.add_student(student)

    updated_student = Student(
        student_id="STU001",
        name="Rahul Sharma",
        age=21,
        email="rahul.sharma@example.com",
        course="Data Science",
        marks={
            "Mathematics": 90,
            "Science": 88,
            "English": 95,
        },
    )

    result = repository.update_student(updated_student)

    assert result is True

    loaded_student = repository.get_student("STU001")

    assert loaded_student is not None
    assert loaded_student.name == "Rahul Sharma"
    assert loaded_student.age == 21
    assert loaded_student.course == "Data Science"
    assert loaded_student.marks["Mathematics"] == 90


def test_update_nonexistent_student(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student = create_student()

    result = repository.update_student(student)

    assert result is False


def test_delete_student(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    student = create_student()

    repository.add_student(student)

    result = repository.delete_student("STU001")

    assert result is True
    assert repository.get_student("STU001") is None


def test_delete_nonexistent_student(tmp_path):
    repository = StudentRepository(tmp_path / "students.json")

    result = repository.delete_student("STU999")

    assert result is False


def test_invalid_json_returns_empty_dictionary(tmp_path):
    file_path = tmp_path / "students.json"

    file_path.write_text(
        "{ invalid json }",
        encoding="utf-8",
    )

    repository = StudentRepository(file_path)

    students = repository.load_students()

    assert students == {}