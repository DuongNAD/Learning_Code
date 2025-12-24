<?php
session_start(); 
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thanh toan tien dien</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        .form-group label {
            min-width: 120px; 
        }
        .form-group input[readonly] {
            background-color: #e9ecef; 
            opacity: 1; 
        }
        .error-message {
            color: red;
            margin-top: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container d-flex justify-content-center align-items-center vh-100">
        <div class="card p-4 shadow">
            <div class="card-body">
                <h2 class="card-title text-center mb-4">Thanh toán tiền điện</h2>

                <?php

                if (isset($_SESSION['form_message'])) {
                    echo '<div class="error-message">' . htmlspecialchars($_SESSION['form_message']) . '</div>';
                    unset($_SESSION['form_message']);
                }
                ?>

                <form method="POST" action="form_write.php">
                    <div class="form-group d-flex align-items-center">
                        <label for="ten" class="mr-2">Tên chủ hộ:</label>
                        <input type="text" class="form-control" id="ten" name="ten" required
                               value="<?php

                                   if (isset($_SESSION['ten'])) {
                                       echo ($_SESSION['ten']);
                                       unset($_SESSION['ten']);
                                   }
                               ?>"
                        >
                    </div>

                    <div class="form-group d-flex align-items-center">
                        <label for="socu" class="mr-2">Chỉ số cũ (Kw):</label>
                        <input type="text" class="form-control" id="socu" name="socu" readonly
                               value="<?php

                                   if (isset($_SESSION['socu'])) {
                                       echo ($_SESSION['socu']);
                                       unset($_SESSION['socu']); 
                                   }
                               ?>"
                        >
                    </div>

                    <div class="form-group d-flex align-items-center">
                        <label for="somoi" class="mr-2">Chỉ số mới (Kw):</label>
                        <input type="text" class="form-control" id="somoi" name="somoi" readonly
                               value="<?php

                                   if (isset($_SESSION['somoi'])) {
                                       echo ($_SESSION['somoi']);
                                       unset($_SESSION['somoi']);
                                   }
                               ?>"
                        >
                    </div>

                    <div class="form-group d-flex align-items-center">
                        <label for="dongia" class="mr-2">Đơn giá (VNĐ):</label>
                        <input type="text" class="form-control" id="dongia" name="dongia" readonly
                               value="<?php

                                   if (isset($_SESSION['dongia'])) {
                                       echo ($_SESSION['dongia']);
                                       unset($_SESSION['dongia']); 
                                   }
                               ?>"
                        >
                    </div>

                    <div class="form-group d-flex align-items-center">
                        <label for="thanhtoan" class="mr-2">Số tiền thanh toán (VNĐ):</label>
                        <input type="text" class="form-control" id="thanhtoan" name="thanhtoan" readonly
                               value="<?php

                                   if (isset($_SESSION['thanhtoan'])) {
                                       echo ($_SESSION['thanhtoan']);
                                       unset($_SESSION['thanhtoan']); 
                                   }
                               ?>"
                        >
                    </div>

                    <button type="submit" class="btn btn-primary btn-block">Tính</button>
                </form>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>