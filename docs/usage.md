# Usage Guide

This guide explains how to use the Student Management System through the CLI, REST API, and web interface.

---

## 1. Available Interfaces

The system provides three ways to interact with student records:

```text
1. Command-Line Interface (CLI)
2. REST API
3. Browser-based Web Interface
```

All interfaces ultimately use the same core business concepts and service operations.

---

# CLI Usage

## 2. Start the CLI

From the project root, activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Start the application:

```powershell
python -m student_management.main
```

You can also use:

```powershell
student-management
```

---

## 3. Main Menu

The CLI provides options similar to:

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

Choose an option by entering its number.

---

## 4. Add a Student

Select:

```text
1. Add Student
```

The application asks for:

- Student ID
- Name
- Age
- Email
- Course

Example:

```text
Student ID: STU001
Name: Rahul Kumar
Age: 20
Email: rahul@example.com
Course: Computer Science
```

If the information is valid, the student is stored successfully.

---

## 5. View All Students

Select:

```text
2. View All Students
```

The system displays all stored student records.

Typical information includes:

```text
Student ID
Name
Age
Email
Course
```

---

## 6. Search for Students

Select:

```text
3. Search Student
```

Enter a search term.

For example:

```text
Search: Rahul
```

The system searches student information and displays matching records.

---

## 7. View an Individual Student

Select:

```text
4. View Student
```

Enter the student ID:

```text
Student ID: STU001
```

The student's stored information is displayed.

---

## 8. Update a Student

Select:

```text
5. Update Student
```

Enter the student ID and provide the updated information.

For example:

```text
Student ID: STU001
Name: Rahul Kumar
Age: 21
Email: rahul.kumar@example.com
Course: Computer Science
```

The existing record is updated.

---

## 9. Delete a Student

Select:

```text
6. Delete Student
```

Enter the student ID:

```text
Student ID: STU001
```

The corresponding student record is removed from storage.

---

# Academic Features

## 10. Add or Update Marks

Select:

```text
7. Add / Update Marks
```

Enter:

- Student ID
- Subject
- Mark

Example:

```text
Student ID: STU001
Subject: Python
Mark: 90
```

Marks must be between:

```text
0 and 100
```

If a mark already exists for the subject, it can be updated.

---

## 11. Remove Marks

Select:

```text
8. Remove Marks
```

Enter:

```text
Student ID: STU001
Subject: Python
```

The subject mark is removed from the student's record.

---

## 12. View Result

Select:

```text
9. View Result
```

Enter the student ID.

The system calculates:

```text
Total Marks
Average Marks
Grade
```

Example:

```text
Python:   90
Database: 85

Total:    175
Average:  87.50
Grade:    A
```

---

## 13. Grading System

The system uses the student's average mark.

| Average | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

If a student has no marks, the average is:

```text
0.0
```

and the grade is:

```text
F
```

---

# Web Interface Usage

## 14. Start the Backend

From the project root:

```powershell
uvicorn student_management.api.app:app --reload
```

The API normally runs at:

```text
http://127.0.0.1:8000
```

---

## 15. Start the Frontend

Open another PowerShell terminal.

Navigate to:

```powershell
cd frontend
```

Start the frontend server:

