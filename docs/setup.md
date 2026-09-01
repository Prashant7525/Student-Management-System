# Setup Guide

## Overview

This guide explains how to install, configure, test, and run the Student Management System on a Windows computer.

The project uses Python, a virtual environment, pytest, and JSON-based storage.

---

## Requirements

Before setting up the project, install:

- Python 3.10 or newer
- Git
- pip
- Visual Studio Code (recommended)

The project was developed and tested with Python 3.14.

---

## 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone <your-github-repository-url>
```

Navigate into the project directory:

```bash
cd Student-Management-System
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```powershell
python -m venv .venv
```

The virtual environment keeps the project's dependencies separate from the system Python installation.

---

## 3. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

---

## 4. Install Dependencies

Install the required Python packages:

```powershell
python -m pip install -r requirements.txt
```

The current project dependency is:

```text
pytest
```

---

## 5. Verify Python

Check the Python version:

```powershell
python --version
```

Example:

```text
Python 3.14.7
```

---

## 6. Verify pytest

Check that pytest is installed:

```powershell
pytest --version
```

Example:

```text
pytest 9.1.1
```

---

## 7. Run the Test Suite

Run all automated tests:

```powershell
pytest
```

The current test suite contains:

```text
61 tests
61 passed
```

A successful test run should end with output similar to:

```text
61 passed
```

---

## 8. Run the Application

The project currently uses a `src` layout.

In Windows PowerShell, set the `PYTHONPATH` for the current terminal session:

```powershell
$env:PYTHONPATH = "src"
```

Then start the application:

```powershell
python -m student_management.main
```

---

## 9. Application Menu

After starting the application, the following menu is displayed:

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

Enter the number corresponding to the operation you want to perform.

---

## 10. Data Storage

Student records are stored in:

```text
data/students.json
```

The application creates the `data` directory automatically when necessary.

The JSON file stores:

- Student ID
- Name
- Age
- Email
- Course
- Subject marks

---

## 11. Running from a Fresh Terminal

Whenever a new PowerShell terminal is opened, activate the virtual environment again:

```powershell
.venv\Scripts\Activate.ps1
```

Then set the source path:

```powershell
$env:PYTHONPATH = "src"
```

Then run:

```powershell
python -m student_management.main
```

---

## 12. VS Code Setup

Visual Studio Code can be used as the primary development environment.

Open the project:

```powershell
code .
```

Select the Python interpreter:

```text
D:\PROJECTS\Student-Management-System\.venv\Scripts\python.exe
```

This ensures that VS Code uses the project's virtual environment.

---

## 13. Running Tests in VS Code

Open the integrated terminal:

```text
Terminal → New Terminal
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```powershell
pytest
```

VS Code can also discover pytest tests automatically when Python testing is configured.

---

## 14. Troubleshooting

### Python command not found

If this command:

```powershell
python --version
```

does not work, install Python and ensure Python is added to the system PATH.

---

### Virtual environment does not activate

If PowerShell blocks script execution, verify that you are using the correct activation command:

```powershell
.venv\Scripts\Activate.ps1
```

The project can also be activated from Command Prompt using:

```cmd
.venv\Scripts\activate
```

---

### ModuleNotFoundError

If you see:

```text
ModuleNotFoundError: No module named 'student_management'
```

make sure the `src` directory is configured for the current PowerShell session:

```powershell
$env:PYTHONPATH = "src"
```

Then run:

```powershell
python -m student_management.main
```

---

### pytest is not recognized

Use:

```powershell
python -m pip install -r requirements.txt
```

Then verify:

```powershell
pytest --version
```

---

### Tests cannot import project modules

Make sure `pytest.ini` exists in the project root and contains:

```ini
[pytest]
pythonpath = src
testpaths = tests
```

Then run:

```powershell
pytest
```

---

## 15. Recommended Development Workflow

A typical development workflow is:

```text
Activate virtual environment
          ↓
Set PYTHONPATH
          ↓
Make code changes
          ↓
Run pytest
          ↓
Fix failures
          ↓
Run pytest again
          ↓
Review changes
          ↓
Commit with Git
```

---

## 16. Git Workflow

Check the current repository status:

```powershell
git status
```

Review changed files:

```powershell
git diff
```

Stage changes:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Describe your changes"
```

Check the repository again:

```powershell
git status
```

A clean working tree should show:

```text
nothing to commit, working tree clean
```

---

## 17. Clean Environment Test

To verify that the project can be reproduced on another machine:

1. Clone the repository.
2. Create a new virtual environment.
3. Activate the environment.
4. Install dependencies.
5. Run the test suite.
6. Start the application.

Expected result:

```text
pytest
61 passed
```

The application should then start successfully using:

```powershell
$env:PYTHONPATH = "src"
python -m student_management.main
```

---

## Conclusion

Following this guide provides a complete setup for developing and running the Student Management System.

The project uses an isolated Python environment, automated testing, modular source code, and JSON persistence to provide a clean and reproducible development workflow.
