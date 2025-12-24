<?php

$cookie_expiration = time() + (7*24*60*60);

if($_SERVER['REQUEST_METHOD']=='POST'){
    $username = htmlspecialchars(trim($_POST['username']));
    setcookie("username",$username,$cookie_expiration);
}

if(isset($_COOKIE['username'])){
    $username = $_COOKIE['username'];
    $message = "Chào mừng trở lại, $username!";
}
else{
    $message = "Xin mời nhập tên của bạn.";
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2><?php echo $message ?></h2>
    <form action="" method="POST">
        <label for="username">Tên của bạn: </label>
        <input type="text name" name="username" id="username" required>
        <button type="submit" name="submit">Submit  </button>
    </form>
</body>
</html>