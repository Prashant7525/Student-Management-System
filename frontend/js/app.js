const API_BASE_URL = "https://student-management-api-hz6k.onrender.com";

let students = [];

let editingStudentId = null;

let managingMarksStudentId = null;


// =========================================================
// DOM Elements
// =========================================================

// ---------- General ----------

const statusIndicator =
    document.getElementById("status-indicator");

const statusText =
    document.getElementById("status-text");

const totalStudentsElement =
    document.getElementById("total-students");

const totalCoursesElement =
    document.getElementById("total-courses");

const studentsWithMarksElement =
    document.getElementById("students-with-marks");

const studentsTableBody =
    document.getElementById("students-table-body");


// ---------- Search ----------

const searchInput =
    document.getElementById("search-input");

const searchButton =
    document.getElementById("search-btn");

const clearSearchButton =
    document.getElementById(
        "clear-search-btn"
    );


// ---------- Student Modal ----------

const addStudentButton =
    document.getElementById(
        "add-student-btn"
    );

const studentModal =
    document.getElementById(
        "student-modal"
    );

const closeModalButton =
    document.getElementById(
        "close-modal-btn"
    );

const cancelFormButton =
    document.getElementById(
        "cancel-form-btn"
    );

const studentForm =
    document.getElementById(
        "student-form"
    );

const modalTitle =
    document.getElementById(
        "modal-title"
    );

const modalDescription =
    document.getElementById(
        "modal-description"
    );

const formError =
    document.getElementById(
        "form-error"
    );

const studentIdInput =
    document.getElementById(
        "student-id"
    );

const studentNameInput =
    document.getElementById(
        "student-name"
    );

const studentAgeInput =
    document.getElementById(
        "student-age"
    );

const studentEmailInput =
    document.getElementById(
        "student-email"
    );

const studentCourseInput =
    document.getElementById(
        "student-course"
    );


// ---------- Marks Modal ----------

const marksModal =
    document.getElementById(
        "marks-modal"
    );

const closeMarksButton =
    document.getElementById(
        "close-marks-btn"
    );

const cancelMarksButton =
    document.getElementById(
        "cancel-marks-btn"
    );

const marksForm =
    document.getElementById(
        "marks-form"
    );

const marksStudentName =
    document.getElementById(
        "marks-student-name"
    );

const markSubjectInput =
    document.getElementById(
        "mark-subject"
    );

const markValueInput =
    document.getElementById(
        "mark-value"
    );

const marksFormError =
    document.getElementById(
        "marks-form-error"
    );

const currentMarksList =
    document.getElementById(
        "current-marks-list"
    );


// ---------- Result Modal ----------

const resultModal =
    document.getElementById(
        "result-modal"
    );

const closeResultButton =
    document.getElementById(
        "close-result-btn"
    );

const resultStudentName =
    document.getElementById(
        "result-student-name"
    );

const resultContent =
    document.getElementById(
        "result-content"
    );


// ---------- Toast ----------

const toastContainer =
    document.getElementById(
        "toast-container"
    );


// =========================================================
// API Helper
// =========================================================

async function apiRequest(
    endpoint,
    options = {}
) {
    const response = await fetch(
        `${API_BASE_URL}${endpoint}`,
        {
            headers: {
                "Content-Type":
                    "application/json",

                ...(options.headers || {}),
            },

            ...options,
        }
    );


    let data = null;


    try {
        data = await response.json();
    } catch {
        data = null;
    }


    if (!response.ok) {
        const message =
            data?.detail ||
            "Something went wrong.";

        throw new Error(message);
    }


    return data;
}


// =========================================================
// API Status
// =========================================================

async function checkApiStatus() {
    try {
        await apiRequest("/");


        statusIndicator.classList.remove(
            "offline"
        );

        statusIndicator.classList.add(
            "online"
        );

        statusText.textContent =
            "API Connected";

    } catch {
        statusIndicator.classList.remove(
            "online"
        );

        statusIndicator.classList.add(
            "offline"
        );

        statusText.textContent =
            "API Offline";
    }
}


// =========================================================
// Load Students
// =========================================================

async function loadStudents() {
    try {
        students =
            await apiRequest(
                "/students"
            );


        renderStudents(
            students
        );


        updateStatistics(
            students
        );

    } catch (error) {

        studentsTableBody.innerHTML = `
            <tr>
                <td
                    colspan="7"
                    class="empty-state"
                >
                    Unable to load students.
                </td>
            </tr>
        `;


        showToast(
            error.message
        );
    }
}


// =========================================================
// Render Students
// =========================================================

