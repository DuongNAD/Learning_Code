$(document).ready(function () {
    $("#userForm").on("submit", function (e) {
        e.preventDefault();
        let userID = $("#userId").val().trim();
        let password = $("#password").val().trim();
        let confirmPassword = $("#confirmPassword").val().trim();
        let email = $("#email").val().trim();
        let confirmEmail = $("#confirmEmail").val().trim();

        let emailRegex = /^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if (userID.length < 5) {
            alert("UserID must have at least 5 characters");
            return;
        }

        if (!isNaN(userID[0])) {
            alert("UserID must start with a letter (a-z/A-Z)");
            return;
        }
        if (password.length < 8) {
            alert("Password must have at least 8 characters")
            return;
        }
        function checkpassword(password) {
            let letter = false;
            let number = false;

            for (let i = 0; i < password.length; i++) {
                let char = password[i];

                if (!isNaN(char)) {
                    number = true;
                }
                else {
                    letter = true;
                }
                if (letter && number) {
                    return true;
                }
            }
            return false;
        }

        if (!checkpassword(password)) {
            alert("Password must include at least a letter and a number");
            return;
        }
        if (confirmPassword !== password) {
            alert("Password do not match");
            return;
        }

        if (!emailRegex.test(email)) {
            alert("Invalid email format");
            return;
        }

        if (confirmEmail !== email) {
            alert("Email do not match");
            return;
        }
        alert("Form submitted successfully");
        $("#userForm")[0].submit(); 
    });

    $("#reset").click(function (e) {
    });
});