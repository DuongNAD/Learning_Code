const users = [];


const hobbys = [
    { value: "", Text: "--Hobby--" },
    { value: "Nghe nhac", Text: "Nghe nhac" },
    { value: "Choi game", Text: "Choi game" },
    { value: "Da bong", Text: "Da bong" },
    { value: "An uong", Text: "An uong" },
    { value: "Chay bo", Text: "Chay bo" },
    { value: "Du lich", Text: "Du lich" },
];

const selectHobby = document.createElement("select")
selectHobby.id = "selectHobby";

hobbys.forEach(hobby => {
    const option = document.createElement("option");
    option.value = hobby.value;
    option.textContent = hobby.Text;
    selectHobby.appendChild(option);
});

document.getElementById("hobbySelectContainer").appendChild(selectHobby)

const genders = [
    { value: "", Text: "--Gender--" },
    { value: "Male", Text: "Male" },
    { value: "Female", Text: "Female" },
    { value: "Others", Text: "Others" },
];

const selectGender = document.createElement("select")
selectGender.id = "selectGender";

genders.forEach(gender => {
    const option = document.createElement("option");
    option.value = gender.value;
    option.textContent = gender.Text;
    selectGender.appendChild(option);
});

document.getElementById("genderSelectContainer").appendChild(selectGender);

const nameInput = document.getElementById("nameInput");
const emailInput = document.getElementById("emailInput");
const phoneInput = document.getElementById("phoneInput");
const ageInput = document.getElementById("ageInput");

document.getElementById("form-user").addEventListener("submit", function (e) {
    e.preventDefault();
    if (
        nameInput.value.trim() === "" ||
        selectGender.value.trim() === "" ||
        ageInput.value.trim() === "" ||
        emailInput.value.trim() === "" ||
        phoneInput.value.trim() === "" ||
        selectHobby.value.trim() === ""
    ) {
        alert("Vui lòng nhập đầy đủ thông tin!");
        return;
    }
    const newUser = {
        name: nameInput.value,
        gender: selectGender.value,
        age: ageInput.value,
        email: emailInput.value,
        phone: phoneInput.value,
        hobby: selectHobby.value,
    };

    users.push(newUser);
    addTableRow(newUser);
    console.log("Danh sach user", users);

    nameInput.value = "";
    selectGender.selectedIndex = 0;
    ageInput.value = "";
    emailInput.value = "";
    phoneInput.value = "";
    selectHobby.selectedIndex = 0;
});

function addTableRow(user) {
    const tableBody = document.getElementById("tableBody");
    const row = document.createElement("tr");
    row.innerHTML = `
    <td>${user.name}</td>
    <td>${user.gender}</td>
    <td>${user.age}</td>
    <td>${user.email}</td>
    <td>${user.phone}</td>
    <td>${user.hobby}</td>
    `
    tableBody.appendChild(row);
}
nameInput.addEventListener("input", function () {
    this.value = this.value.replace(/[^a-zA-Z\s]/g, '');
});
phoneInput.addEventListener("input", function () {
    this.value = this.value.replace(/\D/g, '');
});
ageInput.addEventListener("input", function () {
    this.value = this.value.replace(/\D/g, '');;
});