<?php
session_start();

$error = '';

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['tinh'])) {
    $soluong = $_POST['soluong'];
    $thoigian = $_POST['thoigian'];

    $gia = 0;
    $tongtien = 0;

    if ($soluong > 0 && $thoigian > 0) {
        if ($thoigian < 10) {
            $gia = 5.5;
        } elseif ($thoigian >= 10 && $thoigian <= 20) {
            $gia = 4;
        } elseif ($thoigian > 20 && $thoigian <= 30) {
            $gia = 2.5;
        } else {
            $gia = 0;
        }

        $tongtien = $gia * $soluong;
        $_SESSION['tinhtien'] = $tongtien; 

        echo "<script>document.getElementById('tinhtien').value = '$tongtien';</script>";
    } else {
        $error = "Số lượng hoặc thời gian không hợp lệ!";
    }
}
?>

<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tính tiền giao Pizza</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow">
            <div class="card-body">
                <h2 class="card-title text-center mb-3">Tính tiền giao Pizza</h2>
                <?php if ($error != ''): ?>
                    <div class="alert alert-danger"><?php echo $error; ?></div>
                <?php endif; ?>
                <form method="POST" action="<?php echo($_SERVER['PHP_SELF']); ?>">
                    <div class="form-group">
                        <label for="soluong">Số lượng Pizza</label>
                        <input type="number" class="form-control" name="soluong" id="soluong" required>
                    </div>
                    <div class="form-group">
                        <label for="thoigian">Thời gian (phút)</label>
                        <input type="number" class="form-control" name="thoigian" id="thoigian" required>
                    </div>
                    <div class="form-group">
                        <label for="tinhtien">Tính tiền</label>
                        <input type="text" class="form-control" name="tinhtien" id="tinhtien" readonly
                               value="<?php echo isset($_SESSION['tinhtien']) ? $_SESSION['tinhtien'] : ''; ?>">
                    </div>
                    <button type="submit" class="btn btn-primary btn-block" name="tinh">Tính</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>