
const members = [];


const jobTypes = [
  { value: "", Text: "--Chon loai cong viec--" },
  { value: "Hoc HTML", Text: "Hoc HTML" },
  { value: "Hoc Js", Text: "Hoc Js" },
  { value: "Lam bai tap", Text: "Lam bai tap" },
  { value: "Lam viec nha", Text: "Lam viec nha" },
];

const selectElement = document.createElement("select");
selectElement.id = "jobSelect";

jobTypes.forEach(job => {
  const option = document.createElement("option");
  option.value = job.value;
  option.textContent = job.Text;
  selectElement.appendChild(option);
});

document.getElementById("jobSelectContainer").appendChild(selectElement);


const titleInput = document.getElementById("titleInput");
const startDateInput = document.getElementById("startDateInput");
const endDateInput = document.getElementById("endDateInput");


document.getElementById("todoForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const newMember = {
    title: titleInput.value,
    startDate: startDateInput.value,
    endDate: endDateInput.value,
    type: selectElement.value,
  };

  members.push(newMember);
  addTableRow(newMember);
  console.log("Danh sách member:", members);


  titleInput.value = "";
  startDateInput.value = "";
  endDateInput.value = "";
  selectElement.value = "";
});


function addTableRow(member) {
  const tableBody = document.getElementById("tableBody");
  const row = document.createElement("tr");
  row.innerHTML = `
    <td>${member.title}</td>
    <td>${member.startDate}</td>
    <td>${member.endDate}</td>
    <td>${member.type}</td>
  `;
  tableBody.appendChild(row);
}
