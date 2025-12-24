<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Tinh dien tich hinh chu nhat</h2>
    <form method="POST" action="">
        <label for="chieudai">Chieu dai:</label>
        <input type="number" id="chieudai" name="chieudai" required><br><br>

        <label for="chieurong">Chieu rong:</label>
        <input type="number" id="chieurong" name="chieurong" required><br><br>

        <label for="dientich">Dien tich</label>
        <input type="text" id="dientich" name="dientich" readonly><br><br>

        <button type="submit" name="tinh">Tinh</button>
    </form>

    <?php 
    if($_SERVER["REQUEST_METHOD"]== "POST" && isset($_POST['tinh'])){
        $chieudai = $_POST['chieudai'];
        $chieurong = $_POST['chieurong'];

        $dt = $chieudai * $chieurong;

        echo "<script>document.getElementById('dientich').value = '$dt';</script>";
    }
    ?>
</body>
</html>