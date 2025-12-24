<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Hiển thị ảnh</h2>
    <table>
        <thead>
            <tr>
                <th>STT</th>
                <th>Ảnh</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            <?php
                $img = "img/";
                $number_img = 8;

                for ($i =1;$i <= $number_img;$i++){
                    $name = "anh" . $i . ".jpg";
                    $img_path = $img . $name;
                
            ?>
            <tr>
                <td>
                    <?php echo $i ?>
                </td>
                <td>
                    <img src="<?php echo $img_path; ?>" alt="Hình ảnh <?php echo $i; ?>" width="150" height="100">
                </td>
                <td>
                    <?php echo "Hình ảnh" . $i ?>
                </td>
            </tr>
            <?php
                }
                ?>
        </tbody>
    </table>
</body>
</html>