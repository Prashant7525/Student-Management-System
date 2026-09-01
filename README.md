# Student Management System

A beginner-to-intermediate Python project for managing student records, academic information, marks, and results through a command-line interface.

The project is designed using a clean layered architecture with validation, JSON-based persistence, automated testing, and modular code organization.

---

## 📌 Project Status

- ✅ Core functionality completed
- ✅ CLI completed
- ✅ JSON persistence implemented
- ✅ Automated tests implemented
- 🚧 Documentation and project polish in progress

---

## ✨ Features

### Student Management

- Add new students
- View all students
- Search students
- View individual student details
- Update student information
- Delete students

### Academic Management

- Add marks for subjects
- Update existing marks
- Remove subject marks
- Calculate total marks
- Calculate average marks
- Automatically calculate grades

### Data Management

- Persistent JSON storage
- Automatic creation of the data directory
- Load student records when the application starts
- Preserve marks when updating student information

### Validation

- Student ID validation
- Student name validation
- Age validation
- Email validation
- Course validation
- Marks validation

### Testing

- Unit tests
- Service-layer tests
- Repository tests
- CLI tests
- Integration tests
- Persistence tests

---

## 🛠️ Technologies Used

- Python 3
- JSON
- pytest
- Git
- GitHub
- Visual Studio Code

---

## 🏗️ Architecture

The project follows a layered architecture:

```text
┌──────────────────────────────┐
│       Command-Line UI        │
│            (CLI)             │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       Service Layer          │
│     Business Operations      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│      Repository Layer        │
│      Data Persistence        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│        JSON Storage          │
│     data/students.json       │
└──────────────────────────────┘
```

### Layer Responsibilities

**CLI**

Handles user interaction and displays information.

**Service Layer**

Contains business logic and coordinates operations.

**Repository Layer**

Handles reading and writing student data.

**Model Layer**

Represents the student and provides academic calculations.

**Utils**

Contains reusable validation functions.

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── data/
│   └── students.json
│
├── docs/
│
├── src/
│   └── student_management/
│       │
│       ├── cli/
│       │   ├── __init__.py
│       │   └── menu.py
│       │
│       ├── models/
│       │   ├── __init__.py
│       │   └── student.py
│       │
│       ├── repositories/
│       │   ├── __init__.py
│       │   └── student_repository.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   └── student_service.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   └── validators.py
│       │
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   ├── test_integration.py
│   ├── test_menu.py
│   ├── test_repository.py
│   ├── test_student.py
│   ├── test_student_service.py
│   └── test_validators.py
│
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## ⚙️ Requirements

Make sure the following are installed:

- Python 3.10 or newer
- pip
- Git

The project was developed and tested with Python 3.14.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate into the project

```bash
cd Student-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Application

The project currently uses a `src` layout.

### Windows PowerShell

Set the source directory for the current terminal session:

```powershell
$env:PYTHONPATH = "src"
```

Then run:

```powershell
python -m student_management.main
```

The main menu provides:

```text
==================================================
           STUDENT MANAGEMENT SYSTEM
==================================================
1. Add Student
2. View All Students
3. Search Student
4. View Student
5. Update Student
6. Delete Student
7. Add / Update Marks
8. Remove Marks
9. View Result
0. Exit
==================================================
```

---

## 🧪 Running Tests

Activate the virtual environment and run:

```bash
pytest
```

Current test suite:

```text
61 passed
```

The tests cover:

- Student model
- Validators
- Repository
- Service layer
- CLI
- Integration
- JSON persistence

---

## 📋 Validation Rules

### Student ID

A valid student ID:

- Starts with `STU`
- Is followed by one or more digits
- Is case-insensitive

Examples:

```text
STU001
STU123
stu456
```

### Name

Names:

- Cannot be empty
- Can contain letters and spaces

Example:

```text
Rahul Kumar
```

### Age

Age must be between:

```text
1 - 100
```

### Email

A basic email format is required.

Example:

```text
rahul@example.com
```

### Course

The course name cannot be empty.

### Marks

Marks must be between:

```text
0 - 100
```

---

## 🎓 Grading System

The system calculates the grade using the student's average marks.

| Average | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

---

## 💾 Data Persistence

Student records are stored in:

```text
data/students.json
```

Example:

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

The repository layer automatically loads existing records and saves changes to the JSON file.

---

## 🔍 Example Workflow

A typical workflow:

```text
Start Application
       ↓
Add Student
       ↓
Add Subject Marks
       ↓
View Student
       ↓
View Result
       ↓
Calculate Total
       ↓
Calculate Average
       ↓
Calculate Grade
```

Example result:

```text
=============================================
               STUDENT RESULT
=============================================
ID     : STU001
Name   : Rahul Kumar
Course : Computer Science

Marks:
  Python                90.00

---------------------------------------------
Total   : 90.00
Average : 90.00
Grade   : A+
=============================================
```

---

## 🧪 Testing Strategy

The project uses pytest for automated testing.

Testing is organized into multiple layers:

```text
Unit Tests
    │
    ├── Student Model
    ├── Validators
    │
    ▼
Service Tests
    │
    ▼
Repository Tests
    │
    ▼
CLI Tests
    │
    ▼
Integration Tests
    │
    ▼
Persistence Tests
```

This helps verify both individual components and the complete application workflow.

---

## 🔐 Error Handling

The application handles invalid user input without terminating unexpectedly.

Examples include:

- Invalid student ID
- Invalid name
- Invalid age
- Invalid email
- Invalid course
- Invalid marks
- Duplicate student ID
- Student not found
- Subject not found

User-friendly error messages are displayed through the CLI.

---

## 📈 Future Improvements

Possible future versions may include:

- SQLite database support
- Advanced search and filtering
- Sorting students
- Attendance management
- More detailed academic reports
- Export results to CSV/PDF
- GUI application
- REST API
- Web-based interface
- User authentication
- Admin dashboard
- Database migrations
- Logging
- Configuration management

---

## 🎯 Learning Objectives

This project demonstrates practical understanding of:

- Python programming
- Object-oriented programming
- Dataclasses
- Modular architecture
- Separation of concerns
- Input validation
- Exception handling
- File handling
- JSON serialization
- CRUD operations
- Business logic
- Automated testing
- Integration testing
- Git version control
- Project documentation

---

## 👨‍💻 Development Approach

The project was developed incrementally using separate development phases.

```text
Phase 1  → Project Foundation
Phase 2  → Student Model
Phase 3  → Input Validation
Phase 4  → JSON Repository
Phase 5  → Service Layer
Phase 6  → Command-Line Interface
Phase 7  → Integration & Persistence Testing
Phase 8  → Documentation & Project Polish
Phase 9  → GitHub Setup
```

Each major phase was tested and committed separately using Git.

---

## 📜 License

This project is licensed under the MIT License.
