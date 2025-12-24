<?php

$host = "localhost";
$user = "root";
$password = "";
$database = "quan_ly_sinh_vien";

$conn = mysqli_connect($host, $user, $password, $database);

if (!$conn) {
    die("Kết nối thất bại: " . mysqli_connect_error());
} else {
    echo "---> Kết nối thành công csdl: " . $database;
}

?>
