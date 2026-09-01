# System Architecture

## Overview

The Student Management System follows a layered architecture designed to keep user interaction, business logic, data access, and data representation separate.

The main flow is:

```text
User
  |
  v
CLI Layer
  |
  v
Service Layer
  |
  v
Repository Layer
  |
  v
JSON Storage
```

The model layer provides the data structure and academic calculation logic used by the service and CLI layers.

---

## Architecture Layers

### 1. CLI Layer

Location:

```text
src/student_management/cli/
```

Main file:

```text
menu.py
```

Responsibilities:

- Display the application menu
- Collect user input
- Display student information
- Display results
- Handle user-facing error messages
- Call service-layer operations

The CLI does not directly manipulate JSON files.

---

### 2. Service Layer

Location:

```text
src/student_management/services/
```

Main file:

```text
student_service.py
```

Responsibilities:

- Implement student management operations
- Validate input
- Enforce business rules
- Prevent duplicate student IDs
- Coordinate repository operations
- Manage student marks
- Provide search functionality

The service layer acts as the main business-logic boundary of the application.

---

### 3. Repository Layer

Location:

```text
src/student_management/repositories/
```

Main file:

```text
student_repository.py
```

Responsibilities:

- Load students from JSON
- Save students to JSON
- Add students
- Retrieve students
- Retrieve all students
- Update students
- Delete students

The repository layer isolates persistence logic from the rest of the application.

---

### 4. Model Layer

Location:

```text
src/student_management/models/
```

Main file:

```text
student.py
```

The `Student` dataclass represents a student record.

It contains:

- Student ID
- Name
- Age
- Email
- Course
- Subject marks

It also provides academic calculations:

- Total marks
- Average marks
- Grade

---

### 5. Utilities Layer

Location:

```text
src/student_management/utils/
```

Main file:

```text
validators.py
```

Responsibilities:

- Validate student IDs
- Validate names
- Validate ages
- Validate email addresses
- Validate courses
- Validate marks

Keeping validation functions separate makes them reusable and easy to test.

---

## Data Flow

### Adding a Student

```text
User
  |
  v
CLI
  |
  v
StudentService
  |
  +-- Validate input
  |
  +-- Check duplicate ID
  |
  v
StudentRepository
  |
  v
students.json
```

### Viewing a Student

```text
User
  |
  v
CLI
  |
  v
StudentService
  |
  v
StudentRepository
  |
  v
students.json
  |
  v
Student object
  |
  v
CLI
```

### Adding Marks

```text
User
  |
  v
CLI
  |
  v
StudentService
  |
  +-- Find student
  +-- Validate mark
  +-- Update marks
        |
        v
StudentRepository
        |
        v
students.json
```

### Viewing a Result

```text
User
  |
  v
CLI
  |
  v
StudentService
  |
  v
Student
  |
  +-- total_marks()
  +-- average_marks()
  +-- grade()
        |
        v
Result displayed by CLI
```

---

## Separation of Concerns

Each component has a specific responsibility.

| Component | Responsibility |
|---|---|
| CLI | User interaction |
| Service | Business logic |
| Repository | Data persistence |
| Model | Student data and calculations |
| Validators | Input validation |

This separation makes the project easier to:

- Understand
- Test
- Maintain
- Debug
- Extend

---

## Persistence Architecture

The application currently uses JSON for persistent storage.

```text
Application
     |
     v
StudentRepository
     |
     v
data/students.json
```

The repository converts between Python `Student` objects and JSON-compatible dictionaries.

Example stored structure:

```json
{
    "STU001": {
        "student_id": "STU001",
        "name": "Rahul Kumar",
        "age": 20,
        "email": "rahul@example.com",
        "course": "Computer Science",
        "marks": {
            "Python": 90.0
        }
    }
}
```

---

## Testing Architecture

Testing is performed at multiple levels.

```text
                    Test Suite
                        |
        +---------------+---------------+
        |               |               |
        v               v               v
     Unit Tests     Service Tests    CLI Tests
        |               |               |
        +---------------+---------------+
                        |
                        v
                Integration Tests
                        |
                        v
                Persistence Tests
```

The project currently contains:

```text
61 tests
61 passed
```

---

## Why This Architecture?

The layered design was chosen to avoid putting all application logic into a single file.

For example:

- The CLI should not know how JSON files are written.
- The repository should not handle user input.
- Validation should not be duplicated throughout the application.
- Business rules should remain independent from the user interface.

This makes future upgrades easier.

For example, the CLI could eventually be replaced with:

```text
             +-- CLI
             |
Service -----+-- GUI
             |
             +-- REST API
```

The same service and repository layers could continue to provide the underlying functionality.

---

## Future Architecture

A future version could replace JSON with SQLite:

```text
CLI / GUI / REST API
         |
         v
   Service Layer
         |
         v
 Repository Layer
         |
         v
   SQLite Database
```

This would allow the application to handle larger datasets and more advanced database operations.

---

## Conclusion

The current architecture provides a clean foundation for the Student Management System while keeping the project simple enough to understand.

The separation between presentation, business logic, persistence, models, and validation allows the application to grow without requiring a complete rewrite.
