<?php
session_start();

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="b1.css">

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
    </style>
</head>

<body>
    <div class="login_form">
        <div class="title">
            <h2>Login form</h2>
        </div>
        <div class="input">
            <form action="" method="POST">
                <div class="username">
                    <label for="username">Username</label>
                    <input type="text" name="username" id="username" placeholder="Enter Username" required>
                </div>
                <div class="password">
                    <label for="password">Password</label>
                    <input type="password" name="password" id="password"  placeholder="Enter password" required>
                </div>
                <div class="submit">
                    <button type="submit" name="login" class="login">Login</button>
                </div>
                <div class="register">
                    <p>Click here to</p>
                    <a href="giohang.php">Register</a>
                </div>
            </form>
        </div>
    </div>


    <?php
    
    $message ='';
    $isSuccess = false;
    function _login($username, $password)
    {
        global $Employee;
        if ( isset($Employee[$username]) && array_key_exists($username, $Employee)  && $Employee[$username] == $password ) {
            return true;
        }
        return false;
    }

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
       
        $Employee = [
            'NguyenVan_A' => 'abc123',
            'Tran_Thi_B' => 'B715',
            'Le_Van_C' => 'C_lo_vo_92',
            'Pham_ThiD' => 'De_PT_68',
            'Doan_Van_E' => 'E_v58',
            'admin'=>'123456'
        ];
        $username = $_POST['username']; 
        $_SESSION['username'] = $username;

        $password = $_POST['password'];
        $loginResult = _login($username, $password);

        if($loginResult){
            $message = 'Đăng nhập thành công!';
            echo $_SESSION['username'] ;
            $isSuccess = true;
            header('Location: giohang.php');
           
            exit();
            
        }
        else{
            $message = 'Đăng nhập thất bại. Tên đăng nhập hoặc mật khẩu không đúng.';
            $isSuccess = false;
        }
    }
    if (!empty($message)) {

        echo '<div class="' . ($isSuccess ? 'success-message' : 'error-message') . '">' . $message . '</div>';
    }
    
    ?>
</body>

</html>