<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tinh S hcn</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow">
            <div class="card-body">
                <h2 class="card-title text-center mb-3">Diện tích hình chữ nhật</h2>
                <form method="post" action="from_write.php">
                    <div class="form-group">
                        <label for="dai">Chiều dài</label>
                        <input type="number" class="form-control" name="dai" id="dai" required>
                    </div>
                    <div class="form-group">
                        <label for="rong">Chiều rộng</label>
                        <input type="number" class="form-control" name="rong" id="rong" required>
                    </div>
                    <div class="form-group">
                        <label for="dientich">Diện tích</label>
                        <input type="text" class="form-control" name="dientich" id="dientich" readonly

                        value="<?php
                                   session_start();
                                   if (isset($_SESSION["dientich"])) {
                                       echo $_SESSION["dientich"];
                                       unset($_SESSION["dientich"]);
                                   }
                               ?>">

                    </div>
                    <button type="submit" class="btn btn-primary btn-block" name="tinh">Tính</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>