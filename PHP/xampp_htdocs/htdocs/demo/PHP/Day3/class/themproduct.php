<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thêm sản phẩm mới</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 500px;
        }
        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 25px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: bold;
        }
        .form-group input[type="text"],
        .form-group input[type="number"] {
            width: calc(100% - 20px); /* Tính toán để trừ padding */
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box; /* Đảm bảo padding không làm tăng chiều rộng tổng thể */
            font-size: 16px;
        }
        .form-group input:focus {
            border-color: #007bff;
            outline: none;
        }
        .btn-submit {
            width: 100%;
            padding: 12px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 18px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .btn-submit:hover {
            background-color: #218838;
        }
        .error-message {
            color: red;
            margin-bottom: 15px;
            text-align: center;
        }
        .success-message {
            color: green;
            margin-bottom: 15px;
            text-align: center;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>Thêm sản phẩm mới</h2>

        <?php

        $error = [];
        $success = '';

        $product = [];

        if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add_product'])){
            $new_name = trim($_POST['name'] ?? '');
            $new_image = trim($_POST['img'] ?? '');
            $new_price = trim($_POST['price'] ?? '');
            $new_sale_price = trim($_POST['sale_price'] ?? '');

            if (empty($new_name)) {
                $error[] = "Tên sản phẩm không được để trống.";
            }
            if (empty($new_price) || !is_numeric($new_price) || $new_price < 0) {
                $error[] = "Giá sản phẩm phải là số dương và không được để trống.";
            }
            if (!empty($new_sale_price) && (!is_numeric($new_sale_price) || $new_sale_price < 0)) {
                $error[] = "Giá khuyến mãi phải là số dương.";
            }
            if (!empty($new_price) && !empty($new_sale_price) && $new_sale_price > $new_price) {
                $error[] = "Giá khuyến mãi không được lớn hơn giá gốc.";
            }

            if (empty($error)) {
                $new_product = [
                    'name' => $new_name,
                    'image' => $new_image,
                    'price' => $new_price,
                    'sale_price' => $new_sale_price,
                ];

                array_push($product, $new_product); 
                $success = "Thêm sản phẩm thành công: " . $new_name;


                $_POST = [];
            }
        }


        if (!empty($error)) {
            echo '<div class="error-message">';
            foreach ($error as $err) {
                echo '<p>' . htmlspecialchars($err) . '</p>';
            }
            echo '</div>';
        }

        if (!empty($success)) {
            echo '<div class="success-message">';
            echo '<p>' . htmlspecialchars($success) . '</p>';
            echo '</div>';
        }
        ?>

        <form action="" method="POST">
            <div class="form-group">
                <label for="name">Tên sản phẩm:</label>
                <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($_POST['name'] ?? ''); ?>" required>
            </div>
            <div class="form-group">
                <label for="img">URL hình ảnh:</label>
                <input type="text" id="img" name="img" value="<?php echo htmlspecialchars($_POST['img'] ?? ''); ?>">
            </div>
            <div class="form-group">
                <label for="price">Giá:</label>
                <input type="number" id="price" name="price" step="0.01" value="<?php echo htmlspecialchars($_POST['price'] ?? ''); ?>" required>
            </div>
            <div class="form-group">
                <label for="sale_price">Giá khuyến mãi (nếu có):</label>
                <input type="number" id="sale_price" name="sale_price" step="0.01" value="<?php echo htmlspecialchars($_POST['sale_price'] ?? ''); ?>">
            </div>
            <button type="submit" name="add_product" class="btn-submit">Thêm sản phẩm</button>
        </form>
    </div>

</body>
</html>