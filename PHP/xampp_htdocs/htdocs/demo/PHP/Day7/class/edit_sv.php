<?php
include 'header.php';

$message = "";
$student_data = null;
$student_id_to_edit = 0;

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['student_id_hidden'])) {
    $student_id_to_edit = intval($_POST['student_id_hidden']);
} elseif ($_SERVER['REQUEST_METHOD'] == 'GET' && isset($_GET['id'])) {
    $student_id_to_edit = intval($_GET['id']);
}

if ($student_id_to_edit > 0) {
    $sql_select = "SELECT id, name, email, phone, lop_hoc_id FROM sinh_vien WHERE id = " . $student_id_to_edit;
    $result_select = mysqli_query($conn, $sql_select);

    if ($result_select && mysqli_num_rows($result_select) > 0) {
        $student_data = mysqli_fetch_assoc($result_select);
    } else {
        $message = "Lỗi: Không tìm thấy sinh viên với ID " . htmlspecialchars($student_id_to_edit) . " hoặc có lỗi truy vấn.";
        $student_data = null;
    }
} else {
    $message = "Vui lòng chọn một sinh viên từ danh sách để sửa.";
    $student_data = null;
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['edit_sv'])) {
    if ($student_id_to_edit > 0 && $student_data) {
        try {
            $name_new = trim($_POST['name'] ?? '');
            $email_new = trim($_POST['email'] ?? '');
            $phone_new = trim($_POST['phone'] ?? '');
            $class_id_new = $_POST['lop_hoc_id'] ?? '';

            $name_to_update = !empty($name_new) ? $name_new : $student_data['name'];
            $email_to_update = !empty($email_new) ? $email_new : $student_data['email'];
            $phone_to_update = !empty($phone_new) ? $phone_new : $student_data['phone'];
            $class_id_to_update = ($class_id_new !== '') ? intval($class_id_new) : $student_data['lop_hoc_id'];

            $query_update = "UPDATE sinh_vien
                             SET name = '" . mysqli_real_escape_string($conn, $name_to_update) . "',
                                 email = '" . mysqli_real_escape_string($conn, $email_to_update) . "',
                                 phone = '" . mysqli_real_escape_string($conn, $phone_to_update) . "',
                                 lop_hoc_id = " . intval($class_id_to_update) . "
                             WHERE id = " . intval($student_id_to_edit);

            $result = mysqli_query($conn, $query_update);

            if ($result) {
                $message = "Sửa sinh viên thành công!";
                $student_data['name'] = $name_to_update;
                $student_data['email'] = $email_to_update;
                $student_data['phone'] = $phone_to_update;
                $student_data['lop_hoc_id'] = $class_id_to_update;
            } else {
                $message = "Lỗi khi sửa sinh viên: " . mysqli_error($conn);
            }
        } catch (Exception $e) {
            $message = 'Lỗi ngoại lệ: ' . $e->getMessage();
        }
    } else {
        if (!($student_id_to_edit > 0)) {
            $message = "Lỗi: Không có ID sinh viên để thực hiện cập nhật.";
        } elseif (!$student_data) {
            $message = "Lỗi: Không thể tải dữ liệu sinh viên gốc để cập nhật. ID có thể không đúng.";
        }
    }
}
?>

<h2>Sửa sinh viên</h2>

<?php if (!empty($message)): ?>
    <p style="color: <?php echo strpos(strtolower($message), 'lỗi') === false ? 'green' : 'red'; ?>;">
        <?php echo htmlspecialchars($message); ?>
    </p>
<?php endif; ?>

<?php if ($student_data): ?>
    <form action="?id=<?php echo htmlspecialchars($student_id_to_edit); ?>" method="POST">
        <input type="hidden" name="student_id_hidden" value="<?php echo htmlspecialchars($student_id_to_edit); ?>">

        <p>
            <label for="name">Tên sinh viên:</label><br>
            <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($student_data['name'] ?? ''); ?>">
        </p>
        <p>
            <label for="email">Email:</label><br>
            <input type="email" name="email" id="email" value="<?php echo htmlspecialchars($student_data['email'] ?? ''); ?>">
        </p>
        <p>
            <label for="phone">Số điện thoại:</label><br>
            <input type="text" id="phone" name="phone" value="<?php echo htmlspecialchars($student_data['phone'] ?? ''); ?>">
        </p>
        <p>
            <label for="lop_hoc_id">Lớp học:</label><br>
            <select name="lop_hoc_id" id="lop_hoc_id">
                <option value="">-- Chọn lớp --</option>
                <?php
                $current_lop_id = $student_data['lop_hoc_id'] ?? '';
                $cac_lop_hoc = [
                    "1" => "Lớp Lập trình Web K10",
                    "2" => "Lớp Cơ sở dữ liệu K10",
                    "3" => "Lớp Lập trình C++ K9"
                ];
                foreach ($cac_lop_hoc as $id_lop => $ten_lop) {
                    $selected_attr = ($current_lop_id == $id_lop) ? 'selected' : '';
                    echo "<option value=\"" . htmlspecialchars($id_lop) . "\" $selected_attr>" . htmlspecialchars($ten_lop) . "</option>";
                }
                ?>
            </select>
        </p>
        <br>
        <button type="submit" name="edit_sv">Sửa sinh viên</button>
        <a href="sinh_vien.php">Quay lại danh sách</a>

        <?php if (!empty($message)): ?>
            <p style="color: <?php echo strpos(strtolower($message), 'lỗi') === false ? 'green' : 'red'; ?>;">
                <?php echo htmlspecialchars($message); ?>
            </p>
        <?php endif; ?>

    </form>
<?php else: ?>
    <p style="color: red;"><?php echo htmlspecialchars($message); ?></p>
    <a href="sinh_vien.php">Quay lại danh sách</a>
<?php endif; ?>

<?php
include 'footer.php';
?>