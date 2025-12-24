<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="POST" action="">
        <div>
            <label for="so1">Nhap so thu nhat:</label>
            <input type="number" id="so1" name="so1" required>
        </div>
        <div>
            <label for="so2">Nhap so thu hai:</label>
            <input type="number" id="so2" name="so2" required>
        </div>
        <div>
            <p>Chon phep tinh:</p>
            <p>1. Cong 2 so</p>
            <p>2. Tru 2 so</p>
            <p>3. Nhan 2 so</p>
            <p>4. Chia 2 so</p>
        </div>
        <div>
            <label for="chose">Nhap lua chon (1-4):</label>
            <input type="number" id="chose" name="chose" min="1" max="4" required>
        </div>
        <div>
            <button type="submit" name="submit">Tinh</button>
        </div>
        <div>
            <label for="dapan">Dap an:</label>
            <input type="number" id="dapan" name="dapan" readonly>
        </div>

        <?php
            if($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['submit'])){
                $so1 = $_POST['so1'];
                $so2 = $_POST['so2'];
                $dapan = ""; // Khởi tạo giá trị mặc định cho $dapan
                $chose = $_POST['chose'];

                switch($chose){
                    case 1:
                        $dapan = $so1 + $so2;
                        break;
                    case 2:
                        $dapan = $so1 - $so2;
                        break;
                    case 3:
                        $dapan = $so1 * $so2;
                        break;
                    case 4:
                        $dapan = $so1 / $so2;
                        break;
                    default:
                        $dapan = "Lua chon khong hop le";
                        break;
                }
                echo "<script> document.getElementById('dapan').value = '$dapan';</script>";
            }
        ?>
    </form>
</body>
</html>