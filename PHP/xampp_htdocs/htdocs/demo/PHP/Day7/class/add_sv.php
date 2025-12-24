<?php
include 'header.php';

$message = "";
$name_value = '';
$email_value = '';
$phone_value = '';
$class_value = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add'])) {
    try {
        $name_raw = $_POST['name'] ?? '';
        $email_raw = $_POST['email'] ?? '';
        $phone_raw = $_POST['phone'] ?? '';
        $class_raw = $_POST['class'] ?? '';

        $name_value = $name_raw;
        $email_value = $email_raw;
        $phone_value = $phone_raw;
        $class_value = $class_raw;

        $name = trim($name_raw);
        $email = trim($email_raw);
        $phone = trim($phone_raw);
        $class_id = intval($class_raw);

        if (empty($name) || empty($email) || empty($phone) || $class_id == 0) {
            $message = "Lỗi: Vui lòng điền đầy đủ thông tin và chọn lớp học.";
        } else {

            $query = "INSERT INTO sinh_vien(name, email, phone, lop_hoc_id) VALUES (
                        '$name_escaped',
                        '$email_escaped',
                        '$phone_escaped',
                        $class_id
                      )";

            $result = mysqli_query($conn, $query);

            if ($result) {
                $message = "Thêm sinh viên thành công!";
                $name_value = '';
                $email_value = '';
                $phone_value = '';
                $class_value = '';
            } else {
                $message = "Lỗi khi thêm sinh viên: " . mysqli_error($conn);
            }
        }
    } catch (Exception $e) {
        $message = 'Lỗi ngoại lệ: ' . $e->getMessage();
    }
}
?>
<h2>Thêm sinh viên</h2>

<form action="" method="POST">
    <label for="name">Tên sinh viên</label>
    <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name_value); ?>" required><br><br>

    <label for="email">Email</label>
    <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email_value); ?>" required><br><br>

    <label for="phone">Số điện thoại</label>
    <input type="text" id="phone" name="phone" value="<?php echo htmlspecialchars($phone_value); ?>" required><br><br>

    <label for="class">Lớp học</label>
    <select name="class" id="class">
        <option value="">-- Chọn lớp --</option>
        <?php
        $cac_lop_hoc = [
            "1" => "Lớp Lập trình Web K10",
            "2" => "Lớp Cơ sở dữ liệu K10",
            "3" => "Lớp Lập trình C++ K9"
        ];
        foreach ($cac_lop_hoc as $id_lop => $ten_lop) {
            $selected_attr = ($class_value == $id_lop) ? 'selected' : '';
            echo "<option value=\"" . htmlspecialchars($id_lop) . "\" $selected_attr>" . htmlspecialchars($ten_lop) . "</option>";
        }
        ?>
    </select><br><br>
    <button type="submit" name="add">Thêm</button>

    <?php if (!empty($message)): ?>
        <p style="color: <?php echo strpos(strtolower($message), 'lỗi') === false ? 'green' : 'red'; ?>;">
            <?php echo htmlspecialchars($message); ?>
        </p>
    <?php endif; ?>
</form>

<?php
include 'footer.php';
?>