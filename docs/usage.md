# Usage Guide

## Overview

The Student Management System provides a command-line interface for managing student records, academic marks, and results.

Start the application with:

```powershell
$env:PYTHONPATH = "src"
python -m student_management.main
```

The main menu contains nine operations and an exit option.

---

## Main Menu

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

Enter the number of the operation you want to perform.

---

## 1. Add Student

Select:

```text
1
```

The application asks for:

- Student ID
- Name
- Age
- Email
- Course

Example:

```text
--- Add Student ---
Student ID: STU001
Name: Rahul Kumar
Age: 20
Email: rahul@example.com
Course: Computer Science

✓ Student 'STU001' added successfully!
```

### Validation

The application checks all entered information before saving the student.

Invalid input produces a user-friendly error message.

For example:

```text
Student ID: ABC001
```

produces:

```text
❌ Invalid student ID.
```

---

## 2. View All Students

Select:

```text
2
```

The application displays all stored students.

Example:

```text
--- All Students ---

ID          Name                     Age     Course
----------------------------------------------------------------------
STU001      Rahul Kumar              20      Computer Science
STU002      Priya Sharma             21      Data Science
```

If there are no students:

```text
No students found.
```

---

## 3. Search Student

Select:

```text
3
```

Enter a search term.

The system searches across:

- Student ID
- Name
- Email
- Course

Example:

```text
--- Search Student ---
Enter search term: Rahul
```

The matching student is displayed:

```text
Found 1 student(s):

ID     : STU001
Name   : Rahul Kumar
Age    : 20
Email  : rahul@example.com
Course : Computer Science
----------------------------------------
```

The search is case-insensitive.

For example:

```text
rahul
RAHUL
Rahul
```

can all find the same student.

---

## 4. View Student

Select:

```text
4
```

Enter a student ID:

```text
--- View Student ---
Student ID: STU001
```

The application displays detailed information:

```text
---------------------------------------------
Student Details
---------------------------------------------
ID     : STU001
Name   : Rahul Kumar
Age    : 20
Email  : rahul@example.com
Course : Computer Science

Marks:
  Python               90.00
---------------------------------------------
```

If the student does not exist:

```text
❌ Student 'STU999' not found.
```

---

## 5. Update Student

Select:

```text
5
```

Enter the student's ID:

```text
--- Update Student ---
Student ID: STU001
```

The current information is displayed as prompts:

```text
Press Enter to keep the current value.

Name [Rahul Kumar]:
Age [20]:
Email [rahul@example.com]:
Course [Computer Science]:
```

Pressing Enter keeps the existing value.

For example, changing only the course:

```text
Name [Rahul Kumar]:
Age [20]:
Email [rahul@example.com]:
Course [Computer Science]: Data Science
```

The application confirms:

```text
✓ Student 'STU001' updated successfully!
```

### Important

Existing marks are preserved when student information is updated.

---

## 6. Delete Student

Select:

```text
6
```

Enter the student ID:

```text
--- Delete Student ---
Student ID: STU001
```

The application asks for confirmation:

```text
Student: Rahul Kumar
Are you sure you want to delete this student? (y/n):
```

Enter:

```text
y
```

The student is deleted:

```text
✓ Student 'STU001' deleted successfully.
```

If anything other than `y` is entered, deletion is cancelled:

```text
Deletion cancelled.
```

---

## 7. Add / Update Marks

Select:

```text
7
```

Enter:

- Student ID
- Subject
- Mark

Example:

```text
--- Add / Update Marks ---
Student ID: STU001
Subject: Python
Mark (0-100): 90
```

The application confirms:

```text
✓ Mark for 'Python' saved successfully for Rahul Kumar.
```

### Updating a Mark

If the same subject is entered again, its existing mark is updated.

For example:

```text
Subject: Python
Mark (0-100): 95
```

The Python mark becomes:

```text
Python    95.00
```

### Mark Validation

Marks must be between:

```text
0 - 100
```

Invalid values are rejected.

---

## 8. Remove Marks

Select:

```text
8
```

Enter:

