from student_management.services.student_service import StudentService


class StudentMenu:
    """Handle the command-line interface for the Student Management System."""

    def __init__(self, service: StudentService):
        self.service = service

    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("           STUDENT MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. View Student")
        print("5. Update Student")
        print("6. Delete Student")
        print("7. Add / Update Marks")
        print("8. Remove Marks")
        print("9. View Result")
        print("0. Exit")
        print("=" * 50)

    def run(self) -> None:
        """Start the application menu."""
        while True:
            self.display_menu()

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_all_students()
            elif choice == "3":
                self.search_students()
            elif choice == "4":
                self.view_student()
            elif choice == "5":
                self.update_student()
            elif choice == "6":
                self.delete_student()
            elif choice == "7":
                self.add_marks()
            elif choice == "8":
                self.remove_marks()
            elif choice == "9":
                self.view_result()
            elif choice == "0":
                print("\nThank you for using Student Management System.")
                break
            else:
                print("\n❌ Invalid choice. Please select an option from 0-9.")

    def add_student(self) -> None:
        """Collect information and add a new student."""
        print("\n--- Add Student ---")

        student_id = input("Student ID: ")
        name = input("Name: ")
        age_input = input("Age: ")
        email = input("Email: ")
        course = input("Course: ")

        try:
            age = int(age_input)
        except ValueError:
            print("\n❌ Age must be a valid number.")
            return
        
        try:
            student = self.service.add_student(
                student_id=student_id,
                name=name,
                age=age,
                email=email,
                course=course,
            )
        
            print(f"\n✓ Student '{student.student_id}' added successfully!")
        
        except ValueError as error:
            print(f"\n❌ {error}")

    def view_all_students(self) -> None:
        """Display all students."""
        print("\n--- All Students ---")

        students = self.service.get_all_students()

        if not students:
            print("No students found.")
            return

        print(
            f"\n{'ID':<12}"
            f"{'Name':<25}"
            f"{'Age':<8}"
            f"{'Course':<25}"
        )
        print("-" * 70)

        for student in students.values():
            print(
                f"{student.student_id:<12}"
                f"{student.name:<25}"
                f"{student.age:<8}"
                f"{student.course:<25}"
            )

    def search_students(self) -> None:
        """Search students."""
        print("\n--- Search Student ---")

        query = input("Enter search term: ")

        results = self.service.search_students(query)

        if not results:
            print("\nNo matching students found.")
            return

        print(f"\nFound {len(results)} student(s):\n")

        for student in results:
            print(f"ID     : {student.student_id}")
            print(f"Name   : {student.name}")
            print(f"Age    : {student.age}")
            print(f"Email  : {student.email}")
            print(f"Course : {student.course}")
            print("-" * 40)

    def view_student(self) -> None:
        """Display a single student."""
        print("\n--- View Student ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if student is None:
            print(f"\n❌ Student '{student_id.strip()}' not found.")
            return

        self.display_student_details(student)

    def display_student_details(self, student) -> None:
        """Display detailed information about a student."""
        print("\n" + "-" * 45)
        print("Student Details")
        print("-" * 45)
        print(f"ID     : {student.student_id}")
        print(f"Name   : {student.name}")
        print(f"Age    : {student.age}")
        print(f"Email  : {student.email}")
        print(f"Course : {student.course}")

        print("\nMarks:")

        if student.marks:
            for subject, mark in student.marks.items():
                print(f"  {subject:<20} {mark:.2f}")
        else:
            print("  No marks recorded.")

        print("-" * 45)

    def update_student(self) -> None:
        """Update an existing student's information."""
        print("\n--- Update Student ---")

        student_id = input("Student ID: ")

        existing_student = self.service.get_student(student_id)

        if existing_student is None:
            print(f"\n❌ Student '{student_id.strip()}' not found.")
            return

        print("\nPress Enter to keep the current value.")

        name_input = input(f"Name [{existing_student.name}]: ")
        age_input = input(f"Age [{existing_student.age}]: ")
        email_input = input(f"Email [{existing_student.email}]: ")
        course_input = input(f"Course [{existing_student.course}]: ")

        name = name_input.strip() or existing_student.name
        email = email_input.strip() or existing_student.email
        course = course_input.strip() or existing_student.course

        try:
            age = (
                int(age_input)
                if age_input.strip()
                else existing_student.age
            )

            student = self.service.update_student(
                student_id=student_id,
                name=name,
                age=age,
                email=email,
                course=course,
            )

            print(f"\n✓ Student '{student.student_id}' updated successfully!")

        except ValueError as error:
            print(f"\n❌ {error}")

    def delete_student(self) -> None:
        """Delete a student."""
        print("\n--- Delete Student ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if student is None:
            print(f"\n❌ Student '{student_id.strip()}' not found.")
            return

        print(f"\nStudent: {student.name}")
        confirmation = input("Are you sure you want to delete this student? (y/n): ")

        if confirmation.strip().lower() != "y":
            print("\nDeletion cancelled.")
            return

        try:
            deleted = self.service.delete_student(student_id)

            if deleted:
                print(f"\n✓ Student '{student_id.strip()}' deleted successfully.")
            else:
                print("\n❌ Student could not be deleted.")

        except ValueError as error:
            print(f"\n❌ {error}")

    def add_marks(self) -> None:
        """Add or update marks for a student."""
        print("\n--- Add / Update Marks ---")

        student_id = input("Student ID: ")
        subject = input("Subject: ")
        mark_input = input("Mark (0-100): ")

        try:
            mark = float(mark_input)

            student = self.service.add_marks(
                student_id=student_id,
                subject=subject,
                mark=mark,
            )

            print(
                f"\n✓ Mark for '{subject.strip()}' saved successfully "
                f"for {student.name}."
            )

        except ValueError as error:
            print(f"\n❌ {error}")

    def remove_marks(self) -> None:
        """Remove a subject mark."""
        print("\n--- Remove Marks ---")

        student_id = input("Student ID: ")
        subject = input("Subject: ")

        try:
            student = self.service.remove_marks(
                student_id=student_id,
                subject=subject,
            )

            print(
                f"\n✓ Mark for '{subject.strip()}' removed "
                f"from {student.name}."
            )

        except ValueError as error:
            print(f"\n❌ {error}")

    def view_result(self) -> None:
        """Display a student's academic result."""
        print("\n--- View Result ---")

        student_id = input("Student ID: ")

        student = self.service.get_student(student_id)

        if student is None:
            print(f"\n❌ Student '{student_id.strip()}' not found.")
            return

        print("\n" + "=" * 45)
        print("               STUDENT RESULT")
        print("=" * 45)

        print(f"ID     : {student.student_id}")
        print(f"Name   : {student.name}")
        print(f"Course : {student.course}")

        print("\nMarks:")

        if student.marks:
            for subject, mark in student.marks.items():
                print(f"  {subject:<20} {mark:>6.2f}")

            print("\n" + "-" * 45)
            print(f"Total   : {student.total_marks():.2f}")
            print(f"Average : {student.average_marks():.2f}")
            print(f"Grade   : {student.grade()}")
        else:
            print("  No marks recorded.")

        print("=" * 45)