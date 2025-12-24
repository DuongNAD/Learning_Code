<?php

include 'header.php';

$cart_update_message = "";
if (isset($_SESSION['cart_message'])) {
    $cart_update_message = $_SESSION['cart_message'];
    unset($_SESSION['cart_message']); 
}


if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_cart'])) {
    if (isset($_POST['quantities']) && is_array($_POST['quantities'])) {
        foreach ($_POST['quantities'] as $book_id => $quantity) {
            $book_id = (int)$book_id;
            $quantity = (int)$quantity;

            if (isset($_SESSION['cart'][$book_id])) {
                if ($quantity > 0) {
                    $_SESSION['cart'][$book_id]['quantity'] = $quantity;
                } else {
                    unset($_SESSION['cart'][$book_id]);
                }
            }
        }
        $_SESSION['cart_message'] = "Giỏ hàng đã được cập nhật.";
    }
    header('Location: cart.php');
    exit;
}

$total_price = 0;
?>
<div class="cart-container">
    <h2>Giỏ hàng</h2>

    <?php
    if (!empty($cart_update_message)) {
        echo "<p style='color: green; font-weight: bold;'>" . htmlspecialchars($cart_update_message) . "</p>";
    }

    if(isset($_SESSION['cart'])&& !empty($_SESSION['cart'])) :
    ?>
    <form action="cart.php" method="POST">
        <table border = "1" style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr>
                    <th>Tên sách</th>
                    <th>Giá</th>
                    <th>Số lượng</th>
                    <th>Thành tiền</th>
                    <th>Xóa</th>
                </tr>
            </thead>
            <tbody>
                <?php
            foreach($_SESSION['cart'] as $book_id=> $book) :
            $subtotal = $book['price'] * $book['quantity'];

            $total_price += $subtotal;
        ?>
            <tr>
                <td><?= htmlspecialchars($book['title']) ?></td>
                <td><?= number_format($book['price']) ?> VNĐ</td>
                <td>
                    <input type="number" name="quantities[<?= $book_id ?>]" value="<?= htmlspecialchars($book['quantity']) ?>" min="0" style="width: 60px;">
                </td>
                <td><?= number_format($subtotal) ?> VNĐ</td>
                <td>
                    <button type="submit" name="quantities[<?= $book_id ?>]" value="0" onclick="return confirm('Bạn có chắc chắn muốn xóa sản phẩm này?');">Xóa</button>
                </td>
            </tr>
        <?php endforeach; ?>
            </tbody>
        </table>
        <div style="text-align: right; margin-top: 20px;">
            <button type="submit" name="update_cart" style="padding: 10px; background-color: #007bff; color: white; border: none; cursor: pointer;">Cập nhật giỏ hàng</button>
        </div>
    </form>
    <div style="text-align: right; margin-top: 20px;">
            <h3>Tổng cộng: <?= number_format($total_price) ?> VNĐ</h3>
            <a href="product.php" style="text-decoration: none; padding: 10px; background-color: #ccc;">Tiếp tục mua sắm</a>
            <a href="checkout.php" style="text-decoration: none; padding: 10px; background-color: #28a745; color: white;">Tiến hành thanh toán</a>
        </div>
        <?php else : ?>
        <p>Giỏ hàng của bạn đang trống. Hãy quay lại <a href="product.php">trang sản phẩm</a> để lựa chọn sách.</p>
    <?php endif; ?>

</div>
<?php

include 'footer.php';

?>
