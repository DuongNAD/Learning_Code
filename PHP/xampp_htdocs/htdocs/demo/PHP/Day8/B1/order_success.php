<?php
include 'header.php';
?>

<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Đặt hàng thành công</title>
    <style>
        .success-container {
            width: 60%;
            margin: 50px auto;
            padding: 40px;
            text-align: center;
            border: 1px solid #d4edda;
            background-color: #f7fdf9;
            border-radius: 8px;
            font-family: Arial, sans-serif;
            color: #155724;
        }
        .success-container h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .success-container p {
            font-size: 1.1em;
            line-height: 1.6;
        }
        .success-container .back-to-home {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 25px;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-size: 1.1em;
            transition: background-color 0.3s;
        }
        .success-container .back-to-home:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <div class="success-container">
        <h1>Đặt Hàng Thành Công!</h1>
        <p>Cảm ơn bạn đã tin tưởng và mua hàng tại cửa hàng của chúng tôi.</p>
        <p>Chúng tôi sẽ liên hệ với bạn để xác nhận đơn hàng trong thời gian sớm nhất.</p>
        <a href="product.php" class="back-to-home">Tiếp Tục Mua Sắm</a>
    </div>

</body>
</html>

<?php
include 'footer.php';
?>