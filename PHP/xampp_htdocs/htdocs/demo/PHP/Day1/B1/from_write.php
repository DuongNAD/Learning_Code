<?php
session_start();
if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['tinh'])){
    $chieudai = $_POST['dai'];
    $chieurong = $_POST['rong'];

    $dientich = $chieudai * $chieurong;

    $_SESSION["dientich"] = $dientich;
    header("Location: b1.php"); 
    exit();
} else {
    header("Location: b1.php"); 
    exit();
}
?>