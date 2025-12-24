<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        $students = [
            ['name' => 'Nguyen Duc Binh', 'email' => 'ducbinh@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'1', 'img' =>'anh1'],
            ['name' => 'Nguyen Anh Duong', 'email' => 'duonganh@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'2', 'img' =>'anh2'],
            ['name' => 'Nguyen Van Tuan', 'email' => 'vantuan@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'3', 'img' =>'anh3'],
            ['name' => 'Nguyen Hoang Duc', 'email' => 'hoangduc@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'4', 'img' =>'anh4'],
            ['name' => 'Nguyen Minh Hieu', 'email' => 'minhhieu@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'5', 'img' =>'anh5'],
            ['name' => 'Nguyen Van Hoang', 'email' => 'vanhoang@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'6', 'img' =>'anh6'],
            ['name' => 'Nguyen Ngoc Hieu', 'email' => 'ngonhieu@gmail.com','phone' => '09966771508','gender'=>'nam','id'=>'7', 'img' =>'anh7'],
            ['name' => 'Do Trong An', 'email' => 'dotrongan496@gmail.com', 'phone' => '0356002098', 'gender'=>'nam','id'=>'8', 'img' => 'anh8'], 
        ];
    ?>
    <table border="1" cellspacing ="0" width ="70%" style="margin: 0 auto;">
        <caption><h2>Danh sach cac tai khoan</h2></caption>
        <tr>
            <th>id</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Gender</th>
            <th>Img</th>
        </tr>

        <?php
    foreach($students as $key => $std){
    ?>
        <tr> 
            <td><?php echo $std['id']; ?></td>    
            <td><?php echo $std['name']; ?></td>   
            <td><?php echo $std['email']; ?></td>  
            <td><?php echo $std['phone']; ?></td>  
            <td><?php echo $std['gender']; ?></td> 
            <?php $image_directory = "img/"; ?>
            <td><?php $image_full_path = $image_directory . $std['img'] . '.jpg'; 
            echo '<img src="' . $image_full_path . '" alt="Ảnh của ' . $std['name'] . '" width="50">';
            ?></td>
             
        </tr> 
        <?php
    }
    ?>

    </table>
</body>
</html>