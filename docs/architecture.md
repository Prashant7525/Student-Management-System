# Architecture

## Overview

The Student Management System follows a layered architecture designed to keep business logic, data access, user interfaces, and external interfaces separated.

The project currently supports:

- Command-line interaction
- REST API access through FastAPI
- A browser-based frontend
- JSON persistence
- SQLite persistence

The architecture makes it possible to change the storage mechanism without rewriting the business logic.

---

## High-Level Architecture

```text
                         ┌──────────────────────────┐
                         │       Web Browser        │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │    Frontend Application  │
                         │      HTML/CSS/JavaScript │
                         └────────────┬─────────────┘
                                      │ HTTPS
                                      ▼
                         ┌──────────────────────────┐
                         │       FastAPI API        │
                         │       API Layer          │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │      Service Layer       │
                         │    Business Operations   │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │    Repository Protocol   │
                         │   Storage Abstraction    │
                         └────────────┬─────────────┘
                                      │
                       ┌──────────────┴──────────────┐
                       ▼                             ▼
              ┌──────────────────┐         ┌──────────────────┐
              │ SQLite Repository │         │  JSON Repository │
              └────────┬─────────┘         └────────┬─────────┘
                       │                            │
                       ▼                            ▼
              ┌──────────────────┐         ┌──────────────────┐
              │ students.db      │         │ students.json   │
              └──────────────────┘         └──────────────────┘
```

The CLI provides an additional interface to the same service layer:

```text
CLI
 │
 ▼
StudentService
 │
 ▼
Repository
 │
 ▼
Storage
```

---

## Architectural Layers

### 1. Presentation Layer

The project has two user-facing interfaces.

#### CLI

The command-line interface is implemented in:

```text
src/student_management/cli/
```

The CLI provides menu-based access to student operations.

#### Web Frontend

The browser interface is located in:

```text
frontend/
├── index.html
├── css/
│   └── style.css
└── js/
    └── app.js
```

The frontend communicates with the FastAPI backend using HTTP requests.

---

### 2. API Layer

The REST API is implemented in:

```text
src/student_management/api/
├── __init__.py
├── app.py
└── schemas.py
```

The API layer is responsible for:

- HTTP routing
- Request validation
- Response serialization
- CORS configuration
- Converting API requests into service-layer operations

FastAPI and Pydantic are used for the web API.

The API does not directly contain the application's core business rules.

---

### 3. Service Layer

The service layer is implemented in:

```text
src/student_management/services/student_service.py
```

`StudentService` contains the application's business logic.

Responsibilities include:

- Adding students
- Retrieving students
- Searching students
- Updating students
- Deleting students
- Adding marks
- Removing marks
- Calculating academic results
- Applying business validation

The service layer depends on a repository abstraction rather than a specific storage implementation.

---

### 4. Repository Layer

Repositories are responsible for data persistence.

The repository layer contains:

```text
src/student_management/repositories/
├── student_repository.py
├── sqlite_student_repository.py
└── student_repository_protocol.py
```

#### JSON Repository

```text
StudentRepository
```

Stores student records in:

```text
data/students.json
```

#### SQLite Repository

```text
SQLiteStudentRepository
```

Stores student records in:

```text
data/students.db
```

Both repositories expose the operations required by the service layer.

---

## Repository Abstraction

The project uses `StudentRepositoryProtocol` to define the storage contract.

```text
StudentService
      │
      ▼
StudentRepositoryProtocol
      │
      ├──────────────► StudentRepository
      │                 JSON storage
      │
      └──────────────► SQLiteStudentRepository
                        SQLite storage
```

This design reduces coupling between business logic and persistence.

For example, the service layer does not need to know whether a student is stored in JSON or SQLite.

---

## Domain Model

The main domain model is:

```text
src/student_management/models/student.py
```

The `Student` dataclass contains:

- Student ID
- Name
- Age
- Email
- Course
- Marks

It also provides academic calculations:

```text
Student
 ├── total_marks()
 ├── average_marks()
 └── grade()
```

This keeps student-related calculations close to the student domain model.

---

## Validation Layer

Validation utilities are located in:

```text
src/student_management/utils/validators.py
```

The validation functions handle:

- Student IDs
- Names
- Ages
- Emails
- Courses
- Marks

Validation occurs before data is passed into the appropriate business operation.

The API also uses Pydantic request models to perform request-level validation.

---

## API Request Flow

A typical web request follows this path:

```text
Browser
   │
   │ HTTP Request
   ▼
FastAPI Route
   │
   │ validated request
   ▼
StudentService
   │
   │ business operation
   ▼
Repository
   │
   │ database operation
   ▼
SQLite
```

The response follows the reverse direction:

```text
SQLite
   │
   ▼
Repository
   │
   ▼
StudentService
   │
   ▼
FastAPI
   │
   ▼
Browser
```

---

## Example: Creating a Student

When a user creates a student through the web interface:

```text
1. User fills in the form
          ↓
2. JavaScript sends POST /students
          ↓
3. FastAPI receives the request
          ↓
4. Pydantic validates the request
          ↓
5. StudentService processes the operation
          ↓
6. Repository stores the student
          ↓
7. SQLite persists the record
          ↓
8. API returns the created student
          ↓
9. Frontend updates the interface
```

---

## Example: Viewing a Result

```text
User clicks "Result"
       ↓
Frontend sends GET /students/STU001/result
       ↓
FastAPI route
       ↓
StudentService
       ↓
Repository
       ↓
Student object
       ↓
total_marks()
average_marks()
grade()
       ↓
ResultResponse
       ↓
Frontend displays result
```