```powershell
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

The frontend communicates with the backend API.

---

## 16. API Connection Status

The dashboard displays the API connection status.

A successful connection is shown as:

```text
🟢 API Connected
```

If the backend is unavailable, the frontend indicates that the API is disconnected.

When troubleshooting, first make sure the FastAPI server is running.

---

## 17. Dashboard

The web dashboard provides summary statistics such as:

```text
Total Students
Courses
Students With Marks
```

These values are updated after student operations.

---

## 18. Add a Student from the Web Interface

Use the **Add Student** button.

Enter:

```text
Student ID
Name
Age
Email
Course
```

Submit the form.

A successful operation displays a confirmation notification.

The student list and dashboard statistics are then refreshed.

---

## 19. Search Students from the Web Interface

Use the search field near the student list.

For example:

```text
Rahul
```

The frontend sends a search request to the API and displays matching students.

Search can be cleared to return to the full student list.

---

## 20. Edit a Student

Use the **Edit** action for the required student.

Modify fields such as:

```text
Name
Age
Email
Course
```

Submit the form.

The frontend sends an update request to the API and refreshes the student list.

---

## 21. Delete a Student

Use the **Delete** action for a student.

After successful deletion:

- The student is removed from the database.
- The student list is refreshed.
- Dashboard statistics are recalculated.
- A success notification is displayed.

---

## 22. Manage Marks

Use the marks action for a student.

Add a subject and mark.

Example:

```text
Subject: Python
Mark: 90
```

The student's marks are saved through the API.

Existing subjects can be updated.

Individual subjects can also be removed.

---

## 23. View Results

Use the **Result** action for a student.

The result view displays:

```text
Student
Course
Marks
Total
Average
Grade
```

For example:

```text
Student: Rahul Kumar
Course: Computer Science

Python: 90

Total:   90
Average: 90.00
Grade:   A+
```

---

# REST API Usage

## 24. API Base URL

### Local

```text
http://127.0.0.1:8000
```

### Production

```text
https://student-management-api-hz6k.onrender.com
```

Swagger documentation:

```text
https://student-management-api-hz6k.onrender.com/docs
```

---

## 25. Health Check

Request:

```text
GET /health
```

Example:

```text
GET http://127.0.0.1:8000/health
```

Expected response:

```json
{
    "status": "healthy",
    "service": "student-management-api"
}
```

---

## 26. Get All Students

Request:

```text
GET /students
```

Example:

```text
GET http://127.0.0.1:8000/students
```

The response contains the available student records.

---

## 27. Get One Student

Request:

```text
GET /students/{student_id}
```

Example:

```text
GET /students/STU001
```

---

## 28. Search Students

Request:

```text
GET /students/search?q={query}
```

Example:

```text
GET /students/search?q=Rahul
```

The API returns students matching the search query.

---

## 29. Create a Student

Request:

```text
POST /students
```

Example JSON:

```json
{
    "student_id": "STU001",
    "name": "Rahul Kumar",
    "age": 20,
    "email": "rahul@example.com",
    "course": "Computer Science"
}
```

---

## 30. Update a Student

Request:

```text
PUT /students/{student_id}
```

Example:

```text
PUT /students/STU001
```

Request body:

```json
{
    "name": "Rahul Kumar",
    "age": 21,
    "email": "rahul.kumar@example.com",
    "course": "Computer Science"
}
```

---

## 31. Delete a Student

Request:

```text
DELETE /students/{student_id}
```

Example:

```text
DELETE /students/STU001
```

---

## 32. Add or Update a Mark

Request:

```text
POST /students/{student_id}/marks
```

Example:

```text
POST /students/STU001/marks
```

Request body:

```json
{
    "subject": "Python",
    "mark": 90
}
```

---

## 33. Remove a Mark

Request:

```text
DELETE /students/{student_id}/marks/{subject}
```

Example:

```text
DELETE /students/STU001/marks/Python
```

---

## 34. Get a Student Result

Request:

```text
GET /students/{student_id}/result
```

Example:

```text
GET /students/STU001/result
```

Example response:

```json
{
    "student_id": "STU001",
    "name": "Rahul Kumar",
    "course": "Computer Science",
    "marks": {
        "Python": 90.0
    },
    "total": 90.0,
    "average": 90.0,
    "grade": "A+"
}
```

---

# Validation

## 35. Student ID Validation

Valid examples:

```text
STU001
STU123
stu456
```

Invalid examples:

```text
ABC001
STUDENT001
STU
123
```

The ID must begin with `STU` and contain at least one digit after it.

---

## 36. Name Validation

Names must:

- Not be empty
- Contain letters and spaces

Example:

```text
Rahul Kumar
```

---

## 37. Age Validation

Age must be an integer from:

```text
1 to 100
```

---

## 38. Email Validation

A basic email format is required.

Example:

```text
rahul@example.com
```

---

## 39. Course Validation

Course names cannot be empty.

Example:

```text
Computer Science
```

---

## 40. Mark Validation

Marks must be numeric values from:

```text
0 to 100
```

Examples:

```text
0
75
90
100
```

---

# Persistence

## 41. JSON Persistence

The JSON repository stores records in:

```text
data/students.json
```

This repository is useful for local file-based storage and migration.

---

## 42. SQLite Persistence

The SQLite repository stores records in:

```text
data/students.db
```

The database is automatically created when the SQLite repository is initialized.

The path can be configured with:

```text
STUDENT_DATABASE_PATH
```

---

## 43. JSON to SQLite Migration

To migrate JSON data to SQLite:

```powershell
python -m student_management.utils.migrate_json_to_sqlite
```

The migration avoids inserting students that already exist in SQLite.

---

# Production Usage

## 44. Production Frontend

The live web application is available at:

```text
https://student-management-system-indol-theta.vercel.app
```

Open the site in a browser and verify:

```text
🟢 API Connected
```

---

## 45. Production Backend

The live API is available at:

```text
https://student-management-api-hz6k.onrender.com
```

Health check:

```text
https://student-management-api-hz6k.onrender.com/health
```

Swagger:

```text
https://student-management-api-hz6k.onrender.com/docs
```

---

## 46. Recommended Production Test

A complete functional workflow is:

```text
Open Web Application
        ↓
