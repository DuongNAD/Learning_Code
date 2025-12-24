<?php
session_start(); 

$name_data = [
    [
        "ten" => "Duong",
        "socu" => "7900",
        "somoi" => "8000",
        "dongia" => "2000"
    ],
    [
        "ten" => "Dung",
        "socu" => "7400",
        "somoi" => "8200",
        "dongia" => "2100"
    ],
    [
        "ten" => "An",
        "socu" => "7500",
        "somoi" => "7600",
        "dongia" => "1900"
    ],
    [
        "ten" => "Minh",
        "socu" => "6500",
        "somoi" => "6850",
        "dongia" => "2050"
    ],
    [
        "ten" => "Hoa",
        "socu" => "8100",
        "somoi" => "8300",
        "dongia" => "2000"
    ],
    [
        "ten" => "Kien",
        "socu" => "7050",
        "somoi" => "7300",
        "dongia" => "2200"
    ]
];

if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['ten'])) {

    $tenNguoiDungNhap = trim($_POST['ten']);

    $_SESSION['ten_input_for_display'] = $tenNguoiDungNhap;

    $timThayNguoiDung = false;
    $thongTinNguoiDung = null;

    if (!empty($tenNguoiDungNhap)) {
        foreach ($name_data as $nguoiDung) {
            if ($nguoiDung["ten"] === $tenNguoiDungNhap) {
                $timThayNguoiDung = true;
                $thongTinNguoiDung = $nguoiDung;
                break;
            }
        }
    }

    if ($timThayNguoiDung && $thongTinNguoiDung) {
        $_SESSION['socu'] = $thongTinNguoiDung['socu'];
        $_SESSION['somoi'] = $thongTinNguoiDung['somoi'];
        $_SESSION['dongia'] = $thongTinNguoiDung['dongia'];

        $soTieuThu = (int)$thongTinNguoiDung['somoi'] - (int)$thongTinNguoiDung['socu'];

        if ($soTieuThu >= 0) {
            $_SESSION['thanhtoan'] = $soTieuThu * (int)$thongTinNguoiDung['dongia'];
        } else {
            $_SESSION['thanhtoan'] = "Lỗi: Chỉ số mới phải lớn hơn hoặc bằng chỉ số cũ.";
        }

        unset($_SESSION['form_message']);

    } else {
        if (empty($tenNguoiDungNhap)) {
            $_SESSION['form_message'] = "Vui lòng nhập tên chủ hộ.";
        } else {
            $_SESSION['form_message'] = "Không tìm thấy thông tin cho chủ hộ: " . htmlspecialchars($tenNguoiDungNhap);
        }
        unset($_SESSION['socu']);
        unset($_SESSION['somoi']);
        unset($_SESSION['dongia']);
        unset($_SESSION['thanhtoan']);
    }

    header("Location: b3.php"); 
    exit();

} else {
    $_SESSION['form_message'] = "Truy cập không hợp lệ.";
    header("Location: b3.php"); 
    exit();
}
?>