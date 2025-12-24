<?php
$host = 'localhost';
$user ='root';
$password = '';
$database = 'bookstore_db';

$conn = mysqli_connect($host, $user, $password, $database);

if(!$conn){
    die("Kết nối thất bại: " . mysqli_connect_error());
}
?>