<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="titel"><h2>Kiem tra Chan Le</h2></div>
    <div>
        <form method="POST" action="">
            <div>
                <label for="nhap">Nhap</label>
                <input type="number" id="nhap" name="nhap" required>
            </div>
            <div>
                <label for="ketqua">Ket qua</label>
                <input type="text" name="ketqua" id="ketqua" readonly>
            </div>
            <div>
                <button type="submit" name="kiemtra">Kiem tra</button>
            </div>
        </form>
    </div>
    <?php
        
        if($_SERVER["REQUEST_METHOD"]=="POST" && isset($_POST)){$input = $_POST['nhap'];
            $input = $_POST['nhap'];

            if($input % 2 == 0){
                $check = "$input la so chan";
            }
            else{
                $check = "$input la so le";
            }
        echo "<script> document.getElementById('ketqua').value ='$check';</script>";
        }
    ?>
</body>
</html>