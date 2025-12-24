import React, { use, useState } from "react";
import StudentInfo from "./StudentInfo";
import StudentCourses from './StudentCourses';

function StudentProfile() {
    const [student] = useState({
        name: 'Nguyen Van A',
        studentId: 1
    });
    const [courses, setCourses] = useState([
        'Toán rời rạc',
        'Giải tích 1',
        'Lập trình nâng cao'
    ]);

    const [newCourse, setNewCourse] = useState('');
    const handleInputChange = (e) => {
        setNewCourse(e.target.value);
    };

    const handleAddCourse = () => {
        if (newCourse.trim() !== '') {
            setCourses([...courses, newCourse]);
            setNewCourse('');
        }
    };

    return (
        <div className="student-profile">
            <StudentInfo name={student.name} studentId={student.studentId} />
            <StudentCourses
                courses={courses}
                newCourseValue={newCourse}
                onInputChange={handleInputChange}
                onAddCourse={handleAddCourse}
            />
        </div>
    );

}

export default StudentProfile;