import React from "react";

function StudentInfo({name, studentId}){
    return(
        <div className="student-info">
            <h2>{name}</h2>
            <p>Ma sinh vien: {studentId}</p>
        </div>
    );
}

export default StudentInfo;