```text
Student ID: STU001
Subject: Python
```

The mark is removed:

```text
✓ Mark for 'Python' removed from Rahul Kumar.
```

If the subject does not exist:

```text
❌ Subject 'Python' does not exist for this student.
```

---

## 9. View Result

Select:

```text
9
```

Enter the student ID:

```text
--- View Result ---
Student ID: STU001
```

The application calculates and displays the result.

Example:

```text
=============================================
               STUDENT RESULT
=============================================
ID     : STU001
Name   : Rahul Kumar
Course : Computer Science

Marks:
  Python                90.00
  Database              80.00

---------------------------------------------
Total   : 170.00
Average : 85.00
Grade   : A
=============================================
```

### Result Calculations

The total is the sum of all subject marks.

For example:

```text
Python     90
Database   80
```

Total:

```text
90 + 80 = 170
```

Average:

```text
170 / 2 = 85
```

The grade is then calculated from the average.

---

## Grading System

| Average | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| Below 50 | F |

---

## 0. Exit

Select:

```text
0
```

The application exits with:

```text
Thank you for using Student Management System.
```

---

## Complete Example Workflow

A complete student workflow can look like this:

### Step 1: Add Student

```text
1
```

Enter:

```text
STU001
Rahul Kumar
20
rahul@example.com
Computer Science
```

### Step 2: Add Marks

Select:

```text
7
```

Add:

```text
Python     90
Database   85
Math       80
```

### Step 3: View Student

Select:

```text
4
```

The student's profile and marks are displayed.

### Step 4: View Result

Select:

```text
9
```

The system calculates:

```text
Total   : 255.00
Average : 85.00
Grade   : A
```

### Step 5: Update Student

Select:

```text
5
```

Change the course if necessary.

Existing marks remain unchanged.

### Step 6: Search Student

Select:

```text
3
```

Search using:

```text
Rahul
```

### Step 7: Delete Student

Select:

```text
6
```

Confirm with:

```text
y
```

---

## Data Persistence

Student information is automatically saved to:

```text
data/students.json
```

Changes are persisted when:

- A student is added
- Student information is updated
- Marks are added
- Marks are updated
- Marks are removed
- A student is deleted

This means the data remains available after closing and reopening the application.

---

## Error Handling

The application handles common errors without crashing.

Examples include:

### Invalid Student ID

```text
❌ Invalid student ID.
```

### Invalid Name

```text
❌ Invalid student name.
```

### Invalid Age

```text
❌ Invalid age.
```

### Invalid Email

```text
❌ Invalid email address.
```

### Invalid Mark

```text
❌ Mark must be between 0 and 100.
```

### Duplicate Student

```text
❌ Student with ID 'STU001' already exists.
```

### Student Not Found

```text
❌ Student 'STU999' not found.
```

### Empty Search

An empty search term produces:

```text
No matching students found.
```

---

## Tips for Using the Application

- Use unique student IDs.
- Follow the `STU` + digits format.
- Enter marks between 0 and 100.
- Use a valid email format.
- Press Enter during an update when you want to keep the current value.
- Confirm deletion carefully.
- Run `pytest` after making code changes.

---

## Data File

The application stores records in:

```text
data/students.json
```

Do not manually edit this file unless you understand the JSON structure.

Invalid JSON may prevent existing records from loading correctly.

---

## Testing the Application

Before committing changes, run:

```powershell
pytest
```

The project currently has:

```text
61 tests
61 passed
```

A successful test run indicates that the core functionality, CLI, service layer, repository, validation, integration, and persistence behavior are working as expected.

---

## Recommended User Flow

For a new student, the recommended sequence is:

```text
Add Student
     ↓
Add / Update Marks
     ↓
View Student
     ↓
View Result
     ↓
Search / Update if needed
     ↓
Delete when no longer required
```

---

## Conclusion

The Student Management System provides a simple command-line workflow for managing student information and academic records.

The application combines validation, business logic, JSON persistence, and automated testing to provide a reliable foundation for future improvements such as SQLite, GUI, REST API, and web-based interfaces.
