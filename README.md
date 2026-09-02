# Student Management System

A modular Python-based Student Management System that provides student CRUD operations, academic marks management, result calculation, REST API access, and a web-based interface.

The project was developed incrementally with clean architecture, input validation, automated testing, JSON and SQLite persistence, Python packaging, Git/GitHub workflows, and cloud deployment.

## 🌐 Live Demo

**Frontend:**  
https://student-management-system-indol-theta.vercel.app

**Backend API:**  
https://student-management-api-hz6k.onrender.com

**API Documentation (Swagger):**  
https://student-management-api-hz6k.onrender.com/docs

> The live demo uses Vercel for the frontend and Render for the FastAPI backend.

---

## 📌 Project Status

- ✅ Student management completed
- ✅ CLI application completed
- ✅ JSON persistence implemented
- ✅ SQLite persistence implemented
- ✅ Service/repository architecture implemented
- ✅ Input validation implemented
- ✅ REST API implemented with FastAPI
- ✅ Swagger/OpenAPI documentation available
- ✅ Responsive web frontend implemented
- ✅ Frontend connected to production API
- ✅ Automated API tests implemented
- ✅ SQLite repository tests implemented
- ✅ Integration and persistence tests implemented
- ✅ Python package configuration implemented
- ✅ Console entry point implemented
- ✅ Render deployment completed
- ✅ Vercel deployment completed
- ✅ Production CRUD workflow verified
- ✅ 85 automated tests passing
- ✅ MIT License added

---

## ✨ Features

### Student Management

- Add students
- View all students
- View individual students
- Search students
- Update student information
- Delete students

### Academic Management

- Add subject marks
- Update existing marks
- Remove subject marks
- Calculate total marks
- Calculate average marks
- Automatically calculate grades
- View student results

### Validation

The system validates:

- Student IDs
- Names
- Ages
- Email addresses
- Course names
- Marks

### Persistence

Two repository implementations are available:

- JSON repository
- SQLite repository

The application uses SQLite for the deployed API while JSON remains available for the original local storage workflow and migration support.

### REST API

The FastAPI backend provides endpoints for:

- Student CRUD operations
- Student search
- Marks management
- Result calculation
- Health checking

### Web Interface

The frontend provides:

- Dashboard statistics
- Student table
- Search
- Add student
- Edit student
- Delete student
- Marks management
- Result display
- API connection status
- Toast notifications
- Input validation feedback

---

## 🛠️ Technology Stack

### Backend

- Python 3.14
- FastAPI
- Pydantic
- Uvicorn
- SQLite
- JSON

### Frontend

- HTML5
- CSS3
- JavaScript

### Testing

- pytest
- httpx2

### Development Tools

- Git
- GitHub
- Visual Studio Code
- Python virtual environment
- setuptools

### Deployment

- Vercel — frontend
- Render — backend API

---

## 🏗️ Architecture

The project follows a layered architecture with a separate web/API layer.

```text
                         ┌──────────────────────┐
                         │     Web Browser      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Vercel Frontend     │
                         │  HTML/CSS/JavaScript │
                         └──────────┬───────────┘
                                    │ HTTPS
                                    ▼
                         ┌──────────────────────┐
                         │   FastAPI Backend    │
                         │      on Render       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    Service Layer     │
                         │    Business Logic    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  Repository Layer    │
                         └──────────┬───────────┘
                                    │
                         ┌──────────┴───────────┐
                         ▼                      ▼
                ┌─────────────────┐    ┌─────────────────┐
                │ SQLite          │    │ JSON            │
                │ Repository      │    │ Repository      │
                └─────────────────┘    └─────────────────┘
```

### Backend layers

```text
API Layer
    ↓
Service Layer
    ↓
Repository Layer
    ↓
Database / JSON Storage
```

### Core components

```text
src/student_management/
│
├── api/
│   ├── app.py
│   └── schemas.py
│
├── cli/
│   └── menu.py
│
├── models/
│   └── student.py
│
├── repositories/
│   ├── student_repository.py
│   ├── sqlite_student_repository.py
│   └── student_repository_protocol.py
│
├── services/
│   └── student_service.py
│
├── utils/
│   ├── validators.py
│   └── migrate_json_to_sqlite.py
│
├── config.py
└── main.py
```

