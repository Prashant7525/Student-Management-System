from student_management.models.student import Student
from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


def create_service(tmp_path):
    """Create a service using a temporary JSON file."""
    file_path = tmp_path / "students.json"

    repository = StudentRepository(file_path)
    return StudentService(repository)


def test_student_lifecycle_with_persistence(tmp_path):
    """Test adding, updating, and deleting a student with persistence."""

    service = create_service(tmp_path)

    # Add a student
    student = service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    assert student.student_id == "STU001"

    # Add marks
    service.add_marks("STU001", "Python", 90)
    service.add_marks("STU001", "Database", 80)

    # Create a new service using the same storage file
    file_path = tmp_path / "students.json"
    repository = StudentRepository(file_path)
    new_service = StudentService(repository)

    # Verify data survived reload
    loaded_student = new_service.get_student("STU001")

    assert loaded_student is not None
    assert loaded_student.name == "Rahul Kumar"
    assert loaded_student.age == 20
    assert loaded_student.email == "rahul@example.com"
    assert loaded_student.course == "Computer Science"

    assert loaded_student.marks == {
        "Python": 90,
        "Database": 80,
    }

    # Verify result calculations after reload
    assert loaded_student.total_marks() == 170
    assert loaded_student.average_marks() == 85
    assert loaded_student.grade() == "A"

    # Update student information
    updated_student = new_service.update_student(
        student_id="STU001",
        name="Rahul Sharma",
        age=21,
        email="rahul.sharma@example.com",
        course="Data Science",
    )

    assert updated_student.name == "Rahul Sharma"
    assert updated_student.age == 21
    assert updated_student.course == "Data Science"

    # Marks should be preserved during student update
    assert updated_student.marks == {
        "Python": 90,
        "Database": 80,
    }

    # Reload again and verify update was persisted
    repository = StudentRepository(file_path)
    final_service = StudentService(repository)

    final_student = final_service.get_student("STU001")

    assert final_student is not None
    assert final_student.name == "Rahul Sharma"
    assert final_student.age == 21
    assert final_student.email == "rahul.sharma@example.com"
    assert final_student.course == "Data Science"

    assert final_student.marks == {
        "Python": 90,
        "Database": 80,
    }

    # Delete the student
    deleted = final_service.delete_student("STU001")

    assert deleted is True

    # Verify deletion was persisted
    repository = StudentRepository(file_path)
    service_after_delete = StudentService(repository)

    assert service_after_delete.get_student("STU001") is None


def test_multiple_students_persist_correctly(tmp_path):
    """Test that multiple students are stored and loaded correctly."""

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

    service.add_student(
        student_id="STU003",
        name="Amit Verma",
        age=19,
        email="amit@example.com",
        course="Information Technology",
    )

    # Reload from storage
    file_path = tmp_path / "students.json"
    repository = StudentRepository(file_path)
    new_service = StudentService(repository)

    students = new_service.get_all_students()

    assert len(students) == 3
    assert "STU001" in students
    assert "STU002" in students
    assert "STU003" in students

    assert students["STU001"].name == "Rahul Kumar"
    assert students["STU002"].name == "Priya Sharma"
    assert students["STU003"].name == "Amit Verma"


def test_marks_persist_after_reload(tmp_path):
    """Test that adding and removing marks persists correctly."""

    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Neha Singh",
        age=20,
        email="neha@example.com",
        course="Computer Science",
    )

    # Add marks
    service.add_marks("STU001", "Python", 95)
    service.add_marks("STU001", "Math", 85)
    service.add_marks("STU001", "Database", 75)

    # Reload
    file_path = tmp_path / "students.json"
    repository = StudentRepository(file_path)
    new_service = StudentService(repository)

    student = new_service.get_student("STU001")

    assert student is not None
    assert len(student.marks) == 3
    assert student.marks["Python"] == 95
    assert student.marks["Math"] == 85
    assert student.marks["Database"] == 75

    # Remove one mark
    new_service.remove_marks("STU001", "Math")

    # Reload again
    repository = StudentRepository(file_path)
    final_service = StudentService(repository)

    student = final_service.get_student("STU001")

    assert student is not None
    assert len(student.marks) == 2
    assert "Math" not in student.marks
    assert student.marks["Python"] == 95
    assert student.marks["Database"] == 75


def test_search_works_with_persisted_students(tmp_path):
    """Test searching students after data has been reloaded."""

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

    # Create a new service to simulate application restart
    file_path = tmp_path / "students.json"
    repository = StudentRepository(file_path)
    new_service = StudentService(repository)

    results = new_service.search_students("Rahul")

    assert len(results) == 1
    assert results[0].student_id == "STU001"

    results = new_service.search_students("Data Science")

    assert len(results) == 1
    assert results[0].student_id == "STU002"


def test_update_marks_persists_correctly(tmp_path):
    """Test that updating an existing mark is persisted."""

    service = create_service(tmp_path)

    service.add_student(
        student_id="STU001",
        name="Aman Gupta",
        age=20,
        email="aman@example.com",
        course="Software Engineering",
    )

    # Add initial mark
    service.add_marks("STU001", "Python", 70)

    # Update the same subject
    service.add_marks("STU001", "Python", 95)

    # Reload
    file_path = tmp_path / "students.json"
    repository = StudentRepository(file_path)
    new_service = StudentService(repository)

    student = new_service.get_student("STU001")

    assert student is not None
    assert student.marks["Python"] == 95
    assert student.total_marks() == 95
    assert student.average_marks() == 95
    assert student.grade() == "A+"