Confirm API Connected
        ↓
Create Student
        ↓
Add Mark
        ↓
View Result
        ↓
Search Student
        ↓
Edit Student
        ↓
Delete Student
        ↓
Confirm Student Removed
```

This workflow verifies the main frontend-to-backend functionality.

---

## 47. Free-Tier Limitation

The deployed backend currently uses a free Render service with SQLite.

The service may spin down after inactivity, which can cause a noticeable delay on the first request after inactivity.

Because the database is stored as a local SQLite file, the deployed data should not be considered permanent production storage.

For production use, a managed persistent database such as PostgreSQL is recommended.

---

# Troubleshooting

## 48. API Disconnected

If the frontend shows an API connection problem:

1. Check that the FastAPI server is running.
2. Open `/health`.
3. Check `API_BASE_URL` in `frontend/js/app.js`.
4. Check the browser console.
5. Verify CORS configuration.

---

## 49. Student Not Found

Make sure the correct student ID is being used.

Example:

```text
STU001
```

Student IDs are case-insensitive during validation, but the stored identifier should be used consistently.

---

## 50. Validation Error

Check:

- Student ID format
- Name
- Age
- Email
- Course
- Mark range

The API also returns validation errors when request data does not satisfy the Pydantic schema.

---

## 51. No Students Displayed

Check:

1. The API is running.
2. The database contains records.
3. The frontend is using the correct API URL.
4. No CORS error is present.
5. The request to `/students` succeeds.

---

# Testing

## 52. Run Tests

From the project root:

```powershell
python -m pytest -q
```

The current suite contains:

```text
85 tests
```

Expected result:

```text
85 passed
```

---

## 53. Detailed Test Output

Use:

```powershell
python -m pytest -v
```

This displays each individual test.

---

## 54. Final Usage Workflow

For a normal local development session:

### Terminal 1 — Backend

```powershell
.venv\Scripts\Activate.ps1
uvicorn student_management.api.app:app --reload
```

### Terminal 2 — Frontend

```powershell
.venv\Scripts\Activate.ps1
cd frontend
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500
```

Use the browser interface to manage students.

---

## Summary

The Student Management System can be used through:

```text
CLI
 │
 ├── Student CRUD
 ├── Search
 ├── Marks
 └── Results

REST API
 │
 ├── Student CRUD
 ├── Search
 ├── Marks
 ├── Results
 └── Health

Web Frontend
 │
 ├── Dashboard
 ├── Student CRUD
 ├── Search
 ├── Marks
 ├── Results
 └── API Status
```

The production application is available at:

```text
Frontend:
https://student-management-system-indol-theta.vercel.app

Backend:
https://student-management-api-hz6k.onrender.com

Swagger:
https://student-management-api-hz6k.onrender.com/docs
```