---

## 📂 Project Structure

```text
Student-Management-System/
│
├── data/
│   └── students.json
│
├── docs/
│   ├── architecture.md
│   ├── setup.md
│   └── usage.md
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
│
├── src/
│   └── student_management/
│       ├── api/
│       │   ├── __init__.py
│       │   ├── app.py
│       │   └── schemas.py
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
│       │   ├── student_repository.py
│       │   ├── sqlite_student_repository.py
│       │   └── student_repository_protocol.py
│       │
│       ├── services/
│       │   ├── __init__.py
│       │   └── student_service.py
│       │
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── validators.py
│       │   └── migrate_json_to_sqlite.py
│       │
│       ├── __init__.py
│       ├── config.py
│       └── main.py
│
├── tests/
│   ├── test_api.py
│   ├── test_integration.py
│   ├── test_menu.py
│   ├── test_repository.py
│   ├── test_sqlite_repository.py
│   ├── test_student.py
│   ├── test_student_service.py
│   └── test_validators.py
│
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── pytest.ini
├── README.md
├── render.yaml
└── requirements.txt
```

---

## ⚙️ Requirements

- Python 3.10+
- Git
- pip
- A modern web browser

The project was developed and tested using:

```text
Python 3.14.7
pytest 9.1.1
Git 2.55.0
```

---

## 🚀 Local Installation

### 1. Clone the repository

```powershell
git clone https://github.com/Prashant7525/Student-Management-System.git
```

### 2. Enter the project directory

```powershell
cd Student-Management-System
```

### 3. Create a virtual environment

```powershell
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install the project

For development and testing:

```powershell
python -m pip install -e ".[dev]"
```

For a normal package installation:

```powershell
python -m pip install .
```

---

## ▶️ Run the CLI

After installation:

```powershell
python -m student_management.main
```

Or use the installed console command:

```powershell
student-management
```

---

## 🌐 Run the API Locally

Start the FastAPI server:

```powershell
uvicorn student_management.api.app:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🖥️ Run the Frontend Locally

The frontend is located in:

```text
frontend/
```

For local development:

```powershell
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

The frontend communicates with the configured API endpoint in:

```text
frontend/js/app.js
```

---

## 🔌 API Endpoints

### Health

```text
GET /health
```

### Students

```text
GET    /students
GET    /students/{student_id}
POST   /students
PUT    /students/{student_id}
DELETE /students/{student_id}
```

### Search

```text
GET /students/search?q={query}
```

### Marks

```text
POST   /students/{student_id}/marks
DELETE /students/{student_id}/marks/{subject}
```

### Result

```text
GET /students/{student_id}/result
```

---

## 🧪 Testing

The project uses pytest.

Run the complete test suite:

```powershell
python -m pytest -q
```

Current result:

```text
85 passed
```

The test suite covers:

- Student model
- Validation
- JSON repository
- SQLite repository
- Service layer
- CLI
- API endpoints
- Integration workflows
- Persistence behavior

---

## 📊 Validation Rules

### Student ID

Must:

- Start with `STU`
- Be followed by one or more digits
- Be case-insensitive

Examples:

```text
STU001
STU123
stu456
```

### Name

- Must not be empty
- Must contain letters and spaces

### Age

```text
1 - 100
```

### Email

A basic valid email format is required.

Example:

```text
rahul@example.com
```

### Course

The course name cannot be empty.

### Marks

Marks must be:

```text
0 - 100
```

---

## 🎓 Grading System

Grades are calculated using the student's average marks.

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

Example:

```text
Python: 90

