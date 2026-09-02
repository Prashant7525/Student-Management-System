# Setup Guide

This guide explains how to install, configure, run, test, and deploy the Student Management System.

---

## 1. Requirements

Install the following software:

- Python 3.10 or newer
- Git
- pip
- Visual Studio Code (recommended)
- A modern web browser

The project was developed and tested with:

```text
Python 3.14.7
Git 2.55.0
pytest 9.1.1
```

---

## 2. Clone the Repository

Clone the GitHub repository:

```powershell
git clone https://github.com/Prashant7525/Student-Management-System.git
```

Enter the project directory:

```powershell
cd Student-Management-System
```

---

## 3. Create a Virtual Environment

Create the project virtual environment:

```powershell
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

The terminal should now show:

```text
(.venv)
```

before the PowerShell prompt.

---

## 4. Upgrade pip

Run:

```powershell
python -m pip install --upgrade pip
```

---

## 5. Install the Project

For development and testing, install the project in editable mode with development dependencies:

```powershell
python -m pip install -e ".[dev]"
```

This installs:

- FastAPI
- Uvicorn
- pytest
- httpx2

For a normal package installation without development dependencies:

```powershell
python -m pip install .
```

---

## 6. Verify the Installation

Verify Python:

```powershell
python --version
```

Verify pytest:

```powershell
python -m pytest --version
```

Verify the package:

```powershell
python -c "import student_management; print('Package installed successfully')"
```

---

## 7. Run the CLI

Start the command-line application:

```powershell
python -m student_management.main
```

The installed console command can also be used:

```powershell
student-management
```

---

## 8. Run the FastAPI Backend

Start the API server:

```powershell
uvicorn student_management.api.app:app --reload
```

The local API is available at:

```text
http://127.0.0.1:8000
```

---

## 9. Verify the API

Open the health endpoint:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
    "status": "healthy",
    "service": "student-management-api"
}
```

---

## 10. Swagger API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

The Swagger interface can be used to:

- View API endpoints
- Inspect request schemas
- Send test requests
- Inspect API responses

The OpenAPI schema is available at:

```text
http://127.0.0.1:8000/openapi.json
```

---

## 11. Run the Frontend

The frontend is located in:

```text
frontend/
```

From the project root:

```powershell
cd frontend
```

Start a local HTTP server:

```powershell
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

or:

```text
http://localhost:5500
```

Return to the project root when finished:

```powershell
cd ..
```

---

## 12. Frontend API Configuration

The frontend communicates with the backend through:

```text
frontend/js/app.js
```

The production frontend currently uses the deployed API:

```javascript
const API_BASE_URL = "https://student-management-api-hz6k.onrender.com";
```

For local development, the value can be changed to:

```javascript
const API_BASE_URL = "http://127.0.0.1:8000";
```

After changing the value, save the file and refresh the frontend.

Do not commit temporary local-only configuration changes unless they are intended for the project.

---

## 13. CORS Configuration

The FastAPI application supports configurable CORS origins through:

```text
CORS_ORIGINS
```

For local development, PowerShell can be configured with:

```powershell
$env:CORS_ORIGINS="http://localhost:5500,http://127.0.0.1:5500"
```

Start the API after setting the variable:

```powershell
uvicorn student_management.api.app:app --reload
```

To remove the environment variable from the current PowerShell session:

```powershell
Remove-Item Env:CORS_ORIGINS
```

The application also provides local development origins by default.

---

## 14. SQLite Database Configuration

The default SQLite database path is:

```text
data/students.db
```

The path can be configured using:

```text
STUDENT_DATABASE_PATH
```

Example:

```powershell
$env:STUDENT_DATABASE_PATH="data/students.db"
```

Verify the configured path:

```powershell
python -c "from student_management.config import get_database_path; print(get_database_path())"
```

For a Linux deployment environment, an example configured path is:

```text
/var/data/students.db
```

---

## 15. JSON Storage

The JSON repository uses:

```text
data/students.json
```

The JSON database is useful for:

- Local development
- Demonstrating file-based persistence
- Testing the JSON repository
- Migrating existing records to SQLite

---

## 16. JSON to SQLite Migration

The project includes:

```text
src/student_management/utils/migrate_json_to_sqlite.py
```

Run the migration:

```powershell
python -m student_management.utils.migrate_json_to_sqlite
```

The migration:

1. Reads students from JSON.
2. Creates the SQLite database if required.
3. Copies students into SQLite.
4. Avoids inserting students that already exist.

---

## 17. Run the Test Suite

Run all tests:

```powershell
python -m pytest -q
```

The current project test suite contains:

```text
85 tests
```

Expected result:

```text
85 passed
```

For more detailed output:

```powershell
python -m pytest -v
```

---

## 18. Compile Check

Before committing changes, run:

```powershell
python -m compileall src
```

This checks Python source files for syntax errors.

---

## 19. Package Build Check

The project uses `pyproject.toml` and setuptools.

Install the package locally:

```powershell
python -m pip install .
```

Verify the installed package:

```powershell
python -c "import student_management; print(student_management.__file__)"
```

---

## 20. Git Status Check

Before making a commit:

```powershell
git status
```

Review changed files:

```powershell
git diff
```

Check only the documentation changes:

```powershell
git diff -- README.md docs/
```

---

# Deployment Setup

## 21. Backend Deployment — Render

The backend is deployed as a Python web service on Render.

The repository contains:

```text
render.yaml
```

The production backend uses:

```text
Build Command:
pip install .
```

and:

```text
Start Command:
uvicorn student_management.api.app:app --host 0.0.0.0 --port $PORT
```

The health check is:

```text
/health
```

---

## 22. Render Environment Variables

The production backend uses:

```text
CORS_ORIGINS
```

The production frontend origin is included in the Render environment configuration.

A typical configuration is:

```text
https://student-management-system-indol-theta.vercel.app,http://localhost:5500,http://127.0.0.1:5500
```

Environment variables should be configured through the hosting platform rather than committed to the repository.

---

## 23. Production Backend

The deployed API is available at:

```text
https://student-management-api-hz6k.onrender.com
```

Health endpoint:

```text
https://student-management-api-hz6k.onrender.com/health
```

Swagger documentation:

```text
https://student-management-api-hz6k.onrender.com/docs
```

---

## 24. Frontend Deployment — Vercel

The frontend is deployed separately from the backend.

Vercel configuration:

```text
Repository:
Prashant7525/Student-Management-System

