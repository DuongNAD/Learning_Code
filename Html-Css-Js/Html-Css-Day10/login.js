document.getElementById("loginForm").addEventListener("submit", function(e){
    e.preventDefault();

    const usernameInput = document.getElementById("username");
    const passwordInput = document.getElementById("password")

    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;

    if (user === "admin" && pass == "123456"){
        window.location.href = "B10.html";
    }
    else {
        alert("Mật khẩu hoặc tên đăng nhập sai!\nMời nhập lại");

        usernameInput.value="";
        passwordInput.value="";
    }

    usernameInput.focus();
});