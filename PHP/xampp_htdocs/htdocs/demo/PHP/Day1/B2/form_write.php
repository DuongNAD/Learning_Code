<?php
session_start();
    if($_SERVER["REQUEST_METHOD"] == "POST"  &&  isset($_POST['tinh'])){
        
        $bankinh = $_POST['bankinh'];

        if($bankinh >0){

            $chuvi = 2 * $bankinh * M_PI;
            $dientich = $bankinh * $bankinh * M_PI;

            $_SESSION['chuvi'] = round($chuvi,2);
            $_SESSION['dientich'] = round($dientich,2);
    }
        else {
            $_SESSION['error_message'] = "Bán kính phải là một số dương.";
            unset($_SESSION['chuvi']);
            unset($_SESSION['dientich']);
        }
    header("Location: b2.php");
    exit();
    }
    else{
    header("Location: b2.php");
    exit();
}
?>