function renderStudents(
    studentList
) {

    if (
        studentList.length === 0
    ) {

        studentsTableBody.innerHTML = `
            <tr>
                <td
                    colspan="7"
                    class="empty-state"
                >
                    No students found.
                </td>
            </tr>
        `;

        return;
    }


    studentsTableBody.innerHTML =
        studentList
            .map((student) => {

                const markCount =
                    Object.keys(
                        student.marks || {}
                    ).length;


                return `
                    <tr>

                        <td>
                            ${escapeHtml(
                                student.student_id
                            )}
                        </td>

                        <td>
                            ${escapeHtml(
                                student.name
                            )}
                        </td>

                        <td>
                            ${student.age}
                        </td>

                        <td>
                            ${escapeHtml(
                                student.email
                            )}
                        </td>

                        <td>
                            ${escapeHtml(
                                student.course
                            )}
                        </td>

                        <td>
                            ${markCount}
                        </td>

                        <td>

                            <button
                                class="btn"
                                onclick="manageMarks(
                                    '${escapeHtml(
                                        student.student_id
                                    )}'
                                )"
                            >
                                Marks
                            </button>


                            <button
                                class="btn"
                                onclick="viewResult(
                                    '${escapeHtml(
                                        student.student_id
                                    )}'
                                )"
                            >
                                Result
                            </button>


                            <button
                                class="btn"
                                onclick="editStudent(
                                    '${escapeHtml(
                                        student.student_id
                                    )}'
                                )"
                            >
                                Edit
                            </button>


                            <button
                                class="btn"
                                onclick="deleteStudent(
                                    '${escapeHtml(
                                        student.student_id
                                    )}'
                                )"
                            >
                                Delete
                            </button>

                        </td>

                    </tr>
                `;
            })
            .join("");
}


// =========================================================
// Statistics
// =========================================================

function updateStatistics(
    studentList
) {

    totalStudentsElement.textContent =
        studentList.length;


    const courses =
        new Set(
            studentList.map(
                (student) =>
                    student.course
            )
        );


    totalCoursesElement.textContent =
        courses.size;


    const studentsWithMarks =
        studentList.filter(
            (student) =>
                Object.keys(
                    student.marks || {}
                ).length > 0
        );


    studentsWithMarksElement.textContent =
        studentsWithMarks.length;
}


// =========================================================
// Search
// =========================================================

async function searchStudents() {

    const query =
        searchInput.value.trim();


    if (!query) {
        await loadStudents();

        return;
    }


    try {

        const results =
            await apiRequest(
                `/students/search?q=${encodeURIComponent(
                    query
                )}`
            );


        renderStudents(
            results
        );

    } catch (error) {

        showToast(
            error.message
        );
    }
}


searchButton.addEventListener(
    "click",
    searchStudents
);


searchInput.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter"
        ) {
            searchStudents();
        }

    }
);


clearSearchButton.addEventListener(
    "click",
    async () => {

        searchInput.value = "";

        await loadStudents();
    }
);


// =========================================================
// Student Modal
// =========================================================

function openAddStudentModal() {

    editingStudentId = null;


    modalTitle.textContent =
        "Add Student";


    modalDescription.textContent =
        "Enter the student's information.";


    studentForm.reset();


    studentIdInput.disabled =
        false;


    clearFormError();


    studentModal.classList.remove(
        "hidden"
    );
}


function openEditStudentModal(
    student
) {

    editingStudentId =
        student.student_id;


    modalTitle.textContent =
        "Edit Student";


    modalDescription.textContent =
        "Update the student's information.";


    studentIdInput.value =
        student.student_id;


    studentNameInput.value =
        student.name;


    studentAgeInput.value =
        student.age;


    studentEmailInput.value =
        student.email;


    studentCourseInput.value =
        student.course;


    studentIdInput.disabled =
        true;


    clearFormError();


    studentModal.classList.remove(
        "hidden"
    );
}


function closeStudentModal() {

    studentModal.classList.add(
        "hidden"
    );


    studentForm.reset();


    studentIdInput.disabled =
        false;


    editingStudentId = null;


    clearFormError();
}


function clearFormError() {

    formError.textContent = "";


    formError.classList.add(
        "hidden"
    );
}


function showFormError(
    message
) {

    formError.textContent =
        message;


    formError.classList.remove(
        "hidden"
    );
}


addStudentButton.addEventListener(
    "click",
    openAddStudentModal
);


closeModalButton.addEventListener(
    "click",
    closeStudentModal
);


cancelFormButton.addEventListener(
    "click",
    closeStudentModal
);


// =========================================================
// Create / Update Student
// =========================================================

studentForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        clearFormError();


        const studentData = {

            student_id:
                studentIdInput.value.trim(),

            name:
                studentNameInput.value.trim(),

            age:
                Number(
                    studentAgeInput.value
                ),

            email:
                studentEmailInput.value.trim(),

            course:
                studentCourseInput.value.trim(),
        };


        try {

            if (
                editingStudentId
            ) {

                await apiRequest(
                    `/students/${encodeURIComponent(
                        editingStudentId
                    )}`,
                    {
                        method: "PUT",

                        body:
                            JSON.stringify({
                                name:
                                    studentData.name,

                                age:
                                    studentData.age,

                                email:
                                    studentData.email,

                                course:
                                    studentData.course,
                            }),
                    }
                );


                showToast(
                    "Student updated successfully."
                );

            } else {

                await apiRequest(
                    "/students",
                    {
                        method: "POST",

                        body:
                            JSON.stringify(
                                studentData
                            ),
                    }
                );


                showToast(
                    "Student created successfully."
                );
            }


            closeStudentModal();


            await loadStudents();

        } catch (error) {

            showFormError(
                error.message
            );
        }
    }
);


// =========================================================
// Edit Student
// =========================================================

async function editStudent(
    studentId
) {

    try {

        const student =
            await apiRequest(
                `/students/${encodeURIComponent(
                    studentId
                )}`
            );


        openEditStudentModal(
            student
        );

    } catch (error) {

        showToast(
            error.message
        );
    }
}


// =========================================================
// Delete Student
// =========================================================

async function deleteStudent(
    studentId
) {

    const confirmed =
        window.confirm(
            `Delete student ${studentId}?`
        );


    if (!confirmed) {
        return;
    }


    try {

        await apiRequest(
            `/students/${encodeURIComponent(
                studentId
            )}`,
            {
                method: "DELETE",
            }
        );


        showToast(
            "Student deleted successfully."
        );


        await loadStudents();

    } catch (error) {

        showToast(
            error.message
        );
    }
}


// =========================================================
// Result
// =========================================================

async function viewResult(
    studentId
) {

    resultModal.classList.remove(
        "hidden"
    );


    resultStudentName.textContent =
        "Loading...";


    resultContent.innerHTML =
        "Loading result...";


    try {

        const result =
            await apiRequest(
                `/students/${encodeURIComponent(
                    studentId
                )}/result`
            );


        resultStudentName.textContent =
            `${result.name} (${result.student_id})`;


        const marks =
            Object.entries(
                result.marks
            );


        const marksHtml =
            marks.length === 0
                ? `
                    <p>
                        No marks recorded.
                    </p>
                `
                : `
                    <ul>

                        ${marks
                            .map(
                                ([subject, mark]) =>
                                    `
                                    <li>
                                        ${escapeHtml(
                                            subject
                                        )}:
                                        ${mark}
                                    </li>
                                    `
                            )
                            .join("")}

                    </ul>
                `;


        resultContent.innerHTML = `

            <div class="result-grid">

                <div class="result-item">

                    <span>
                        Total
                    </span>

                    <strong>
                        ${result.total}
                    </strong>

                </div>


                <div class="result-item">

                    <span>
                        Average
                    </span>

                    <strong>
                        ${result.average.toFixed(
                            2
                        )}
                    </strong>

                </div>


                <div class="result-item">

                    <span>
                        Grade
                    </span>

                    <strong>
                        ${escapeHtml(
                            result.grade
                        )}
                    </strong>

                </div>

            </div>


            <h3>
                Marks
            </h3>


            ${marksHtml}
        `;

    } catch (error) {

        resultStudentName.textContent =
            "";


        resultContent.textContent =
            error.message;
    }
}


function closeResultModal() {

    resultModal.classList.add(
        "hidden"
    );
}


closeResultButton.addEventListener(
    "click",
    closeResultModal
);


// =========================================================
// Marks Management
// =========================================================

async function manageMarks(
    studentId
) {

    managingMarksStudentId =
        studentId;


    marksModal.classList.remove(
        "hidden"
    );


    marksStudentName.textContent =
        "Loading...";


    marksForm.reset();


    clearMarksFormError();


    currentMarksList.innerHTML =
        "Loading marks...";


    try {

        const student =
            await apiRequest(
                `/students/${encodeURIComponent(
                    studentId
                )}`
            );


        marksStudentName.textContent =
            `${student.name} (${student.student_id})`;


        renderCurrentMarks(
            student.marks || {}
        );

    } catch (error) {

        marksStudentName.textContent =
            "";


        currentMarksList.textContent =
            error.message;
    }
}


