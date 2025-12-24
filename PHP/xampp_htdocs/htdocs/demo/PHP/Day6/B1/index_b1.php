<?php

require 'b1.php';
session_start();
$product_list = null;
$message = "";

if (!isset($_SESSION['products'])) {
    $_SESSION['products'] = [];
}
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['addProduct'])) {
    try {
        $id_raw = $_POST['productId'] ?? '';
        $name_raw = $_POST['productName'] ?? '';
        $brand_raw = $_POST['brandName'] ?? '';
        $price_raw = $_POST['productPrice'] ?? '';
        $total_quantity_raw = $_POST['stockQuantity'] ?? '';

        $id_val = intval($id_raw);
        $name_val = trim($name_raw);
        $brand_val = trim($brand_raw);
        $price_val = floatval($price_raw);
        $total_quantity_val = intval($total_quantity_raw);

        if ($id_val <= 0) {
            throw new Exception('Mã sản phẩm phải là số dương.');
        }
        if (empty($name_val)) {
            throw new Exception('Tên sản phẩm không được để trống.');
        }
        if (empty($brand_val)) {
            throw new Exception('Thương hiệu không được để trống.');
        }
        if ($price_val < 0) {
            throw new Exception('Giá sản phẩm không được âm.');
        }
        if ($total_quantity_val < 0) {
            throw new Exception('Số lượng tồn kho không được âm.');
        }

        foreach ($_SESSION['products'] as $existing_product) {
            if ($existing_product->getProductId() == $id_val) { 
                throw new Exception("Mã sản phẩm '$id_val' đã tồn tại. Vui lòng nhập mã khác.");
            }
        }

        $product_to_add = new Product_list($id_val, $name_val, $brand_val, $price_val, $total_quantity_val);
        $_SESSION['products'][] = $product_to_add; 
        $message = "Thêm sản phẩm thành công!";
    } catch (Exception $e) {
        $message = 'Lỗi: ' . $e->getMessage();
    }
}

$all_products = $_SESSION['products'];
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }

        .container>div {
            background-color: #fff;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        h1,
        h2 {
            color: #333;
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        input[type="text"],
        input[type="number"] {
            width: calc(100% - 22px);
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }

        button {
            background-color: #5cb85c;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #4cae4c;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
    <title>Document</title>
</head>

<body>
    <div>
        <div>
            <h1>Quản lý sản phẩm</h1>
        </div>
    </div>

    <?php if (!empty($message)): ?>
        <div class="message <?= strpos($message, 'Lỗi') !== false ? 'error' : 'success'; ?>">
            <?= htmlspecialchars($message) ?>
        </div>
    <?php endif; ?>

    <div class="container">
        <div class="add-product">
            <h2>Thêm sản phẩm</h2>
            <form action="" method="POST">
                <input type="number" id="productId" name="productId" placeholder="Mã sản phẩm">
                <input type="text" id="productName" name="productName" placeholder="Tên sản phẩm">
                <input type="text" id="brandName" name="brandName" placeholder="Thương hiệu">
                <input type="number" id="productPrice" name="productPrice" placeholder="Giá">
                <input type="text" id="stockQuantity" name="stockQuantity" placeholder="Tồn kho">
                <button type="submit" name="addProduct">Thêm</button>
            </form>
        </div>
        <div class="sell-product">
            <h2>Bán sản phẩm</h2>
            <form action="" method="POST">
                <input type="text" id="sell-productId" name="sell-productId" placeholder="Mã sản phẩm">
                <input type="number" id="product-quantity" name="product-quantity" placeholder="Số lượng">
                <button type="submit" class="sell" name="sellProduct">Bán</button>
            </form>
        </div>
        <div class="list-product">
            <h2>Danh sách sản phẩm</h2>
            <table>
                <thead>
                    <tr>
                        <th>Mã sản phẩm</th>
                        <th>Tên sản phẩm</th>
                        <th>Thương hiệu</th>
                        <th>Giá</th>
                        <th>Tồn kho</th>
                        <th>Trạng thái</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (!empty($all_products)): ?>
                        <?php foreach ($all_products as $product_item): ?>
                            <tr>
                                <td><?= htmlspecialchars($product_item->getProductId()) ?></td>
                                <td><?= htmlspecialchars($product_item->getProductName()) ?></td>
                                <td><?= htmlspecialchars($product_item->getBrandName()) ?></td>
                                <td><?= htmlspecialchars(number_format($product_item->getProductPrice(), 2, '.', ',')) ?></td>
                                <td><?= htmlspecialchars($product_item->getStockQuantity()) ?></td>
                                <td><?= htmlspecialchars($product_item->getStatus()) ?></td>
                            </tr>
                        <?php endforeach; ?>
                    <?php else: ?>
                        <tr>
                            <td colspan="6" style="text-align: center;">Chưa có thông tin sản phẩm để hiển thị.</td>
                        </tr>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>
    </div>
</body>

</html>