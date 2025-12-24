<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="" method="POST">
        So a: <input type="text" name="so1" required>
        so b: <input type="text" name="so2" required>
        <input type="reset" name="submit" value="Xóa">
        <input type="submit" name="submit" value="Tính">
    </form>

    <?php
    function is_number($value)
    {
        return is_numeric($value); 
    }

    function cong_hai_so($a, $b)
    {
        return $a + $b;
    }


    if($_SERVER['REQUEST_METHOD'] == 'POST'){
        $a = $_POST['so1'] ?? ''; 
        $b = $_POST['so2'] ?? '';
        if(is_number($a) && is_number($b)){
            $ketqua = cong_hai_so((float)$a, (float)$b); 
            echo $ketqua;
        }
        else{
            echo "Không hợp lệ: Vui lòng nhập số.";
        }
    }
    ?>
</body>

</html>