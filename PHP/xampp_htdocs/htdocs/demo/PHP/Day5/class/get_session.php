<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
    session_start();
    $name = isset($_SESSION['name']) ? $_SESSION['name'] : '';
    $profile = isset($_SESSION['profile']) ? $_SESSION['profile'] :'';
    ?>

    <h1>Hello <?php echo $name; ?></h1>
    <h2>Name: <?php echo $profile['name'] ?></h2>
    <h2>Email: <?php echo $profile['email'] ?></h2>
</body>
</html>