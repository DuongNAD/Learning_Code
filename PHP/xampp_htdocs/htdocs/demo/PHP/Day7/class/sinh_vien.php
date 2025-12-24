<?php

include 'header.php';

$query = "SELECT sinh_vien.*, lop_hoc.name as ten_lop FROM sinh_vien JOIN lop_hoc on sinh_vien.lop_hoc_id = lop_hoc.id order by sinh_vien.id ASC";
$result = mysqli_query($conn, $query);

?>

<h2>Danh sách sinh viên</h2>
<table border="1">
    <tr>
        <th>ID</th>
        <th>Họ tên</th>
        <th>Email</th>
        <th>Số điện thoại</th>
        <th>Lớp</th>
        <th>Trạng thái</th>
    </tr>
    <?php while ($row = mysqli_fetch_assoc($result)) : ?>

        <tr>
            <td><?= $row['id'] ?></td>
            <td><?= $row['name'] ?></td>
            <td><?= $row['email'] ?></td>
            <td><?= $row['phone'] ?></td>
            <td><?= $row['ten_lop'] ?></td>
            <td>
                <a href="edit_sv.php?id=<?= $row['id'] ?>">Sửa</a>
                <a href="delete_sv.php?id=<?= $row['id'] ?>" onclick="return confirm('Xóa sinh viên')">Xóa</a>
            </td>

        </tr>
    <?php endwhile; ?>
</table>
<button type="submit" name="edit"><a href="add_sv.php">Thêm sinh viên</a></button>
<?php
include 'footer.php';
?>