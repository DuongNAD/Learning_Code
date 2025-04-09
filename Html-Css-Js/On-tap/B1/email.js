$(document).ready(function () {
    let dataArray = [];

    $("#loginForm").submit(function (event) {
        event.preventDefault();
        let email = $("#email").val().trim(); let password = $("#password").val().trim();
        $("#errorMsg").text("");

        if (email === "") {
            $("#errorMsg").text("⚠ Vui lòng nhập Email!");
            return;
        }
        let atIndex = email.indexOf("@");
        if (atIndex === -1 || atIndex !== email.lastIndexOf("@")) {
            $("#errorMsg").text("⚠ Email phải chứa đúng một '@'!");
            return;
        }

        let localPart = email.substring(0, atIndex);
        if (localPart.length === 0) {
            $("#errorMsg").text("⚠ Phần trước '@' không được để trống!");
            return;
        }
        let firstChar = localPart.charAt(0);
        if (!((firstChar >= 'A' && firstChar <= 'Z') ||
            (firstChar >= 'a' && firstChar <= 'z') ||
            (firstChar >= '0' && firstChar <= '9'))) {
            $("#errorMsg").text("⚠ Phần trước '@' phải bắt đầu bằng chữ cái hoặc số!");
            return;
        }
        let allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._%+-";
        for (let i = 0; i < localPart.length; i++) {
            if (allowedChars.indexOf(localPart.charAt(i)) === -1) {
                $("#errorMsg").text("⚠ Phần trước '@' chứa ký tự không hợp lệ!");
                return;
            }
        }
        let domainPart = email.substring(atIndex + 1);
        if (domainPart === "") {
            $("#errorMsg").text("⚠ Phần sau '@' không được để trống!");
            return;
        }

        let dotIndex = domainPart.lastIndexOf(".");
        if (dotIndex === -1) {
            $("#errorMsg").text("⚠ Phần sau '@' phải chứa dấu '.'!");
            return;
        }

        let tld = domainPart.substring(dotIndex + 1);
        if (tld.length < 2) {
            $("#errorMsg").text("⚠ TLD phải có ít nhất 2 ký tự!");
            return;
        }
        for (let i = 0; i < tld.length; i++) {
            let c = tld.charAt(i);
            if (!((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z'))) {
                $("#errorMsg").text("⚠ TLD chỉ được chứa chữ cái!");
                return;
            }
        }

        if (dataArray.includes(email)) {
            $("#errorMsg").text("⚠ Email đã tồn tại!");
            return;
        }
        if (password === "") {
            $("#errorMsg").text("⚠ Vui lòng nhập mật khẩu!");
            return;
        }
        if (password.length < 6 || password.length > 12) {
            $("#errorMsg").text("⚠ Mật khẩu phải từ 6 đến 12 ký tự!");
            return;
        }
        if (!$('#checkbox').is(':checked')) {
            $('#errorMsg').text('⚠ Bạn cần đồng ý với điều khoản trước khi tiếp tục!');
            return;
        }

        $("#errorMsg").text("✅ Tạo Email thành công")
        dataArray.push(email);
        $("#email").val("");
        $("#password").val("");
        displayEmails()

    });
});