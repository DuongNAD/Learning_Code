<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div>
        <form action="" method="POST">
            <div>
                <label for="link">Link image</label>
                <input type="text" name="link" id="link" class="">
            </div>
            <div>
                <label for="width">Chiều rộng image</label>
                <input type="text" name="width" id="width">
            </div>
            <div>
                <label for="height">Chiều dài image</label>
                <input type="text" name="height" id="height">
            </div>
            <div>
                <button type="submit" name="hienthi">Hiển thị</button>
            </div>
        </form>
    </div>
    <?php

    function _image($link,$width,$height){
        

        echo "<img src='$link' width='$width' height='$height' >";
        
    }
    if($_SERVER["REQUEST_METHOD"]=="POST"){
        $link = $_POST['link'];
        $width = $_POST['width'].'px';
        $height = $_POST['height'].'px';
        _image($link,$width,$height);
    }
    ?>
    
    
</body>

</html>