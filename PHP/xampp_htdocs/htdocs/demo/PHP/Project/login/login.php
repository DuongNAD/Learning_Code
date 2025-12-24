<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <title>Document</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <link rel="stylesheet" href="/demo/Project/login/login.css">
</head>

<body>
    <div class="form">
        <div class="title">
            <div class="name_shop">
                <a href="/demo/Project/login/login.php">DuongAnh Store <span><i class="fas fa-mobile-alt"></i></span></a>
            </div>
            <div class="help">
                <a href="/demo/Project/How I can help you/help.php">Bạn cần giúp gì</a>
            </div>
        </div>
        <div class="form_input">
            <div class="welcome">
                <img src="img1.jpg" alt="">

                <div class="text-overlay">
                    <h2>Welcome to website</h2>
                    <p>Smartphones are vital in modern life. They are key for communication, connecting us globally.
                        They
                        also provide instant access to information and entertainment. For many, they boost productivity
                        on
                        the go. Their versatility has transformed how we live and interact daily.</p>
                </div>
            </div>
            <div class="login_form">
                <form action="" class="input">
                    <div class="title_form">
                        <h2>USER LOGIN</h2>
                    </div>
                    <div class="username">
                        <span class="material-symbols-outlined">
                            account_circle
                        </span>
                        <input type="text" id="username" name="username" placeholder="Username">
                    </div>
                    <div class="password">
                        <span class="material-symbols-outlined">
                            lock
                        </span>
                        <input type="password" name="password" id="password" placeholder="Password">
                    </div>
                    <div class="remember-forgot">
                        <label class="remember-me">
                            <input type="checkbox" name="remember">
                            <span class="checkmark"></span>
                            Remember
                        </label>
                        <div class="forgot-password">
                            <a href="#">Forgot password?</a>
                        </div>
                    </div>
                    <div class="submit_form">
                        <button type="submit" class="submit">Login</button>
                    </div>
                </form>
            </div>
        </div>
        <div class="design">
            <p>Design by DuongAnh</p>
            <span><i class="fas fa-mobile-alt"></i></span></a>
        </div>
    </div>

    <?php
        session_start();

        $user_data = [
            'Duonganh' => '111111',
            'Hoangminh' =>'222222',
            'Lieuhong' => '333333',
            'Ngocminh' =>'444444',
        ];


        $admin_data = [
            'admin' => '123456',
        ];

    ?>
</body>

</html>