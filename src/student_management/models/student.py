from dataclasses import dataclass, field


@dataclass
class Student:
    """Represent a student and their academic information."""

    student_id: str
    name: str
    age: int
    email: str
    course: str
    marks: dict[str, float] = field(default_factory=dict)

    def total_marks(self) -> float:
        """Return the total marks obtained by the student."""
        return sum(self.marks.values())

    def average_marks(self) -> float:
        """Return the average marks obtained by the student."""
        if not self.marks:
            return 0.0

        return self.total_marks() / len(self.marks)

    def grade(self) -> str:
        """Return the student's grade based on average marks."""
        average = self.average_marks()

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"