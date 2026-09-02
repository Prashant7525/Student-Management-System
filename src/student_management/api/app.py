from fastapi import FastAPI, HTTPException, Query, status

from student_management.api.schemas import (
    MarkCreate,
    ResultResponse,
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)
from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


app = FastAPI(
    title="Student Management System API",
    description="REST API for managing students and academic records.",
    version="1.0.0",
)


repository = StudentRepository()
service = StudentService(repository)


@app.get("/")
def root() -> dict[str, str]:
    """Return basic API information."""
    return {
        "message": "Student Management System API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/students", response_model=list[StudentResponse])
def get_all_students() -> list[StudentResponse]:
    """Return all students."""
    students = service.get_all_students()

    return [
        StudentResponse(
            student_id=student.student_id,
            name=student.name,
            age=student.age,
            email=student.email,
            course=student.course,
            marks=student.marks,
        )
        for student in students.values()
    ]


@app.get("/students/search", response_model=list[StudentResponse])
def search_students(
    q: str = Query(..., min_length=1),
) -> list[StudentResponse]:
    """Search students by ID, name, email, or course."""
    students = service.search_students(q)

    return [
        StudentResponse(
            student_id=student.student_id,
            name=student.name,
            age=student.age,
            email=student.email,
            course=student.course,
            marks=student.marks,
        )
        for student in students
    ]


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: str) -> StudentResponse:
    """Return a student by ID."""
    student = service.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student '{student_id.strip()}' not found.",
        )

    return StudentResponse(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course,
        marks=student.marks,
    )


@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student(student_data: StudentCreate) -> StudentResponse:
    """Create a new student."""
    try:
        student = service.add_student(
            student_id=student_data.student_id,
            name=student_data.name,
            age=student_data.age,
            email=student_data.email,
            course=student_data.course,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return StudentResponse(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course,
        marks=student.marks,
    )


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: str,
    student_data: StudentUpdate,
) -> StudentResponse:
    """Update an existing student."""
    try:
        student = service.update_student(
            student_id=student_id,
            name=student_data.name,
            age=student_data.age,
            email=student_data.email,
            course=student_data.course,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return StudentResponse(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course,
        marks=student.marks,
    )


@app.delete("/students/{student_id}")
def delete_student(student_id: str) -> dict[str, str]:
    """Delete a student."""
    student = service.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student '{student_id.strip()}' not found.",
        )

    service.delete_student(student_id)

    return {
        "message": f"Student '{student_id.strip()}' deleted successfully."
    }


@app.post(
    "/students/{student_id}/marks",
    response_model=StudentResponse,
)
def add_mark(
    student_id: str,
    mark_data: MarkCreate,
) -> StudentResponse:
    """Add or update a student's mark."""
    try:
        student = service.add_marks(
            student_id=student_id,
            subject=mark_data.subject,
            mark=mark_data.mark,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return StudentResponse(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course,
        marks=student.marks,
    )


@app.delete("/students/{student_id}/marks/{subject}")
def remove_mark(
    student_id: str,
    subject: str,
) -> dict[str, str]:
    """Remove a student's mark for a subject."""
    try:
        service.remove_marks(
            student_id=student_id,
            subject=subject,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error

    return {
        "message": (
            f"Mark for '{subject.strip()}' removed "
            f"from student '{student_id.strip()}'."
        )
    }


@app.get(
    "/students/{student_id}/result",
    response_model=ResultResponse,
)
def get_student_result(student_id: str) -> ResultResponse:
    """Return a student's academic result."""
    student = service.get_student(student_id)

    if student is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student '{student_id.strip()}' not found.",
        )

    return ResultResponse(
        student_id=student.student_id,
        name=student.name,
        course=student.course,
        marks=student.marks,
        total=student.total_marks(),
        average=student.average_marks(),
        grade=student.grade(),
    )