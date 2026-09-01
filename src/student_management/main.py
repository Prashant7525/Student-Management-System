from student_management.cli.menu import StudentMenu
from student_management.repositories.student_repository import StudentRepository
from student_management.services.student_service import StudentService


def main() -> None:
    """Start the Student Management System."""
    repository = StudentRepository()
    service = StudentService(repository)
    menu = StudentMenu(service)

    menu.run()


if __name__ == "__main__":
    main()