import pytest
from fastapi.testclient import TestClient

from student_management.api.app import app
from student_management.api import app as app_module
from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


@pytest.fixture
def client(tmp_path, monkeypatch):
    """Create a test client with an isolated JSON database."""

    test_file = tmp_path / "students.json"
    repository = StudentRepository(test_file)
    service = StudentService(repository)

    monkeypatch.setattr(app_module, "repository", repository)
    monkeypatch.setattr(app_module, "service", service)

    return TestClient(app)


def test_root_endpoint(client):
    """Test the API root endpoint."""
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Student Management System API",
        "version": "1.0.0",
        "docs": "/docs",
    }


def test_get_all_students_empty(client):
    """Test retrieving students when no students exist."""
    response = client.get("/students")

    assert response.status_code == 200
    assert response.json() == []


def test_create_student(client):
    """Test creating a new student."""
    student_data = {
        "student_id": "STU100",
        "name": "Test Student",
        "age": 20,
        "email": "test@example.com",
        "course": "Computer Science",
    }

    response = client.post("/students", json=student_data)

    assert response.status_code == 201

    data = response.json()

    assert data["student_id"] == "STU100"
    assert data["name"] == "Test Student"
    assert data["age"] == 20
    assert data["email"] == "test@example.com"
    assert data["course"] == "Computer Science"
    assert data["marks"] == {}


def test_get_student(client):
    """Test retrieving a specific student."""
    student_data = {
        "student_id": "STU101",
        "name": "Test Student",
        "age": 21,
        "email": "student101@example.com",
        "course": "Data Science",
    }

    client.post("/students", json=student_data)

    response = client.get("/students/STU101")

    assert response.status_code == 200
    assert response.json()["student_id"] == "STU101"
    assert response.json()["name"] == "Test Student"


def test_get_nonexistent_student(client):
    """Test retrieving a student that does not exist."""
    response = client.get("/students/STU999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student 'STU999' not found."


def test_update_student(client):
    """Test updating an existing student."""
    student_data = {
        "student_id": "STU102",
        "name": "Original Name",
        "age": 20,
        "email": "original@example.com",
        "course": "Computer Science",
    }

    client.post("/students", json=student_data)

    updated_data = {
        "name": "Updated Name",
        "age": 22,
        "email": "updated@example.com",
        "course": "Artificial Intelligence",
    }

    response = client.put("/students/STU102", json=updated_data)

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == "STU102"
    assert data["name"] == "Updated Name"
    assert data["age"] == 22
    assert data["email"] == "updated@example.com"
    assert data["course"] == "Artificial Intelligence"


def test_delete_student(client):
    """Test deleting an existing student."""
    student_data = {
        "student_id": "STU103",
        "name": "Delete Student",
        "age": 20,
        "email": "delete@example.com",
        "course": "Mathematics",
    }

    client.post("/students", json=student_data)

    response = client.delete("/students/STU103")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Student 'STU103' deleted successfully."
    }

    get_response = client.get("/students/STU103")

    assert get_response.status_code == 404


def test_search_students(client):
    """Test searching students."""
    students = [
        {
            "student_id": "STU104",
            "name": "Alice Johnson",
            "age": 20,
            "email": "alice@example.com",
            "course": "Computer Science",
        },
        {
            "student_id": "STU105",
            "name": "Bob Smith",
            "age": 21,
            "email": "bob@example.com",
            "course": "Data Science",
        },
    ]

    for student in students:
        client.post("/students", json=student)

    response = client.get("/students/search?q=alice")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["student_id"] == "STU104"


def test_add_mark(client):
    """Test adding a mark to a student."""
    student_data = {
        "student_id": "STU106",
        "name": "Marks Student",
        "age": 20,
        "email": "marks@example.com",
        "course": "Computer Science",
    }

    client.post("/students", json=student_data)

    mark_data = {
        "subject": "Python",
        "mark": 92,
    }

    response = client.post(
        "/students/STU106/marks",
        json=mark_data,
    )

    assert response.status_code == 200
    assert response.json()["marks"] == {"Python": 92.0}


def test_remove_mark(client):
    """Test removing a student's mark."""
    student_data = {
        "student_id": "STU107",
        "name": "Remove Mark Student",
        "age": 20,
        "email": "remove@example.com",
        "course": "Computer Science",
    }

    client.post("/students", json=student_data)

    client.post(
        "/students/STU107/marks",
        json={
            "subject": "Python",
            "mark": 90,
        },
    )

    response = client.delete(
        "/students/STU107/marks/Python",
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Mark for 'Python' removed from student 'STU107'."
    }


def test_get_student_result(client):
    """Test retrieving a student's academic result."""
    student_data = {
        "student_id": "STU108",
        "name": "Result Student",
        "age": 20,
        "email": "result@example.com",
        "course": "Computer Science",
    }

    client.post("/students", json=student_data)

    client.post(
        "/students/STU108/marks",
        json={
            "subject": "Python",
            "mark": 90,
        },
    )

    client.post(
        "/students/STU108/marks",
        json={
            "subject": "Mathematics",
            "mark": 80,
        },
    )

    response = client.get("/students/STU108/result")

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == "STU108"
    assert data["marks"] == {
        "Python": 90.0,
        "Mathematics": 80.0,
    }
    assert data["total"] == 170.0
    assert data["average"] == 85.0
    assert data["grade"] == "A"


def test_create_duplicate_student(client):
    """Test that duplicate student IDs are rejected."""
    student_data = {
        "student_id": "STU109",
        "name": "Duplicate Student",
        "age": 20,
        "email": "duplicate@example.com",
        "course": "Computer Science",
    }

    first_response = client.post(
        "/students",
        json=student_data,
    )

    second_response = client.post(
        "/students",
        json=student_data,
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 400
    assert (
        second_response.json()["detail"]
        == "Student with ID 'STU109' already exists."
    )


def test_invalid_student_data(client):
    """Test API validation for invalid student data."""
    student_data = {
        "student_id": "INVALID",
        "name": "",
        "age": 150,
        "email": "invalid-email",
        "course": "",
    }

    response = client.post(
        "/students",
        json=student_data,
    )

    assert response.status_code == 422


def test_invalid_mark(client):
    """Test API validation for an invalid mark."""
    student_data = {
        "student_id": "STU110",
        "name": "Invalid Mark Student",
        "age": 20,
        "email": "invalidmark@example.com",
        "course": "Computer Science",
    }

    client.post("/students", json=student_data)

    response = client.post(
        "/students/STU110/marks",
        json={
            "subject": "Python",
            "mark": 150,
        },
    )

    assert response.status_code == 422