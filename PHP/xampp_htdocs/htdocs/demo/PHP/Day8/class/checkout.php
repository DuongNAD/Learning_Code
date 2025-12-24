<?php
$products   =[
    ["id" => 1, "name" => "laptop","price" =>1500],
    ["id" => 2,"name"=>"smartphone","price" => 2000],
    ["id" =>3, "name" => "headphone","price"=>4000],
];

$conn = new mysqli('locahost','root','','managerment_products');
if($conn->connect_error) die("ket noi that bai" . $conn->connect_error);

$customer_name = $_POST['customer_name'];
$quantity = $_POST['quantity'];

$conn -> query("insert into orders (customer_name) values ('$customer_name')");
$order_id = $conn->insert_id;

foreach ($products as $product){
    $id = $product['id'];
    $quantity = (int)($quantities[$id] ?? 0);
    if ($quantity >0){
        $name = $conn->real_escape_string(($product['name']));
        $conn->query("insert into order_details (order_id,product_name,quantity) values ('$order_id','$name','$quantity')");
    }
}

echo "Don hang cua ban da dc tao thanh cong";
$conn->close();
?>