const students = [
    {
        IdentityCode: "100", 
        name: "Nguyen Anh Duong",
        age: 18,
        Email: "Duong100@gmail.com",
    },
    {
        IdentityCode: "101", 
        name: "Nguyen Thi Phuong Anh",
        age: 23,
        Email: "PAnh101@gmail.com",
    },
    {
        IdentityCode: "102",
        name: "Duong Manh Dat",
        age: 19,
        Email: "Dat102@gmail.com",
    },
    {
        IdentityCode: "103",
        name: "Li Duc Khanh",
        age: 29,
        Email: "Khanh103@gmail.com",
    }
];

function displayStudents(students, containerId) {
    const container = document.getElementById(containerId);
    const table = document.createElement("table");
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    const headers = [
        "IdentityCode", 
        "Name",
        "age",
        "Email"
    ];

    headers.forEach(headerText => {
        const th = document.createElement("th");
        th.textContent = headerText;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");

    students.forEach(student => {
        const row = document.createElement("tr");

        const tdIdentityCode = document.createElement("td");
        tdIdentityCode.textContent = student.IdentityCode;
        tdIdentityCode.classList.add("col-id");
        row.appendChild(tdIdentityCode);
        
        const tdName = document.createElement("td");
        tdName.textContent = student.name;
        tdName.classList.add("col-name");
        row.appendChild(tdName);



        const tdAge = document.createElement("td");
        tdAge.textContent = student.age;
        tdAge.classList.add("col-age");
        row.appendChild(tdAge);

        const tdEmail = document.createElement("td");
        tdEmail.textContent = student.Email;
        tdEmail.classList.add("col-email");
        row.appendChild(tdEmail);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    container.appendChild(table);
}

displayStudents(students, "studentTable");
displayStudents(students.filter(student => student.age > 20), "listAbove20");
displayStudents(students.filter(student => student.IdentityCode), "listWithID");