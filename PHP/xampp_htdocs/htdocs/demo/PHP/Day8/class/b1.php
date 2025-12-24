<?php

$products = [
    ["id" => 1, "name" => "laptop","price" =>1500],
    ["id" => 2,"name"=>"smartphone","price" => 2000],
    ["id" =>3, "name" => "headphone","price"=>4000],
];

?>

<form action="checkout.php" method="POST">
    <h2>Danh sach san pham</h2>
    <?php 
        foreach ($products as $product): ?>
        <div>
            <strong><label for=""><?= $product['name'] ?></label>
            <label for="">Gia san pham: (<?= $product['price'] ?>$)</label></strong><br>
            <input type="number" name="quantity[<?= $product['id'] ?>]" value="0" min="0">
        </div>

        <?php endforeach; ?>
        <br>
        Ten khach hang: <input type="text" name="customer_name" required ><br><br>
        <button type="submit">Thanh toan</button>
</form>