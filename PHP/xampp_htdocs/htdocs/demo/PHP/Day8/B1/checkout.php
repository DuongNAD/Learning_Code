<?php
include 'header.php';
if(empty($_SESSION['cart'])){
    header('Location: product.php');
    exit;
}

$message = "";

$customer_name = '';
$customer_email = '';
$customer_phone = '';
$customer_address = '';

if($_SERVER['REQUEST_METHOD'] == 'POST' ){
    $customer_name = trim($_POST['customer_name'] ?? '');
    $customer_email = trim($_POST['customer_email'] ?? '');
    $customer_phone = trim($_POST['customer_phone'] ?? '');
    $customer_address = trim($_POST['customer_address'] ?? '');

    if(empty($customer_name) || empty($customer_email) || empty($customer_address) || empty($customer_phone)){
        $message = "Vui lòng điền đầy đủ thông tin giao hàng";
    } else {
        $conn->begin_transaction();

        try {
            $total_amount = 0;
            foreach($_SESSION['cart'] as $book){
                $total_amount += $book['price'] * $book['quantity'];
            }
            $query_order = "INSERT INTO `orders` (customer_name, customer_email, customer_phone, customer_address, total_amount) VALUES
            ('$customer_name', '$customer_email', '$customer_phone', '$customer_address', $total_amount)";
            mysqli_query($conn, $query_order); 

            $order_id = $conn->insert_id;

            foreach($_SESSION['cart'] as $book_id => $book){
                $book_quantity = $book['quantity'];
                $book_price = $book['price'];
                $query_details = "INSERT INTO order_details (order_id, book_id, quantity, price) VALUES
                ('$order_id', '$book_id', '$book_quantity', '$book_price')";
                mysqli_query($conn, $query_details); 
            }

            $conn->commit();

            unset($_SESSION['cart']);

            header('Location: order_success.php'); 
            exit;

        } catch (Exception $e) {
            $conn->rollback();
            $message = "Đã có lỗi xảy ra trong quá trình đặt hàng. Vui lòng thử lại.";
        }
    }
}
?>
<div class="checkout-container" style="width: 60%; margin: auto; padding: 20px;">
    <h2>Thông tin thanh toán</h2>
    
    <?php if ($message) echo $message; ?>

    <form action="checkout.php" method="POST">
        <div style="margin-bottom: 15px;">
            <label for="customer_name">Họ và Tên:</label><br>
            <input type="text" id="customer_name" name="customer_name" required style="width: 100%; padding: 8px;" value="<?= htmlspecialchars($customer_name) ?>">
        </div>
        <div style="margin-bottom: 15px;">
            <label for="customer_email">Email:</label><br>
            <input type="email" id="customer_email" name="customer_email" required style="width: 100%; padding: 8px;" value="<?= htmlspecialchars($customer_email) ?>">
        </div>
        <div style="margin-bottom: 15px;">
            <label for="customer_phone">Số điện thoại:</label><br>
            <input type="tel" id="customer_phone" name="customer_phone" required style="width: 100%; padding: 8px;" value="<?= htmlspecialchars($customer_phone) ?>">
        </div>
        <div style="margin-bottom: 15px;">
            <label for="customer_address">Địa chỉ giao hàng:</label><br>
            <textarea id="customer_address" name="customer_address" required style="width: 100%; padding: 8px; height: 80px;"><?= htmlspecialchars($customer_address) ?></textarea>
        </div>

        <h3>Tóm tắt đơn hàng</h3>
        <table border="1" style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
                <tr><th>Sản phẩm</th><th>Số lượng</th><th>Giá</th></tr>
            </thead>
            <tbody>
                <?php 
                $total_price = 0;
                foreach($_SESSION['cart'] as $book_id => $book): 
                    $total_price += $book['price'] * $book['quantity'];
                ?>
                <tr>
                    <td><?= htmlspecialchars($book['title']) ?></td>
                    <td><?= $book['quantity'] ?></td>
                    <td><?= number_format($book['price'] * $book['quantity']) ?> VNĐ</td>
                </tr>
                <?php endforeach; ?>
            </tbody>
            <tfoot>
                <tr>
                    <th colspan="2" style="text-align: right;">Tổng cộng:</th>
                    <th><?= number_format($total_price) ?> VNĐ</th>
                </tr>
            </tfoot>
        </table>

        <div style="text-align: center; margin-top: 20px;">
            <button type="submit" style="padding: 12px 25px; background-color: #28a745; color: white; border: none; font-size: 1.1em; cursor: pointer;">Xác nhận và Đặt hàng</button>
        </div>
    </form>
</div>

<?php include 'footer.php'; ?>
