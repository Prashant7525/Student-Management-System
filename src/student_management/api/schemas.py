from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    """Request model for creating a student."""

    student_id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=1, le=100)
    email: str = Field(..., min_length=1)
    course: str = Field(..., min_length=1)


class StudentUpdate(BaseModel):
    """Request model for updating a student."""

    name: str = Field(..., min_length=1)
    age: int = Field(..., ge=1, le=100)
    email: str = Field(..., min_length=1)
    course: str = Field(..., min_length=1)


class MarkCreate(BaseModel):
    """Request model for adding or updating a mark."""

    subject: str = Field(..., min_length=1)
    mark: float = Field(..., ge=0, le=100)


class StudentResponse(BaseModel):
    """Response model representing a student."""

    student_id: str
    name: str
    age: int
    email: str
    course: str
    marks: dict[str, float]


class ResultResponse(BaseModel):
    """Response model representing a student's academic result."""

    student_id: str
    name: str
    course: str
    marks: dict[str, float]
    total: float
    average: float
    grade: str