Branch:
main

Root Directory:
frontend/

Application Preset:
Other
```

The production frontend is available at:

```text
https://student-management-system-indol-theta.vercel.app
```

The frontend uses the Render API as its production backend.

---

## 25. Production Architecture

```text
User Browser
     │
     ▼
Vercel
     │
     │ HTTPS
     ▼
Render FastAPI
     │
     ▼
SQLite
```

The frontend and backend are deployed independently.

This separation allows:

- Independent frontend deployment
- Independent backend deployment
- Clear API boundaries
- Easier future scaling

---

## 26. Free-Tier Deployment Limitation

The current backend runs on a free Render service.

Free hosting may:

- Spin down inactive services
- Cause a delay when the service wakes up
- Provide limited compute resources
- Not provide persistent application-file storage

Because SQLite is stored as a local database file, the deployed database should be treated as demonstration/portfolio storage rather than production-critical storage.

For a production system, use a managed persistent database such as PostgreSQL.

---

## 27. Production Verification

After deployment, verify the following:

### Backend

Open:

```text
https://student-management-api-hz6k.onrender.com/health
```

Expected:

```json
{
    "status": "healthy",
    "service": "student-management-api"
}
```

### Swagger

Open:

```text
https://student-management-api-hz6k.onrender.com/docs
```

### Frontend

Open:

```text
https://student-management-system-indol-theta.vercel.app
```

Verify:

```text
API Connected
```

Then test:

```text
Create Student
      ↓
Add Marks
      ↓
View Result
      ↓
Search Student
      ↓
Edit Student
      ↓
Delete Student
```

---

## 28. Recommended Development Workflow

For future changes:

```text
1. Create or switch to development branch
          ↓
2. Make a small change
          ↓
3. Run tests
          ↓
4. Run compile/package checks
          ↓
5. Review git diff
          ↓
6. Commit
          ↓
7. Push development
          ↓
8. Test deployment if applicable
          ↓
9. Merge into main
          ↓
10. Push main
```

Before a final release:

```powershell
python -m pytest -q
python -m compileall src
git status
```

---

## 29. Troubleshooting

### `ModuleNotFoundError: No module named 'student_management'`

Make sure the project is installed:

```powershell
python -m pip install -e ".[dev]"
```

or:

```powershell
python -m pip install .
```

---

### Frontend shows API disconnected

Check that:

1. The backend is running.
2. `/health` responds successfully.
3. `API_BASE_URL` is correct.
4. CORS allows the frontend origin.
5. The browser console contains no CORS errors.

---

### SQLite database is not found

Check:

```powershell
python -c "from student_management.config import get_database_path; print(get_database_path())"
```

Make sure the directory exists or allow the repository to create it automatically.

---

### Tests cannot import the package

Make sure the virtual environment is active:

```powershell
.venv\Scripts\Activate.ps1
```

Then reinstall:

```powershell
python -m pip install -e ".[dev]"
```

---

## 30. Clean Local Environment

If the virtual environment needs to be recreated:

Deactivate it:

```powershell
deactivate
```

Delete it:

```powershell
Remove-Item -Recurse -Force .venv
```

Create it again:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -e ".[dev]"
```

Run the tests:

```powershell
python -m pytest -q
```

---

## Summary

A complete local setup is:

```powershell
git clone https://github.com/Prashant7525/Student-Management-System.git
cd Student-Management-System
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
python -m pytest -q
```

Run the CLI:

```powershell
python -m student_management.main
```

Run the API:

```powershell
uvicorn student_management.api.app:app --reload
```

Run the frontend:

```powershell
cd frontend
python -m http.server 5500
```

Production:

```text
Frontend:
https://student-management-system-indol-theta.vercel.app

Backend:
https://student-management-api-hz6k.onrender.com

Swagger:
https://student-management-api-hz6k.onrender.com/docs
```
