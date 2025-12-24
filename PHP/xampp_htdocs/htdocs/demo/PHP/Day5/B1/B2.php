<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cửa hàng điện tử</title> <style>

        .header { 
            display: flex; 
            justify-content: space-between; 
            align-items: center;
            padding: 10px 20px;
            background-color: #f0f0f0; 
            border-bottom: 1px solid #ccc; 
        }

        .header h2 {
            margin: 0; 
        }

        .header a {
            text-decoration: none; 
            color: blue; 
        }


        .products-container { 
            display: flex; 
            flex-wrap: wrap; 
            gap: 20px; 
            padding: 20px;
            justify-content: center; 
        }

        .product-card { 
            border: 1px solid #ccc; 
            border-radius: 8px; 
            padding: 15px;
            width: 200px; 
            text-align: center; 
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); 
            background-color: #fff; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
        }

        .product-card img {
            max-width: 100%; 
            height: 150px;
            object-fit: cover; 
            border-radius: 4px; 
            margin-bottom: 10px; 
        }

        .product-card .product-name,
        .product-card .product-detail, 
        .product-card .product-price { 
            margin-bottom: 8px; 
            font-size: 1em;
            color: #333;
        }

        .product-card .product-price {
            font-weight: bold; 
            color: #e44d26;
        }


        .product-card a.view-button,
        .product-card button.add-to-cart-button { 
             display: inline-block; 
             padding: 8px 15px;
             background-color: red;
             color: white;
             text-decoration: none; 
             border: none; 
             border-radius: 5px;
             cursor: pointer;
             margin-top: 5px; 
             width: 90%; 
             text-align: center; 
             box-sizing: border-box; 
        }

        .product-card button.add-to-cart-button {
            background-color: #e44d26; 
             margin-top: 10px; 
        }
    </style>
</head>
<body>
    <div class="header"> 
        <div><h2>Cửa hàng điện tử</h2></div>
        <div class="tool">
            <div><a href="">Giỏ hàng</a></div>
            <div><a href="themproduct">Thêm sản phẩm</a></div>
        </div>
    </div>

    <div class="products-container"> <div class="product-card"> <div>
            <img src="/demo/Day3/class/imgpro/img1.jpg" alt="Ảnh sản phẩm"> </div>
            <div class="product-name">Sản phẩm</div> <div class="product-detail">Tel</div> 
            <div class="product-price">310.000 VND</div> <a href="" class="view-button">Xem</a> <form action="" method="post">
            <input type="hidden" name="product_id" value="ID_cua_san_pham">
            <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button> </form>
        </div>

        <div class="product-card">
            <div><img src="/demo/Day3/class/imgpro/img2.jpg" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Nak</div>
            <div class="product-price">100.000 VND</div>
            <a href="" class="view-button">Xem</a>
            <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button>
            </form>
        </div>

         <div class="product-card">
            <div><img src="/demo/Day3/class/imgpro/img3.jpg" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Raz</div>
            <div class="product-price">160.000 VND</div>
            <a href="" class="view-button">Xem</a>
            <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button>
            </form>
        </div>

        <div class="product-card">
            <div><img src="/demo/Day3/class/imgpro/img4.jpg" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Ryo</div>
            <div class="product-price">210.000 VND</div>
            <a href="" class="view-button">Xem</a>
            <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button>
            </form>
        </div>
        </div>

        <?php   
            if($_SERVER["REQUEST_METHOD"] == "POSt" && isset($_POST['add-to-cart-button'])){
                $product_id = $_POST['product_id'];
                if (!isset($_SESSION['cart'])){
                    $_SESSION['cart'] = array();
                }

                $count =1;
                if(isset($_SESSION['cart'][$product_id])){
                    $_SESSION['cart'][$product_id] += $count;
                }
                else{
                    $_SESSION['cart'][$product_id] = $count;
                }
                header('Location: giohang.php'); 
                exit();
            }

        ?>
</body>
</html>