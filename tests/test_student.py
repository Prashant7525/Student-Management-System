from student_management.models.student import Student


def test_student_creation():
    student = Student(
        student_id="STU001",
        name="Rahul",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    assert student.student_id == "STU001"
    assert student.name == "Rahul"
    assert student.age == 20
    assert student.email == "rahul@example.com"
    assert student.course == "Computer Science"


def test_total_marks():
    student = Student(
        student_id="STU001",
        name="Rahul",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
        marks={
            "Mathematics": 85,
            "Science": 78,
            "English": 92,
        },
    )

    assert student.total_marks() == 255


def test_average_marks():
    student = Student(
        student_id="STU001",
        name="Rahul",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
        marks={
            "Mathematics": 85,
            "Science": 78,
            "English": 92,
        },
    )

    assert student.average_marks() == 85.0


def test_grade():
    student = Student(
        student_id="STU001",
        name="Rahul",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
        marks={
            "Mathematics": 85,
            "Science": 78,
            "English": 92,
        },
    )

    assert student.grade() == "A"


def test_empty_marks():
    student = Student(
        student_id="STU001",
        name="Rahul",
        age=20,
        email="rahul@example.com",
        course="Computer Science",
    )

    assert student.total_marks() == 0
    assert student.average_marks() == 0.0
    assert student.grade() == "F"