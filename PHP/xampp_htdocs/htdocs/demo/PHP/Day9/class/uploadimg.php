<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Upload Ảnh Bìa Sách</h2>
    <form action="" method="POST" enctype="multipart/form-data">
        Chọn ảnh bìa:
        <input type="file" name="book_image" required>
        <input type="submit" name="submit" value="Upload">
    </form>
</body>
</html>

<?php

if($_SERVER['REQUEST_METHOD'] == 'POST'){

    $targetDir = "uploads/";
    $fileName = basename($_FILES["book_image"]["name"]);
    $targetFilePath = $targetDir . $fileName;
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($targetFilePath, PATHINFO_EXTENSION));

    if(isset($_POST["submit"])){
        $check = getimagesize($_FILES["book_image"]["tmp_name"]);
        if($check !== false){
            echo "file là một hình ảnh - " . $check["mime"] . ".<br>";
            $uploadOk = 1;
        }
        else{
            echo "File không phải là hình ảnh.<br>";
            $uploadOk = 0;
        }
    }

    if(file_exists($targetFilePath)){
        echo "Xin lỗi, file đã tồn tại.<br>";
        $uploadOk = 0;
    }

    if($_FILES["book_image"]["size"] > 2 * 1024 * 1024){
        echo "Xin lỗi, file quá lớn. Chỉ cho phép file dưới 2MB.<br>";
        $uploadOk = 0;
    }

    $allowedType = ["jpg","png","jpeg","gif"];
    if(!in_array($imageFileType,$allowedType)){
        echo "Chỉ cho phép cá file JPG, PNG, JPEG & GIF.<br>";
        $uploadOk = 0;
    }

    if($uploadOk == 1){
        if(!is_dir($targetDir)){
            mkdir($targetDir, 0777,true);
        }

        if(move_uploaded_file($_FILES["book_image"]["tmp_name"], $targetFilePath)){
            echo "FIle " . htmlspecialchars($fileName) . " đã được upload thành công.<br>";
            echo "Đường dẫn file: <a href='$targetFilePath' target='_blank'>$targetFilePath</a><br>";
            echo "<img src = '$targetFilePath' width='300' height='300'>";
        }
        else{
            echo "Có lỗi khi upload file.<br>";
        }
    }



}

?>