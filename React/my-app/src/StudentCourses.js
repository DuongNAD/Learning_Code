import React from "react";

function StudentCourses({courses, newCourseValue, onInputChange, onAddCourse}){
    return(
        <div className="student-courses">
            <h2>Cac khoa hoc da dang ky</h2>
            <ul>
                {courses.map((course, index) => (
                    <li key={index}>{course}</li>
                ))}
            </ul>
            <div className="add-course-form">
                <input
                    type="text"
                    value={newCourseValue}
                    onChange={onInputChange}
                    placeholder="Nhập tên khóa học mới"
                />
                <button onClick={onAddCourse}>Thêm khóa học</button>
            </div>
        </div>
    );
}

export default StudentCourses;