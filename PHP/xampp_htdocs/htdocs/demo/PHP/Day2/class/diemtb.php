<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div class="titel"><h2>Kiem tra hanh kiem</h2></div>
    <div>
        <form method="POST" action="">
            <div>
                <label for="toan">Nhap</label>
                <input type="number" id="toan" name="toan" required>
            </div>
            <div>
                <label for="ly">Nhap</label>
                <input type="number" id="ly" name="ly" required>
            </div>
            <div>
                <label for="hoa">Nhap</label>
                <input type="number" id="hoa" name="hoa" required>
            </div>
            <div>
                <label for="ketqua">Hanh kiem</label>
                <input type="text" name="ketqua" id="ketqua" readonly>
            </div>
            <div>
                <button type="submit" name="kiemtra">Kiem tra</button>
            </div>
        </form>
    </div>
    <?php

        if($_SERVER["REQUEST_METHOD"]=="POST" && isset($_POST['kiemtra'])){
            $toan = $_POST['toan'];
            $ly = $_POST['ly'];
            $hoa = $_POST['hoa'];

            $hanhkiem =($toan +$ly + $hoa)/3;

            if($hanhkiem<=5){
                $xeploai = "Kem";
            }
            else if($hanhkiem>5 && $hanhkiem <=6){
                $xeploai = "Trung binh";
            }
            else if($hanhkiem >6 && $hanhkiem<=8){
                $xeploai = "Kha";
            }
            else if($hanhkiem >8 && $hanhkiem<=9){
                $xeploai = "Gioi";
            }
            else{
                $xeploai = "Xuat sac";
            }

            echo "<script> document.getElementById('ketqua').value = '$xeploai';</script>" ;       
        }
    ?>
</body>
</html>