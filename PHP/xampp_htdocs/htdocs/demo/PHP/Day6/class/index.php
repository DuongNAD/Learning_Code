<?php

require 'person.php';

$person = null;
$message = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
        $name = htmlspecialchars($_POST['name']);
        $age = intval($_POST['age']);
        $email = htmlspecialchars($_POST['email']);

        if (empty($name) || empty($email) || $age < 0) {
            throw new Exception("Vui lòng nhập đầy đủ và chính xác thông tin");
        }

        $person = new person($name, $age, $email);

        $message = "Thông tin đã được lưu thành công!";
    } catch (Exception $e) {
        $message = "Lỗi: " . $e->getMessage();
    }
}

?>

<!DOCTYPE html>
<html lang="vi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    ` <h1>Nhập thông tin cá nhân</h1>
    <form action="" method="POST">
        <label for="">Họ và tên: </label>
        <input type="text" id="name" name="name" value="<?= isset($_POST['name']) ? htmlspecialchars($_POST['name']) : '' ?>" required><br><br>

        <label for="age">Tuổi: </label>
        <input type="number" id="age" name="age" value="<?= isset($_POST['age']) ? htmlspecialchars($_POST['age']) : '' ?>" required><br><br>

        <label for="email">Email: </label>
        <input type="email" id="email" name="email" value="<?= isset($_POST['email']) ? htmlspecialchars($_POST['email']) : '' ?>" required><br><br>
    
        <button type="submit">Lưu thông tin</button>
    </form>
    <hr>

    <p style="color: <?= strpos($message, 'Lỗi') !== false ? 'red' : 'green'; ?>;">
        <?= htmlspecialchars($message) ?>
    </p>

    <?php if ($person): ?>
        <h2>Thông tin đăng nhập: </h2>
        <p><strong>Họ và tên: </strong> <?= htmlspecialchars($person->getName()) ?></p>
        <p><strong>Tuổi: </strong> <?= htmlspecialchars($person->getAge()) ?></p>
        <p><strong>Email: </strong> <?= htmlspecialchars($person->getEmail()) ?></p>
    <?php endif; ?>


</body>

</html>