<?php
session_start();
$name = isset($_SESSION['username']) ? $_SESSION['username']: '';
$products_data = [
    'product1' => ['name' => 'Điện thoại Tel', 'price' => 150000, 'image_path' => 'img/tel.jpg'],
    'product2' => ['name' => 'Tai nghe Nak', 'price' => 500000, 'image_path' => 'img/nak.jpg'],
    'product3' => ['name' => 'Sạc dự phòng Raz', 'price' => 210000, 'image_path' => 'img/raz.jpg'],
    'product4' => ['name' => 'Loa Ryo', 'price' => 210000, 'image_path' => 'img/ryo.jpg'],
];

if(!isset($_SESSION['cart'])){
    $_SESSION['cart'] = [
        'product1' => 2,
        'product2' => 3,
        'product3' => 1,
        'product4' => 2,
    ];
}

$total_quantity = 0;
$total_amount = 0;

if(isset($_SESSION['cart']) && !empty($_SESSION['cart'])){
    
}

if (!empty($cart_items)) {
    foreach ($cart_items as $product_id => $quantity) {
        if (isset($products_data[$product_id])) { 
            $item_data = $products_data[$product_id];
            $total_quantity += $quantity;
            $total_amount += $item_data['price'] * $quantity;
        }

    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Giỏ hàng của bạn</title>
    <style>

        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f8f8f8;
        }

        h2 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }

        .cart-table {
            width: 80%;
            border-collapse: collapse;
            margin: 20px auto;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            background-color: #fff;
        }

        .cart-table thead {
            background-color: #007bff;
            color: white;
        }

        .cart-table th,
        .cart-table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }

        .cart-table th {
            text-align: center;
            font-weight: bold;
        }

         .cart-table tbody tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .cart-table tbody tr:hover {
             background-color: #e9e9e9;
        }


        .cart-table img {
            max-width: 50px;
            height: auto;
            display: block;
            margin: 0 auto;
            border-radius: 4px;
        }

        .cart-summary {
            width: 80%;
            margin: 10px auto;
            padding: 15px;
            border: 1px solid #ddd;
            background-color: #fff;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        .cart-summary p {
            margin: 8px 0;
            font-size: 1.1em;
            color: #333;
        }

        .cart-summary strong {
            color: #000;
        }

    </style>
</head>
<body>
    <h2> <?php echo $name ?></h2>
    <h2>Giỏ hàng</h2>

    <table class="cart-table">
        <thead>
            <tr>
                <th>Ảnh</th>
                <th>Tên Sản Phẩm</th>
                <th>Giá</th>
                <th>Số Lượng</th>
                <th>Tổng tiền</th>
                </tr>
        </thead>
        <tbody>

        <?php

            if (!empty($cart_items)) { // Chỉ lặp nếu giỏ hàng không rỗng
                foreach ($cart_items as $product_id => $quantity) {
                    if (isset($products_data[$product_id])) { // Cần biến $products_data
                        $item_data = $products_data[$product_id]; // Lấy dữ liệu chi tiết sản phẩm
                        $row_total = $item_data['price'] * $quantity; // Tính tổng tiền cho dòng này

                        // --- In ra hàng (<tr>) cho sản phẩm hiện tại ---
        ?>
            <tr>
                <td><img src="<?php echo $item_data['image_path']; ?>" alt="<?php echo $item_data['name']; ?>"></td>
                <td><?php echo $item_data['name']; ?></td>
                <td><?php echo number_format($item_data['price'], 0, ',', '.'); ?> VND</td>
                <td><?php echo $quantity; ?></td>
                <td><?php echo number_format($row_total, 0, ',', '.'); ?> VND</td>
                </tr>
        <?php
                    }
                    // Nếu sản phẩm không tồn tại trong $products_data, hàng này sẽ không được in ra
                }
            } else {
                // --- Hiển thị thông báo nếu giỏ hàng trống ---
        ?>
            <tr>
                <td colspan="5" style="text-align:center;">Giỏ hàng của bạn đang trống.</td>
            </tr>
        <?php
            }
        ?>

        </tbody>
    </table>

    <div class="cart-summary">
        <?php
            // --- Vị trí để bạn hiển thị tổng số lượng và tổng tiền ---
            // Biến $total_quantity và $total_amount đã được tính toán ở phần đầu file.
        ?>
        <p><strong>Tổng số lượng:</strong> <?php echo $total_quantity; ?></p>
        <p><strong>Tổng tiền:</strong> <?php echo number_format($total_amount, 0, ',', '.'); ?> VND</p>
    </div>

</body>
</html>