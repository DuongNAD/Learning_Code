<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cửa hàng điện tử</title> <style>
        /* --- CSS cho phần Header --- */
        .header { /* Tạo một class để dễ style */
            display: flex; /* Dùng flexbox để các mục nằm ngang */
            justify-content: space-between; /* Đẩy "Cửa hàng điện tử" và "Giỏ hàng" ra hai bên */
            align-items: center; /* Căn giữa theo chiều dọc */
            padding: 10px 20px;
            background-color: #f0f0f0; /* Màu nền nhẹ */
            border-bottom: 1px solid #ccc; /* Đường viền dưới */
        }

        .header h2 {
            margin: 0; /* Bỏ margin mặc định của h2 */
        }

        .header a {
            text-decoration: none; /* Bỏ gạch chân link */
            color: blue; /* Màu link */
        }


        /* --- CSS cho Container chứa các sản phẩm --- */
        .products-container { /* Tạo một class cho div chứa tất cả sản phẩm */
            display: flex; /* Bật chế độ flexbox */
            flex-wrap: wrap; /* Cho phép các item xuống dòng khi hết chỗ */
            gap: 20px; /* Tạo khoảng cách giữa các sản phẩm */
            padding: 20px;
            justify-content: center; /* Căn giữa các sản phẩm nếu tổng chiều rộng nhỏ hơn container */
        }

        /* --- CSS cho từng Product Card --- */
        .product-card { /* Tạo một class cho mỗi div sản phẩm */
            border: 1px solid #ccc; /* Đường viền cho card */
            border-radius: 8px; /* Bo góc nhẹ */
            padding: 15px;
            width: 200px; /* Đặt chiều rộng cố định cho mỗi card (có thể điều chỉnh) */
            text-align: center; /* Căn giữa nội dung bên trong card */
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1); /* Thêm bóng đổ nhẹ */
            background-color: #fff; /* Nền trắng cho card */
            display: flex; /* Dùng flexbox để các mục bên trong card xếp dọc */
            flex-direction: column; /* Xếp các mục theo cột */
            align-items: center; /* Căn giữa các mục theo chiều ngang trong cột */
        }

        .product-card img {
            max-width: 100%; /* Ảnh không vượt quá chiều rộng của card */
            height: 150px; /* Chiều cao cố định cho ảnh */
            object-fit: cover; /* Cắt ảnh để vừa với kích thước mà không bị méo */
            border-radius: 4px; /* Bo góc ảnh nhẹ */
            margin-bottom: 10px; /* Khoảng cách dưới ảnh */
        }

        .product-card .product-name,
        .product-card .product-detail, /* Đổi tên class cho rõ nghĩa */
        .product-card .product-price { /* Đổi tên class cho rõ nghĩa */
            margin-bottom: 8px; /* Khoảng cách dưới mỗi dòng text */
            font-size: 1em; /* Kích thước chữ mặc định */
            color: #333;
        }

        .product-card .product-price {
            font-weight: bold; /* Giá in đậm */
            color: #e44d26; /* Màu đỏ cam cho giá */
        }


        /* --- CSS cho các nút (Xem, Thêm vào giỏ hàng) --- */
        .product-card a.view-button, /* Tạo class cho nút Xem */
        .product-card button.add-to-cart-button { /* Tạo class cho nút Thêm */
             display: inline-block; /* hoặc block nếu muốn chúng xếp chồng */
             padding: 8px 15px;
             background-color: red;
             color: white;
             text-decoration: none; /* Dành cho thẻ a */
             border: none; /* Dành cho button */
             border-radius: 5px;
             cursor: pointer;
             margin-top: 5px; /* Khoảng cách trên các nút */
             width: 90%; /* Chiều rộng gần bằng card */
             text-align: center; /* Căn giữa text trong nút */
             box-sizing: border-box; /* Đảm bảo padding không làm tăng width */
        }

        .product-card button.add-to-cart-button {
            background-color: #e44d26; /* Màu đỏ cam khác */
             margin-top: 10px; /* Khoảng cách thêm cho nút giỏ hàng */
        }

    </style>
</head>
<body>
    <div class="header"> <div><h2>Cửa hàng điện tử</h2></div>
        <div><a href="">Giỏ hàng</a></div>
        <div><a href="themproduct">Thêm sản phẩm</a></div>
    </div>

    <div class="products-container"> <div class="product-card"> <div>
                <img src="" alt="Ảnh sản phẩm"> </div>
            <div class="product-name">Sản phẩm</div> <div class="product-detail">Tel</div> <div class="product-price">10.000 VND</div> <a href="" class="view-button">Xem</a> <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button> </form>
        </div>

        <div class="product-card">
            <div><img src="" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Nak</div>
            <div class="product-price">10.000 VND</div>
            <a href="" class="view-button">Xem</a>
            <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button>
            </form>
        </div>

         <div class="product-card">
            <div><img src="" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Raz</div>
            <div class="product-price">10.000 VND</div>
            <a href="" class="view-button">Xem</a>
            <form action="" method="post">
                <input type="hidden" name="product_id" value="ID_cua_san_pham">
                <button type="submit" class="add-to-cart-button">Thêm vào giỏ hàng</button>
            </form>
        </div>

        <div class="product-card">
            <div><img src="" alt="Ảnh sản phẩm"></div>
            <div class="product-name">Sản phẩm</div>
            <div class="product-detail">Ryo</div>
            <div class="product-price">10.000 VND</div>
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