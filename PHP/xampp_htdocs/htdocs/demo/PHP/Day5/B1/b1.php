<?php
session_start();

$Employee = [
    'NguyenVan_A' => 'abc123',
    'Tran_Thi_B' => 'B715',
    'Le_Van_C' => 'C_lo_vo_92',
    'Pham_ThiD' => 'De_PT_68',
    'Doan_Van_E' => 'E_v58',
    'admin' => '123456'
];

function _login($username, $password, $users_data)
{
    if (isset($users_data[$username]) && array_key_exists($username, $users_data) && $users_data[$username] == $password) {
        return true;
    }
    return false;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    if (isset($_POST['login'])) {
        $username = $_POST['username'];
        $password = $_POST['password'];

        $_SESSION['username'] = $username;

        $loginResult = _login($username, $password, $Employee);

        if ($loginResult) {
            $_SESSION['message'] = 'Đăng nhập thành công! Đang chuyển hướng...';
            $_SESSION['isSuccess'] = true;
            $_SESSION['last_action'] = 'login'; 
            header('Location: ' . $_SERVER['PHP_SELF']);
            exit();
        } else {
            $_SESSION['message'] = 'Đăng nhập thất bại. Tên đăng nhập hoặc mật khẩu không đúng.';
            $_SESSION['isSuccess'] = false;
        }
    }

    if (isset($_POST['register'])) {
        $reg_username = $_POST['reg_username'];
        $reg_email = $_POST['reg_email'];
        $reg_password = $_POST['reg_password'];
        $confirm_password = $_POST['confirm_password'];

        if ($reg_password !== $confirm_password) {
            $_SESSION['message'] = 'Mật khẩu và xác nhận mật khẩu không khớp.';
            $_SESSION['isSuccess'] = false;
            $_SESSION['show_register_form'] = true; 
        } elseif (array_key_exists($reg_username, $Employee)) {
            $_SESSION['message'] = 'Tên đăng nhập đã tồn tại. Vui lòng chọn tên khác.';
            $_SESSION['isSuccess'] = false;
            $_SESSION['show_register_form'] = true; 
        } else {
            $_SESSION['message'] = 'Đăng ký thành công! Vui lòng đăng nhập.';
            $_SESSION['isSuccess'] = true;
            $_SESSION['show_register_form'] = false; 
        }

        header('Location: ' . $_SERVER['PHP_SELF']);
        exit();
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đăng nhập / Đăng ký</title>
    <link rel="stylesheet" href="/demo/Day5/B1/b1.css">
    <link rel="stylesheet" href="/demo/Day5/B1/register.css">
    <style>
        .success-message {
            color: green;
            font-weight: bold;
            background-color: #e6ffe6;
            padding: 10px;
            margin-top: 15px;
            border: 1px solid green;
            border-radius: 5px;
            text-align: center;
        }

        .error-message {
            color: red;
            font-weight: bold;
            background-color: #ffe6e6;
            padding: 10px;
            margin-top: 15px;
            border: 1px solid red;
            border-radius: 5px;
            text-align: center;
        }

        .form-container {
            display: none;
        }

        .form-container.active {
            display: block;
        }

        /* CSS cho nút Register trông giống link */
        .switch-form-button {
            border: none;
            background-color: transparent;
            color: blue;
            cursor: pointer;
            padding: 0;
            text-decoration: underline;
        }

        .switch-form-button:hover {
            color: darkblue;
        }
    </style>
</head>

<body>
    <div class="login_form form-container <?php echo (!isset($_SESSION['show_register_form']) || !$_SESSION['show_register_form']) ? 'active' : ''; ?>" id="loginFormContainer">
        <div class="title">
            <h2>Login form</h2>
        </div>
        <div class="input">
            <form action="" method="POST" id="loginForm">
                <div class="username">
                    <label for="loginUsername">Username</label>
                    <input type="text" name="username" id="loginUsername" placeholder="Enter Username" required>
                </div>
                <div class="password">
                    <label for="loginPassword">Password</label>
                    <input type="password" name="password" id="loginPassword" placeholder="Enter password" required>
                </div>
                <div class="submit">
                    <button type="submit" name="login" class="login">Login</button>
                </div>
                <div class="register">
                    <p>Click here to</p>
                    <button type="button" id="showRegisterForm" class="switch-form-button">Register</button>
                </div>
            </form>
        </div>
    </div>

    <div class="login_form form-container <?php echo (isset($_SESSION['show_register_form']) && $_SESSION['show_register_form']) ? 'active' : ''; ?>" id="registerFormContainer">
        <div class="title">
            <h2>Register form</h2>
        </div>
        <div class="input">
            <form action="" method="POST" id="registerForm" class="register_input">
                <div class="username">
                    <label for="registerUsername">Username</label>
                    <input type="text" name="reg_username" id="registerUsername" placeholder="Enter Username" required>
                </div>
                <div class="email">
                    <label for="registerEmail">Email</label>
                    <input type="email" name="reg_email" id="registerEmail" placeholder="Enter Email" required>
                </div>
                <div class="password">
                    <label for="registerPassword">Password</label>
                    <input type="password" name="reg_password" id="registerPassword" placeholder="Enter password" required>
                </div>
                <div class="confirm-password">
                    <label for="confirmPassword">Confirm Password</label>
                    <input type="password" name="confirm_password" id="confirmPassword" placeholder="Confirm password" required>
                </div>
                <div class="submit">
                    <button type="submit" name="register" class="register_button">Register</button>
                </div>
                <div class="login-back">
                    <p>Already have an account?</p>
                    <button type="button" id="showLoginForm" class="switch-form-button">Login here</button>
                </div>
            </form>
        </div>
    </div>

    <?php
    if (isset($_SESSION['message'])) {
        $message = $_SESSION['message'];
        $isSuccess = $_SESSION['isSuccess'];

        echo '<div class="' . ($isSuccess ? 'success-message' : 'error-message') . '">' . htmlspecialchars($message) . '</div>';

        if ($isSuccess && isset($_SESSION['last_action']) && $_SESSION['last_action'] == 'login') {
            echo '<script>
                        setTimeout(function() {
                            window.location.href = "/demo/Day5/B1/b2.php"; // Chuyển hướng đến b2.php sau 1 giây
                        }, 1000);
                    </script>';
        }

        unset($_SESSION['message']);
        unset($_SESSION['isSuccess']);
        unset($_SESSION['last_action']);
    }
    ?>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const loginFormContainer = document.getElementById('loginFormContainer');
            const registerFormContainer = document.getElementById('registerFormContainer');
            const showRegisterFormBtn = document.getElementById('showRegisterForm');
            const showLoginFormBtn = document.getElementById('showLoginForm');

            function showForm(formToShow) {
                if (formToShow === 'login') {
                    loginFormContainer.classList.add('active');
                    registerFormContainer.classList.remove('active');
                } else if (formToShow === 'register') {
                    loginFormContainer.classList.remove('active');
                    registerFormContainer.classList.add('active');
                }
            }

            if (showRegisterFormBtn) {
                showRegisterFormBtn.addEventListener('click', function() {
                    showForm('register');
                });
            }

            if (showLoginFormBtn) {
                showLoginFormBtn.addEventListener('click', function() {
                    showForm('login');
                });
            }
        });
    </script>
</body>

</html>