import re


def validate_student_id(student_id: str) -> bool:
    """Validate a student ID.

    A valid student ID must:
    - Start with STU
    - Be followed by at least one digit
    - Be case-insensitive
    """
    if not isinstance(student_id, str):
        return False

    return bool(re.fullmatch(r"STU\d+", student_id.strip(), re.IGNORECASE))


def validate_name(name: str) -> bool:
    """Validate a student's name.

    The name must:
    - Be a string
    - Not be empty
    - Contain letters and spaces only
    """
    if not isinstance(name, str):
        return False

    name = name.strip()

    if not name:
        return False

    return all(char.isalpha() or char.isspace() for char in name)


def validate_age(age: int) -> bool:
    """Validate a student's age."""
    return isinstance(age, int) and not isinstance(age, bool) and 1 <= age <= 100


def validate_email(email: str) -> bool:
    """Perform basic email validation."""
    if not isinstance(email, str):
        return False

    email = email.strip()

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return bool(re.fullmatch(pattern, email))


def validate_course(course: str) -> bool:
    """Validate a student's course."""
    if not isinstance(course, str):
        return False

    return bool(course.strip())


def validate_mark(mark: float) -> bool:
    """Validate an individual mark.

    Marks must be between 0 and 100.
    """
    if isinstance(mark, bool):
        return False

    return isinstance(mark, (int, float)) and 0 <= mark <= 100