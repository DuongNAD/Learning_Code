<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php 
    $name = "Nguyen Anh Duong";
    $age = "19";
    $phone = "0967908595";
    $address = "Ha Noi";
    $img = "https://image.nhandan.vn/w800/Files/Images/2022/04/16/01a-1650105565608.jpg.webp";
    ?>

    <table border="1" style="width: 65%; margin: auto;">
        <caption><h2>Thong tin ca nhan</h2></caption>
        <tr>
            <td>Name</td>
            <td><?php echo $name; ?> </td>
        </tr>
        <tr>
            <td>Age</td>
            <td><?php echo $age; ?></td>
        </tr>
        <tr>
            <td>Phone</td>
            <td><?php echo $phone ?></td>
        </tr>
        <tr>
            <td>Address</td>
            <td><?php echo $address ?></td>
        </tr>
        <tr>
            <td>Image</td>
            <td> <img src="<?php echo $img?>" alt="#"></td>
        </tr>
    </table>
</body>
</html>