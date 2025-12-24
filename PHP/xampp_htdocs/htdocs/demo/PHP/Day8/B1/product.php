<?php

include 'header.php';

$message = "";

if($_SERVER['REQUEST_METHOD']=='POST' && isset($_POST['add_to_cart'])){
    $book_id = (int)$_POST['book_id'];

    if (!isset($_SESSION['cart'])) {
        $_SESSION['cart'] = [];
    }

    if(isset($_SESSION['cart'][$book_id])){
        $_SESSION['cart'][$book_id]['quantity']++;
        echo "Đã cập nhật số lượng sách trong giỏ hàng.";
    }
    else{
        $query = "select title, price from books where id = ? and stock >0";

        $stmt = $conn->prepare($query);
        $stmt->bind_param("i", $book_id);
        $stmt->execute();
        $result = $stmt->get_result();
        if ($book = $result->fetch_assoc()) { 
            $_SESSION['cart'][$book_id] = [
                'title' => $book['title'],
                'price' => $book['price'],
                'quantity' => 1
            ];
            echo "Đã thêm sách vào giỏ hàng.";
        }
        else{
            echo "Không thể thêm sách này vào giỏ hàng.";
        }
    }
}


$query = "select * from books";

$result = mysqli_query($conn,$query);

?>

<h2>Danh sách sản phẩm</h2>

<?php
if (!empty($message)) {
    echo "<p style='color: green; font-weight: bold;'>" . htmlspecialchars($message) . "</p>";
}
?>

<table border="1">
    <tr>
        <th>ID</th>
        <th>title</th>
        <th>author</th>
        <th>price</th>
        <th>stock</th>
        <th>description</th>
    </tr>
    <?php while($row = mysqli_fetch_assoc($result)) : ?>
        <tr>
            <td><?= htmlspecialchars($row['id']) ?></td>
            <td><?= htmlspecialchars($row['title']) ?></td>
            <td><?= htmlspecialchars($row['author']) ?></td>
            <td><?= number_format($row['price']) ?> VNĐ</td>
            <td><?= htmlspecialchars($row['stock']) ?></td>
            <td>
                <form action="product.php" method="POST">
                     <input type="hidden" name="book_id" value="<?= $row['id'] ?>">
                    
                    <button type="submit" name="add_to_cart">Thêm vào giỏ</button>
                </form>
            </td>
        </tr>
        <?php endwhile ?>
</table>

<?php   
include 'footer.php';

?>