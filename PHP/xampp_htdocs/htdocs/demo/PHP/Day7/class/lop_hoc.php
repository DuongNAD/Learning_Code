<?php

include 'header.php';
$class_value = '';
$students = []; 

if(isset($_GET['select_class'])){
    $class_value = $_GET['select_class'];
}

$query = "SELECT sinh_vien.id, sinh_vien.name, sinh_vien.email, sinh_vien.phone, lop_hoc.name as ten_lop
          FROM sinh_vien
          JOIN lop_hoc ON sinh_vien.lop_hoc_id = lop_hoc.id";

if (!empty($class_value)) {
    $class_id_filtered = intval($class_value);
    $query .= " WHERE sinh_vien.lop_hoc_id = " . $class_id_filtered;
}

$query .= " ORDER BY sinh_vien.id ASC";

$result = mysqli_query($conn, $query);

if ($result) {
    while ($row = mysqli_fetch_assoc($result)) {
        $students[] = $row;
    }
} else {
    echo "<p style='color: red;'>Lỗi truy vấn CSDL: " . mysqli_error($conn) . "</p>";
}

?>

<h2>Danh sách học sinh theo lớp</h2>
<form action="" method="GET">

    <label for="select_class">Chọn lớp</label>
    <select name="select_class" id="select_class" onchange="this.form.submit()">
        <option value="">-- Chọn lớp --</option>
        <?php
        $lop_hoc = [
            "1" => "Lớp Lập trình Web K10",
            "2" => "Lớp Cơ sở dữ liệu K10",
            "3" => "Lớp Lập trình C++ K9"
        ];
        foreach ($lop_hoc as $id => $ten_lop) {
            $selected = ($class_value == $id) ? 'selected' : '';
            echo "<option value=\"" . htmlspecialchars($id) . "\" $selected>" . htmlspecialchars($ten_lop) . "</option>";
        }
        ?>
    </select>
</form>

<?php if (!empty($students)): ?>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Họ tên</th>
            <th>Email</th>
            <th>Số điện thoại</th>
            <th>Lớp</th>
        </tr>
        <?php foreach ($students as $student_item) : ?>
            <tr>
                <td><?= htmlspecialchars($student_item['id']) ?></td>
                <td><?= htmlspecialchars($student_item['name']) ?></td>
                <td><?= htmlspecialchars($student_item['email']) ?></td>
                <td><?= htmlspecialchars($student_item['phone']) ?></td>
                <td><?= htmlspecialchars($student_item['ten_lop']) ?></td>
            </tr>
        <?php endforeach; ?>
    </table>
<?php else: ?>
    <p>Không tìm thấy sinh viên nào cho lớp đã chọn.</p>
<?php endif; ?>

<?php

include 'footer.php';

?>