<?php

include 'header.php';

$message = "";

if(isset($_GET['id'])){
    $student_id_to_delete = $_GET['id'];

    $query_delete = "delete from sinh_vien where id = " . $student_id_to_delete;

    if(mysqli_query($conn,$query_delete)){
        header ("location: sinh_vien.php");
        exit();
    }
    else{
        echo "Lỗi: " . mysqli_error($conn);
    }
}
else{
    echo "Không tìm thấy ID sinh viên để xóa";
}

include 'footer.php'


?>