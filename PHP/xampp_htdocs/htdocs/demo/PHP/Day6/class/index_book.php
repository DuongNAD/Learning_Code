<?php

require 'book.php';

$book = null;
$message = "";

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    try {
        $id = intval($_POST['id']);
        $title = htmlspecialchars($_POST['title']);
        $price = intval($_POST['price']);
        $image = htmlspecialchars($_POST['img']);

        if (empty($title) || empty($image) || $id <= 0 || $price < 0) {
            throw new Exception("Vui lòng nhập đầy đủ và chính xác thông tin");
        }

        $book = new book($id, $title, $price, $image);

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
    ` <h1>Nhập thông tin sách</h1>
    <form action="" method="POST">
        <label for="">Id: </label>
        <input type="number" id="id" name="id" value="<?= isset($_POST['id']) ? htmlspecialchars($_POST['id']) : '' ?>" required><br><br>

        <label for="title">Mô tả: </label>
        <input type="text" id="title" name="title" value="<?= isset($_POST['title']) ? htmlspecialchars($_POST['title']) : '' ?>" required><br><br>

        <label for="price">Giá sách: </label>
        <input type="price" id="price" name="price" value="<?= isset($_POST['price']) ? htmlspecialchars($_POST['price']) : '' ?>" required><br><br>

        <label for="img">Ảnh: </label>
        <input type="text" id="img" name="img" value="<?= isset($_POST['img']) ? htmlspecialchars($_POST['img']) : '' ?>" required><br><br>

        <button type="submit">Lưu thông tin</button>
    </form>
    <hr>

    <p style="color: <?= strpos($message, 'Lỗi') !== false ? 'red' : 'green'; ?>;">
        <?= htmlspecialchars($message) ?>
    </p>

    <?php if ($book): ?>
        <h2>Thông tin sách </h2>
        <p><strong>Id: </strong> <?= htmlspecialchars($book->getId()) ?></p>
        <p><strong>Title: </strong> <?= htmlspecialchars($book->getTitle()) ?></p>
        <p><strong>Price: </strong> <?= htmlspecialchars($book->getPrice()) ?></p>
        <img src="<?= htmlspecialchars($book->getImage()) ?>" alt="<?= htmlspecialchars($book->getTitle()) ?>">
    <?php endif; ?>

</body>

</html>