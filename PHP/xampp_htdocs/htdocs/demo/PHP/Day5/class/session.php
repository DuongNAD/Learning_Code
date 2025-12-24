<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <a href="get_session.php">Show</a>
    </div>
    
    <?php
    session_start();
        $_SESSION['name'] ='Nguyen Anh Duong';
        $_SESSION['profile'] = ['name' => 'Nguyen Anh Duong', 'email' => 'duonganh2006@gmail.com'];
    ?>
</body>
</html>