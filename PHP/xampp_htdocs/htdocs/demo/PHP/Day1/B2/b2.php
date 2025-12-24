<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tính diện tích hình tròn</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <?php
        session_start(); 
    ?>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow">
            <div class="card-body">
                <h2 class="card-title text-center mb-3">Tính diện tích hình tròn</h2>
                <form method="POST" action="form_write.php">
                    <div class="form-group">
                        <label for="bankinh">Bán kính</label>
                        <input type="number" class="form-control" id="bankinh" name="bankinh" required>
                    </div>
                    <div class="form-group">
                        <label for="chuvi">Chu vi</label>
                        <input type="text" class="form-control" id="chuvi" name="chuvi" readonly
                               value="<?php
                                   if(isset($_SESSION["chuvi"])){
                                       echo $_SESSION["chuvi"];
                                       unset($_SESSION["chuvi"]);
                                   }
                               ?>">
                    </div>
                    <div class="form-group">
                        <label for="dientich">Diện tích</label>
                        <input type="text" class="form-control" id="dientich" name="dientich" readonly
                               value="<?php
                                   if(isset($_SESSION["dientich"])){
                                       echo $_SESSION["dientich"];
                                       unset($_SESSION["dientich"]);
                                   }
                               ?>">
                    </div>
                    <div>
                        <button type="submit" class="btn btn-primary btn-block" name="tinh">Tính</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>