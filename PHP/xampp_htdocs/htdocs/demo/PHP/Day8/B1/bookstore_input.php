<?php


include 'header.php';

$message ="";
$title_value ='';
$author_value = '';
$price_value   ='';
$stock_value ='';
$description_value = ''; 

if($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['add_book'])){
    try{
        $title_value = $_POST['title'] ?? '';
        $author_value = $_POST['author'] ?? '';
        $price_value = $_POST['price'] ?? '';
        $stock_value = $_POST['stock'] ?? '';
        $description_value = $_POST['description'] ?? '';

        $title = trim($title_value);
        $author = trim ($author_value);
        $price = trim ($price_value);
        $stock = trim($stock_value);
        $description = trim($description_value);

        if(empty($title) || $price <= 0  || $stock <=0){
            $message = "Lỗi: Vui lòng điền đầy đủ thông tin";
        }
        else{
            $query = "insert into books(title ,author ,price,stock,description) values (
                '$title',
                '$author',
                '$price',
                '$stock',
                '$description'
                )";
            $result = mysqli_query($conn,$query);

            if ($result) {
                $message = "Thêm sách thành công!";
                $title_value= '';
                $author_value= '';
                $price_value= '';
                $stock_value= '';
                $description_value = '';
            } 

            else {
                $message = "Lỗi khi thêm sách: " . mysqli_error($conn);
            } 
        } 
    }
    catch (Exception $e) {
        $message = "Đã xảy ra lỗi: " . $e->getMessage();
    }   
}

?>
<form action="" method="POST">
    <h2>Thêm sản phẩm</h2>
    <div>
        <label for="title">Title</label>
        <input type="text" name="title" id="title" required value="<?php echo htmlspecialchars($title_value); ?>">

        <label for="author">Author</label>
        <input type="text" name="author" id="author" value="<?php echo htmlspecialchars($author_value); ?>">

        <label for="price">Price</label>
        <input type="number" name="price" id="price" step="0.01" required value="<?php echo htmlspecialchars($price_value); ?>">

        <label for="stock">Stock</label>
        <input type="number" name="stock" id="stock" required value="<?php echo htmlspecialchars($stock_value); ?>">

        <label for="description">Description</label>
        <textarea name="description" id="description" rows="4" cols="30"><?php echo htmlspecialchars($description_value); ?></textarea><br><br>

        <button type="submit" name="add_book">thêm sách</button>
    </div>
</form>

<?php
if (!empty($message)) {
    $message_color = (strpos(strtolower($message), 'lỗi') === false && strpos(strtolower($message), 'error') === false) ? 'green' : 'red';
    echo "<p style='color: {$message_color};'>" . htmlspecialchars($message) . "</p>";
}
?>

<?php

include 'footer.php';
?>