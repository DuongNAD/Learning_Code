<?php

$conn = new mysqli('localhost','root','','bookstore_db');
if($conn->connect_error) die("Ket noi that bai: " . $conn->connect_error);

$title = $_POST['title'];

$conn -> query("insert into orders (title) values('$title')");
$order_id = $conn->insert_id;

echo "Don hang dc tao thanh cong";
?>