function renderCurrentMarks(
    marks
) {

    const entries =
        Object.entries(marks);


    if (
        entries.length === 0
    ) {

        currentMarksList.innerHTML = `
            <p class="no-marks">
                No marks recorded.
            </p>
        `;

        return;
    }


    currentMarksList.innerHTML = `
        <div class="marks-list">

            ${entries
                .map(
                    ([subject, mark]) =>
                        `
                        <div class="mark-row">

                            <div class="mark-info">

                                <span
                                    class="mark-subject"
                                >
                                    ${escapeHtml(
                                        subject
                                    )}
                                </span>

                                <span
                                    class="mark-value"
                                >
                                    Mark: ${mark}
                                </span>

                            </div>


                            <button
                                class="btn mark-remove-btn"
                                onclick="removeMark(
                                    '${escapeHtml(
                                        managingMarksStudentId
                                    )}',
                                    '${encodeURIComponent(
                                        subject
                                    )}'
                                )"
                            >
                                Remove
                            </button>

                        </div>
                        `
                )
                .join("")}

        </div>
    `;
}


function clearMarksFormError() {

    marksFormError.textContent =
        "";


    marksFormError.classList.add(
        "hidden"
    );
}


function showMarksFormError(
    message
) {

    marksFormError.textContent =
        message;


    marksFormError.classList.remove(
        "hidden"
    );
}


// ---------- Save Mark ----------

marksForm.addEventListener(
    "submit",
    async (event) => {

        event.preventDefault();


        clearMarksFormError();


        const subject =
            markSubjectInput.value.trim();


        const mark =
            Number(
                markValueInput.value
            );


        if (!subject) {

            showMarksFormError(
                "Subject cannot be empty."
            );

            return;
        }


        if (
            Number.isNaN(mark) ||
            mark < 0 ||
            mark > 100
        ) {

            showMarksFormError(
                "Mark must be between 0 and 100."
            );

            return;
        }


        try {

            await apiRequest(
                `/students/${encodeURIComponent(
                    managingMarksStudentId
                )}/marks`,
                {
                    method: "POST",

                    body:
                        JSON.stringify({
                            subject:
                                subject,

                            mark:
                                mark,
                        }),
                }
            );


            showToast(
                "Mark saved successfully."
            );


            markSubjectInput.value =
                "";

            markValueInput.value =
                "";


            await refreshMarksModal();


            await loadStudents();

        } catch (error) {

            showMarksFormError(
                error.message
            );
        }
    }
);


// =========================================================
// Refresh Marks Modal
// =========================================================

async function refreshMarksModal() {

    if (
        !managingMarksStudentId
    ) {
        return;
    }


    try {

        const student =
            await apiRequest(
                `/students/${encodeURIComponent(
                    managingMarksStudentId
                )}`
            );


        marksStudentName.textContent =
            `${student.name} (${student.student_id})`;


        renderCurrentMarks(
            student.marks || {}
        );

    } catch (error) {

        currentMarksList.textContent =
            error.message;
    }
}


// =========================================================
// Remove Mark
// =========================================================

async function removeMark(
    studentId,
    encodedSubject
) {

    const subject =
        decodeURIComponent(
            encodedSubject
        );


    const confirmed =
        window.confirm(
            `Remove mark for ${subject}?`
        );


    if (!confirmed) {
        return;
    }


    try {

        await apiRequest(
            `/students/${encodeURIComponent(
                studentId
            )}/marks/${encodedSubject}`,
            {
                method: "DELETE",
            }
        );


        showToast(
            "Mark removed successfully."
        );


        await refreshMarksModal();


        await loadStudents();

    } catch (error) {

        showToast(
            error.message
        );
    }
}


// =========================================================
// Close Marks Modal
// =========================================================

function closeMarksModal() {

    marksModal.classList.add(
        "hidden"
    );


    marksForm.reset();


    clearMarksFormError();


    managingMarksStudentId =
        null;
}


closeMarksButton.addEventListener(
    "click",
    closeMarksModal
);


cancelMarksButton.addEventListener(
    "click",
    closeMarksModal
);


// =========================================================
// Toast
// =========================================================

function showToast(
    message
) {

    const toast =
        document.createElement(
            "div"
        );


    toast.className =
        "toast";


    toast.textContent =
        message;


    toastContainer.appendChild(
        toast
    );


    setTimeout(() => {

        toast.remove();

    }, 3000);
}


// =========================================================
// Security Helper
// =========================================================

function escapeHtml(
    value
) {

    const element =
        document.createElement(
            "div"
        );


    element.textContent =
        value;


    return element.innerHTML;
}


// =========================================================
// Initial Load
// =========================================================

async function initializeApp() {

    await checkApiStatus();

    await loadStudents();
}


initializeApp();