Total:   90
Average: 90.00
Grade:   A+
```

---

## 💾 Data Persistence

### JSON

The JSON repository stores records in:

```text
data/students.json
```

### SQLite

The SQLite repository uses:

```text
data/students.db
```

The SQLite database path can be configured using:

```text
STUDENT_DATABASE_PATH
```

Example:

```powershell
$env:STUDENT_DATABASE_PATH="data/students.db"
```

For deployment, the database path can point to a persistent mounted location when the hosting platform provides one.

---

## 🔄 JSON to SQLite Migration

The project includes a migration utility:

```text
src/student_management/utils/migrate_json_to_sqlite.py
```

Run it with:

```powershell
python -m student_management.utils.migrate_json_to_sqlite
```

The migration copies students from JSON storage into SQLite without duplicating students that already exist in the SQLite database.

---

## ☁️ Deployment

### Frontend — Vercel

The static frontend is deployed from:

```text
frontend/
```

Production frontend:

```text
https://student-management-system-indol-theta.vercel.app
```

### Backend — Render

The FastAPI application is deployed using:

```text
render.yaml
```

Production API:

```text
https://student-management-api-hz6k.onrender.com
```

The backend uses:

```text
uvicorn student_management.api.app:app --host 0.0.0.0 --port $PORT
```

### CORS

The backend uses the `CORS_ORIGINS` environment variable.

The production frontend domain is included in the Render configuration.

---

## ⚠️ Free-Tier Deployment Note

The current deployment uses SQLite on a free Render web service.

Free hosting environments may spin down inactive services and may not provide persistent disk storage.

Therefore, the deployed SQLite database should be considered suitable for demonstration and portfolio purposes rather than production-critical data.

For a production system, the database should be moved to a managed persistent database such as PostgreSQL and configured with appropriate backups and operational monitoring.

---

## 🔐 Security Considerations

The current project is intended as a learning and portfolio application.

It currently does not implement:

- User authentication
- Role-based access control
- Password management
- Production database backups
- Rate limiting
- Advanced audit logging

These are potential future enhancements for a larger production deployment.

---

## 🧪 Production Verification

The deployed application was manually verified through the public frontend.

Verified operations include:

```text
API Connection          ✅
Create Student          ✅
Read Student            ✅
Update Student          ✅
Delete Student          ✅
Search Student          ✅
Add Marks               ✅
View Result             ✅
Dashboard Statistics    ✅
Vercel Frontend         ✅
Render Backend          ✅
```

Example verified workflow:

```text
Create STU001
     ↓
Add Python mark: 90
     ↓
View Result
     ↓
Total: 90
Average: 90.00
Grade: A+
     ↓
Search Rahul
     ↓
Update student
     ↓
Delete student
```

---

## 📚 Documentation

Detailed documentation is available in:

- [Architecture Guide](docs/architecture.md)
- [Setup Guide](docs/setup.md)
- [Usage Guide](docs/usage.md)

---

## 🎯 Learning Objectives

This project demonstrates practical experience with:

- Python programming
- Object-oriented programming
- Dataclasses
- Clean architecture
- Separation of concerns
- Repository pattern
- Service layer design
- Protocol-based abstraction
- Input validation
- Exception handling
- JSON serialization
- SQLite
- CRUD operations
- REST APIs
- FastAPI
- Pydantic
- HTML/CSS/JavaScript
- CORS
- Automated testing
- Integration testing
- Persistence testing
- Python packaging
- Git
- GitHub
- Cloud deployment
- Documentation

---

## 🔮 Future Improvements

Possible future versions may include:

- PostgreSQL production database
- Authentication and authorization
- Admin dashboard
- Role-based access control
- Attendance management
- Course management
- Advanced filtering and sorting
- CSV/PDF exports
- Detailed academic reports
- Automated database migrations
- Structured logging
- CI/CD workflows
- API rate limiting
- Production monitoring
- Custom domain
- Automated backups

---

## 🧩 Development Approach

The project was developed incrementally:

```text
Phase 1  → Project Foundation
Phase 2  → Student Model
Phase 3  → Input Validation
Phase 4  → JSON Repository
Phase 5  → Service Layer
Phase 6  → CLI
Phase 7  → Integration & Persistence Testing
Phase 8  → Documentation & Project Polish
Phase 9  → GitHub & Python Packaging
Phase 10 → FastAPI, SQLite, Web Frontend & Deployment
```

Each major phase was tested and committed using Git.

---

## 📜 License

This project is licensed under the MIT License.

See the [MIT License](https://github.com/Prashant7525/Student-Management-System/blob/main/LICENSE) for details.
