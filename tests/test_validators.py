from student_management.utils.validators import (
    validate_age,
    validate_course,
    validate_email,
    validate_mark,
    validate_name,
    validate_student_id,
)


def test_valid_student_id():
    assert validate_student_id("STU001") is True


def test_student_id_is_case_insensitive():
    assert validate_student_id("stu001") is True


def test_invalid_student_id():
    assert validate_student_id("STUDENT001") is False
    assert validate_student_id("STU") is False
    assert validate_student_id("") is False


def test_valid_name():
    assert validate_name("Rahul Kumar") is True


def test_invalid_name():
    assert validate_name("") is False
    assert validate_name("12345") is False
    assert validate_name("Rahul123") is False


def test_valid_age():
    assert validate_age(20) is True
    assert validate_age(1) is True
    assert validate_age(100) is True


def test_invalid_age():
    assert validate_age(0) is False
    assert validate_age(-5) is False
    assert validate_age(101) is False
    assert validate_age(True) is False


def test_valid_email():
    assert validate_email("rahul@example.com") is True


def test_invalid_email():
    assert validate_email("rahul") is False
    assert validate_email("rahul@") is False
    assert validate_email("@example.com") is False
    assert validate_email("") is False


def test_valid_course():
    assert validate_course("Computer Science") is True


def test_invalid_course():
    assert validate_course("") is False
    assert validate_course("   ") is False


def test_valid_mark():
    assert validate_mark(0) is True
    assert validate_mark(50) is True
    assert validate_mark(100) is True
    assert validate_mark(85.5) is True


def test_invalid_mark():
    assert validate_mark(-1) is False
    assert validate_mark(101) is False
    assert validate_mark(True) is False