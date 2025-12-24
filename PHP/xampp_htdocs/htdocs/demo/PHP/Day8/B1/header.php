<?php
session_start();
include 'connect.php'; 
?>
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cửa hàng sách</title>
</head>
<body>
    <header>
        <h1>Cửa hàng sách</h1>
        <nav>
            <a href="bookstore_input.php">Thêm sản phẩm</a>
            <a href="product.php">Danh sách sản phẩm</a>
            <a href="cart.php">Giỏ hàng</a>
        </nav>
    </header>