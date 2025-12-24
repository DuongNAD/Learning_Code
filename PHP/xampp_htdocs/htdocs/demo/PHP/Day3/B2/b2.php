<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }

        h2,
        h3 {
            text-align: center;
            color: #333;
        }

        table {
            width: 70%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #4CAF50;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        form {
            margin: 20px auto;
            width: 70%;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        form div {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input[type="text"],
        input[type="number"] {
            width: calc(100% - 22px);
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            display: block;
            margin-top: 10px;
        }

        button[name="timkiem"] {
            background-color: #17a2b8;
            margin-left: auto;
            margin-right: auto;
            display: block;
        }

        button[name="them"] {
            background-color: #28a745;
            margin-left: auto;
            margin-right: auto;
            display: block;
        }

        button:hover {
            opacity: 0.9;
        }

        .message {
            text-align: center;
            margin-top: 10px;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <?php
    session_start();
    if (!isset($_SESSION['student_list'])) {
        $_SESSION['student_list'] = [
            ['Stt' => 1, 'Name' => 'Nguyen Anh Duong', 'toan' => 8.6, 'ly' => 9, 'hoa' => 8.6],
            ['Stt' => 2, 'Name' => 'Nguyen Huy Hoang', 'toan' => 8.8, 'ly' => 7.9, 'hoa' => 7],
            ['Stt' => 3, 'Name' => 'Nguyen Duc Anh', 'toan' => 8, 'ly' => 9.6, 'hoa' => 6],
            ['Stt' => 4, 'Name' => 'Pham Duc Dung', 'toan' => 8.9, 'ly' => 7.2, 'hoa' => 8.6],
            ['Stt' => 5, 'Name' => 'Le Van Quang', 'toan' => 6.8, 'ly' => 3, 'hoa' => 5.6],
            ['Stt' => 6, 'Name' => 'Nguyen Minh Duc', 'toan' => 8.6, 'ly' => 9, 'hoa' => 4.4],
            ['Stt' => 7, 'Name' => 'Do Trong An', 'toan' => 6, 'ly' => 8, 'hoa' => 8.4],
            ['Stt' => 8, 'Name' => 'Le Hong Phong', 'toan' => 7, 'ly' => 5.6, 'hoa' => 9.6],
        ];
    }
    $students_to_display = $_SESSION['student_list'];
    $message = '';

    if ($_SERVER['REQUEST_METHOD'] == 'POST' ) {
        if(isset($_POST['them'])){
        $name = trim($_POST['namest']);
        $toan = floatval($_POST['mark-toan']);
        $ly = floatval($_POST['mark-ly']);
        $hoa = floatval($_POST['mark-hoa']);

        if (!empty($name && $toan >= 0 && $toan <= 10 && $ly >= 0 && $ly <= 10 && $hoa >= 0 && $hoa <= 10)) {
            $next_stt = 1;

            if (!empty($_SESSION['student_list'])) {
                $column_stt = array_column($_SESSION['student_list'], 'Stt');
                $next_stt = max($column_stt) + 1;
            }

            $new_student = [
                'Stt' => $next_stt,
                'Name' => $name,
                'toan' => $toan,
                'ly' => $ly,
                'hoa' => $hoa,
            ];

            $_SESSION['student_list'][] = $new_student;
            $students_to_display = $_SESSION['student_list'];
            $message = "<p class='message' style='color: green;'>Thêm học sinh thành công!</p>";
        } else {
            $message = "<p class='message' style='color: red;'>Vui lòng nhập đầy đủ và đúng định dạng các trường (điểm từ 0-10).</p>";
        }
    }
        if (isset($_POST['timkiem'])) {
        $search_query = trim($_POST['search']);
        if (!empty($search_query)) {
            $students_to_display = array_filter($_SESSION['student_list'], function ($student) use ($search_query) {
                return stripos($student['Name'], $search_query) !== false;
            });

            if (empty($students_to_display)) {
                $message = "<p class='message' style='color: orange;'>Không tìm thấy học sinh nào với tên '<strong>" . htmlspecialchars($search_query) . "</strong>'.</p>";
            } else {
                $message = "<p class='message' style='color: blue;'>Kết quả tìm kiếm cho '<strong>" . htmlspecialchars($search_query) . "</strong>'.</p>";
            }
        } else {
            $message = "<p class='message' style='color: red;'>Vui lòng nhập tên học sinh cần tìm.</p>";
        }
    }
}
    ?>

    <div>
        <h2>Danh sách học sinh</h2>
    </div>

    <?php echo $message; ?>

    <form action="" method="POST">
        <div>
            <label for="search">Tìm kiếm học sinh theo tên:</label>
            <input type="text" name="search" id="search" value="<?php echo isset($_POST['search']) ? htmlspecialchars($_POST['search']) : ''; ?>">
        </div>
        <div>
            <button type="submit" name="timkiem">Tìm kiếm</button>
        </div>
    </form>

    <div>
        <table border="1" cellspacing="0">
            <thead>
                <tr>
                    <th>Stt</th>
                    <th>Name</th>
                    <th>Điểm toán</th>
                    <th>Điểm lý</th>
                    <th>Điểm hóa</th>
                    <th>Điểm trung bình</th>
                    <th>Xếp loại</th>
                </tr>
            </thead>
            <tbody>
                <?php
                if (!empty($students_to_display)) {
                    foreach ($students_to_display as $diem) {
                        $toan = $diem['toan'];
                        $ly = $diem['ly'];
                        $hoa = $diem['hoa'];

                        $diemtb = number_format(($toan + $ly + $hoa) / 3, 2);

                        $xeploai = "";

                        if ($diemtb >= 9 && $diemtb <= 10) {
                            if ($toan >= 8 && $ly >= 8 && $hoa >= 8) {
                                $xeploai = 'Xuất Sắc';
                            } else {
                                $xeploai = 'Giỏi';
                            }
                        } elseif ($diemtb >= 8 && $diemtb < 9) {
                            if ($toan >= 8 && $ly >= 8 && $hoa >= 8) {
                                $xeploai = 'Giỏi';
                            } else {
                                $xeploai = 'Khá';
                            }
                        } elseif ($diemtb >= 6.5 && $diemtb < 8) {
                            if ($toan >= 5 && $ly >= 5 && $hoa >= 5) {
                                $xeploai = 'Khá';
                            } else {
                                $xeploai = 'Trung Bình';
                            }
                        } elseif ($diemtb >= 5 && $diemtb < 6.5) {
                            $xeploai = 'Trung Bình';
                        } elseif ($diemtb >= 3.5 && $diemtb < 5) {
                            $xeploai = 'Yếu';
                        } elseif ($diemtb < 3.5) {
                            $xeploai = 'Kém';
                        } else {
                            $xeploai = "Không hợp lệ";
                        }

                ?>
                        <tr>
                            <td><?php echo $diem['Stt']; ?></td>
                            <td><?php echo htmlspecialchars($diem['Name']); ?></td>
                            <td><?php echo $diem['toan']; ?></td>
                            <td><?php echo $diem['ly']; ?></td>
                            <td><?php echo $diem['hoa']; ?></td>
                            <td><?php echo $diemtb; ?></td>
                            <td><?php echo $xeploai; ?></td>
                        </tr>
                <?php
                    }
                } else {
                    echo '<tr><td colspan="7" style="text-align: center;">Không có học sinh nào trong danh sách hoặc không tìm thấy kết quả.</td></tr>';
                }
                ?>

            </tbody>
        </table>
    </div>

    <div>
        <h3>Thêm học sinh mới</h3>
        <form action="" method="POST">
            <div>
                <label for="namest">Tên học sinh:</label>
                <input type="text" name="namest" id="namest" required>
            </div>
            <div>
                <label for="mark-toan">Điểm toán (0-10):</label>
                <input type="number" name="mark-toan" id="mark-toan" step="0.1" min="0" max="10" required>
            </div>
            <div>
                <label for="mark-ly">Điểm lý (0-10):</label>
                <input type="number" name="mark-ly" id="mark-ly" step="0.1" min="0" max="10" required>
            </div>
            <div>
                <label for="mark-hoa">Điểm hóa (0-10):</label>
                <input type="number" name="mark-hoa" id="mark-hoa" step="0.1" min="0" max="10" required>
            </div>
            <div>
                <button type="submit" name="them">Thêm học sinh</button>
            </div>
        </form>
    </div>


</body>

</html>