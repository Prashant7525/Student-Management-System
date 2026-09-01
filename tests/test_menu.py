from student_management.cli.menu import StudentMenu
from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


def create_menu(tmp_path):
    """Create a StudentMenu with temporary storage."""
    repository = StudentRepository(tmp_path / "students.json")
    service = StudentService(repository)

    return StudentMenu(service)


def test_display_menu(capsys, tmp_path):
    menu = create_menu(tmp_path)

    menu.display_menu()

    captured = capsys.readouterr()

    assert "STUDENT MANAGEMENT SYSTEM" in captured.out
    assert "1. Add Student" in captured.out
    assert "2. View All Students" in captured.out
    assert "9. View Result" in captured.out
    assert "0. Exit" in captured.out


def test_add_student(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    inputs = iter([
        "STU001",
        "Rahul Kumar",
        "20",
        "rahul@example.com",
        "Computer Science",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.add_student()

    captured = capsys.readouterr()

    assert "added successfully" in captured.out

    student = menu.service.get_student("STU001")

    assert student is not None
    assert student.name == "Rahul Kumar"


def test_add_student_invalid_age(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    inputs = iter([
        "STU001",
        "Rahul Kumar",
        "abc",
        "rahul@example.com",
        "Computer Science",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.add_student()

    captured = capsys.readouterr()

    assert "Age must be a valid number." in captured.out


def test_view_student_not_found(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "STU999",
    )

    menu.view_student()

    captured = capsys.readouterr()

    assert "not found" in captured.out


def test_view_student(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "STU001",
    )

    menu.view_student()

    captured = capsys.readouterr()

    assert "Rahul Kumar" in captured.out
    assert "Computer Science" in captured.out
    assert "STU001" in captured.out


def test_search_students(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "rahul",
    )

    menu.search_students()

    captured = capsys.readouterr()

    assert "Rahul Kumar" in captured.out
    assert "STU001" in captured.out


def test_search_students_no_results(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "unknown",
    )

    menu.search_students()

    captured = capsys.readouterr()

    assert "No matching students found" in captured.out


def test_delete_student_cancelled(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    inputs = iter([
        "STU001",
        "n",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.delete_student()

    captured = capsys.readouterr()

    assert "Deletion cancelled" in captured.out

    assert menu.service.get_student("STU001") is not None


def test_delete_student_confirmed(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    inputs = iter([
        "STU001",
        "y",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.delete_student()

    captured = capsys.readouterr()

    assert "deleted successfully" in captured.out

    assert menu.service.get_student("STU001") is None


def test_add_marks(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    inputs = iter([
        "STU001",
        "Mathematics",
        "85",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.add_marks()

    captured = capsys.readouterr()

    assert "saved successfully" in captured.out

    student = menu.service.get_student("STU001")

    assert student is not None
    assert student.marks["Mathematics"] == 85


def test_remove_marks(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    menu.service.add_marks(
        student_id="STU001",
        subject="Mathematics",
        mark=85,
    )

    inputs = iter([
        "STU001",
        "Mathematics",
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    menu.remove_marks()

    captured = capsys.readouterr()

    assert "removed" in captured.out

    student = menu.service.get_student("STU001")

    assert student is not None
    assert "Mathematics" not in student.marks


def test_view_result(capsys, monkeypatch, tmp_path):
    menu = create_menu(tmp_path)

    menu.service.add_student(
        student_id="STU001",
        name="Rahul Kumar",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    menu.service.add_marks("STU001", "Mathematics", 85)
    menu.service.add_marks("STU001", "Science", 78)
    menu.service.add_marks("STU001", "English", 92)

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "STU001",
    )

    menu.view_result()

    captured = capsys.readouterr()

    assert "STUDENT RESULT" in captured.out
    assert "Rahul Kumar" in captured.out
    assert "255.00" in captured.out
    assert "85.00" in captured.out
    assert "Grade   : A" in captured.out