---

## Database Design

The SQLite repository uses a single `students` table.

Conceptually:

```text
students
├── student_id  TEXT PRIMARY KEY
├── name        TEXT
├── age         INTEGER
├── email       TEXT
├── course      TEXT
└── marks       TEXT
```

The marks dictionary is serialized as JSON inside the `marks` column.

Example:

```json
{
    "Python": 90.0,
    "Database": 85.0
}
```

This approach keeps the current project simple while allowing the repository implementation to be replaced later with a more normalized relational design.

---

## Configuration

Configuration is centralized in:

```text
src/student_management/config.py
```

The SQLite database path can be configured through:

```text
STUDENT_DATABASE_PATH
```

For example:

```powershell
$env:STUDENT_DATABASE_PATH="data/students.db"
```

This allows deployment environments to provide their own database location without changing application code.

---

## CORS Configuration

The API supports configurable CORS origins through:

```text
CORS_ORIGINS
```

The value can contain multiple comma-separated origins.

Example:

```text
https://student-management-system-indol-theta.vercel.app,http://localhost:5500,http://127.0.0.1:5500
```

This allows the production frontend and local development frontend to communicate with the API.

---

## Deployment Architecture

The production application is split across two hosting services.

```text
                  INTERNET
                     │
                     ▼
        ┌─────────────────────────┐
        │         Vercel          │
        │   Static Web Frontend   │
        └────────────┬────────────┘
                     │
                     │ HTTPS API requests
                     ▼
        ┌─────────────────────────┐
        │         Render          │
        │      FastAPI Backend    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │        SQLite DB        │
        │      students.db        │
        └─────────────────────────┘
```

### Frontend

Hosted on Vercel:

```text
https://student-management-system-indol-theta.vercel.app
```

### Backend

Hosted on Render:

```text
https://student-management-api-hz6k.onrender.com
```

### API Documentation

Swagger UI:

```text
https://student-management-api-hz6k.onrender.com/docs
```

---

## Free-Tier Storage Limitation

The current deployment uses SQLite on a free Render service.

Free hosting environments can spin down inactive services and may not provide persistent storage for application files.

Therefore, the deployed database is suitable for:

- Demonstrations
- Portfolio projects
- Learning
- Functional testing

It should not be treated as production-critical persistent storage.

For a production deployment, the recommended architecture would be:

```text
Frontend
   │
   ▼
API
   │
   ▼
Managed PostgreSQL
```

with backups, monitoring, authentication, and appropriate access controls.

---

## Migration Support

The project provides a JSON-to-SQLite migration utility:

```text
src/student_management/utils/migrate_json_to_sqlite.py
```

Its purpose is to allow existing JSON data to be transferred to SQLite without changing the domain model.

Migration flow:

```text
students.json
     │
     ▼
StudentRepository
     │
     ▼
Student objects
     │
     ▼
SQLiteStudentRepository
     │
     ▼
students.db
```

---

## Testing Architecture

The project uses pytest and separates tests according to application layers.

```text
tests/
├── test_student.py
├── test_validators.py
├── test_repository.py
├── test_sqlite_repository.py
├── test_student_service.py
├── test_menu.py
├── test_api.py
└── test_integration.py
```

The test suite currently contains:

```text
85 tests
```

The tests cover:

- Domain model behavior
- Validation
- JSON persistence
- SQLite persistence
- Service operations
- CLI behavior
- API endpoints
- Integration workflows
- Persistence behavior

---

## Design Principles

The architecture follows several software engineering principles.

### Separation of Concerns

Each layer has a focused responsibility.

```text
Frontend     → User interaction
API          → HTTP interface
Service      → Business logic
Repository   → Persistence
Model        → Domain data and calculations
Validation   → Input rules
```

### Dependency Inversion

The service layer depends on:

```text
StudentRepositoryProtocol
```

rather than directly depending on SQLite or JSON storage.

### Single Responsibility

Classes and modules are designed around specific responsibilities.

### Extensibility

A new repository implementation can be introduced without rewriting the service layer.

For example:

```text
StudentRepositoryProtocol
       │
       ├── JSON
       ├── SQLite
       └── PostgreSQL (future)
```

---

## Future Architecture

A future production-oriented version could evolve into:

```text
                       ┌───────────────────┐
                       │     Frontend      │
                       │       Vercel      │
                       └─────────┬─────────┘
                                 │
                                 ▼
                       ┌───────────────────┐
                       │    FastAPI API    │
                       │      Backend      │
                       └─────────┬─────────┘
                                 │
                    ┌────────────┴────────────┐
                    ▼                         ▼
             ┌──────────────┐        ┌────────────────┐
             │ Service Layer│        │ Authentication │
             └──────┬───────┘        └────────────────┘
                    │
                    ▼
             ┌──────────────┐
             │ Repository   │
             │ Abstraction  │
             └──────┬───────┘
                    │
                    ▼
             ┌──────────────┐
             │ PostgreSQL   │
             │ Managed DB   │
             └──────────────┘
```

Potential additions include:

- Authentication
- Role-based authorization
- PostgreSQL
- Database migrations
- Structured logging
- Monitoring
- Rate limiting
- Automated backups
- CI/CD
- Production observability

---

## Summary

The Student Management System uses a layered, modular architecture:

```text
Presentation
     ↓
API / CLI
     ↓
Service
     ↓
Repository Protocol
     ↓
Persistence
```

This structure keeps the application understandable while providing a foundation for future features and alternative storage systems.
