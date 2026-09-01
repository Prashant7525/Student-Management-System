import pytest

from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


def create_service(tmp_path):
    """Create a StudentService with temporary storage."""
    repository = StudentRepository(tmp_path / "students.json")
    return StudentService(repository)


def test_add_student(tmp_path):
    service = create_service(tmp_path)

    student = service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    assert student.student_id == "STU001"
    assert student.name == "Rahul Kumar"

    saved_student = service.get_student("STU001")

    assert saved_student is not None
    assert saved_student.name == "Rahul Kumar"


def test_duplicate_student_id_is_rejected(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    with pytest.raises(ValueError, match="already exists"):
        service.add_student(
            student_id="STU001",
            name="Another Student",
            age=21,
            email="another@example.com",
            course="Data Science",
        )


def test_invalid_student_data_is_rejected(tmp_path):
    service = create_service(tmp_path)

    with pytest.raises(ValueError, match="Invalid student ID"):
        service.add_student(
            student_id="INVALID",
            name="Rahul Kumar",
            age=20,
            email="rahul@example.com",
            course="Computer Science",
        )


def test_get_all_students(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    service.add_student(
        student_id="STU002",
        name="Priya Sharma",
        age=21,
        email="priya@example.com",
        course="Data Science",
    )

    students = service.get_all_students()

    assert len(students) == 2


def test_search_students(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    service.add_student(
        student_id="STU002",
        name="Priya Sharma",
        age=21,
        email="priya@example.com",
        course="Data Science",
    )

    results = service.search_students("rahul")

    assert len(results) == 1
    assert results[0].student_id == "STU001"


def test_search_is_case_insensitive(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    results = service.search_students("RAHUL")

    assert len(results) == 1


def test_search_empty_query_returns_empty_list(tmp_path):
    service = create_service(tmp_path)

    results = service.search_students("")

    assert results == []


def test_update_student(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    updated_student = service.update_student(
        student_id="STU001",
        name="Rahul Sharma",
        age=21,
        email="rahul.sharma@example.com",
        course="Data Science",
    )

    assert updated_student.name == "Rahul Sharma"
    assert updated_student.age == 21
    assert updated_student.course == "Data Science"


def test_update_nonexistent_student(tmp_path):
    service = create_service(tmp_path)

    with pytest.raises(ValueError, match="does not exist"):
        service.update_student(
            student_id="STU999",
            name="Rahul Kumar",
            age=20,
            email="rahul@example.com",
            course="Computer Science",
        )


def test_delete_student(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    result = service.delete_student("STU001")

    assert result is True
    assert service.get_student("STU001") is None


def test_delete_nonexistent_student(tmp_path):
    service = create_service(tmp_path)

    result = service.delete_student("STU999")

    assert result is False


def test_add_marks(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    student = service.add_marks(
        student_id="STU001",
        subject="Mathematics",
        mark=85,
    )

    assert student.marks["Mathematics"] == 85


def test_update_existing_mark(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    service.add_marks("STU001", "Mathematics", 80)
    student = service.add_marks("STU001", "Mathematics", 95)

    assert student.marks["Mathematics"] == 95


def test_invalid_mark_is_rejected(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    with pytest.raises(ValueError, match="between 0 and 100"):
        service.add_marks("STU001", "Mathematics", 105)


def test_add_marks_to_nonexistent_student(tmp_path):
    service = create_service(tmp_path)

    with pytest.raises(ValueError, match="does not exist"):
        service.add_marks("STU999", "Mathematics", 85)


def test_remove_marks(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    service.add_marks("STU001", "Mathematics", 85)

    student = service.remove_marks("STU001", "Mathematics")

    assert "Mathematics" not in student.marks


def test_remove_nonexistent_mark(tmp_path):
    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    with pytest.raises(ValueError, match="does not exist"):
        service.remove_marks("STU001", "Mathematics")