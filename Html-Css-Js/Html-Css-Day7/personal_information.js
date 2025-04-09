
const name = "Nguyen Anh Duong";
const gender = "Male";
const age = "18";
const address = "Thach That - Ha Noi - Viet Nam";
const phone_number = "0967 908 595";

console.log("================ PERSONAL INFORMATION ===============");
console.log(`Name: ${name}`);
console.log(`gender: ${gender}`);
console.log(`age: ${age}`);
console.log(`address: ${address}`);
console.log(`phone_number: ${phone_number}`);

document.getElementById("info").innerHTML = `
    <strong>Name:</strong> ${name}<br>
    <strong>Gender:</strong> ${gender}<br>
    <strong>Age:</strong> ${age}<br>
    <strong>Address:</strong> ${address}<br>
    <strong>Phone Number:</strong> ${phone_number}
`;