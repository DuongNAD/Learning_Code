$(document).ready(function () {
    let productList = JSON.parse(localStorage.getItem("products")) || [];

    function displayProducts() {
        $("#productTableBody").empty();

        productList.forEach((product, index) => {
            let row = `<tr>
                <td>${product.nameProduct}</td>
                <td>${product.priceProduct}</td>
                <td>${product.quantityProduct}</td>
                <td>${product.descriptionProduct}</td>
                <td>
                    <button class="edit-btn" data-index="${index}">Sửa</button>
                    <button class="delete-btn" data-index="${index}">Xóa</button>
                </td>
            </tr>`;
            $("#productTableBody").append(row);
        });

        localStorage.setItem("products", JSON.stringify(productList));
    }

    $("#addProduct").click(function(){
        let name = $("#nameProduct").val().trim();
        let price = parseFloat($("#priceProduct").val());
        let quantity = parseInt($("#quantityProduct").val());
        let description = $("#descriptionProduct").val().trim();

        if (name === "" || name.length > 50) {
            alert("Tên sản phẩm không được để trống và tối đa 50 ký tự!");
            return;
        }
       
        if (isNaN(price) || price <= 0) {
            alert("Giá sản phẩm phải là số dương!");
            return;
        }

        if (isNaN(quantity) || quantity < 1) {
            alert("Số lượng phải là số nguyên dương!");
            return;
        }

        productList.push({
            nameProduct: name,
            priceProduct: price,
            quantityProduct: quantity,
            descriptionProduct: description
        });

        displayProducts();
        $("#productForm")[0].reset();
        $("#updateIndex").val("");
    });

    $(document).on("click", ".edit-btn", function(){
        let index = $(this).data("index");
        let product = productList[index];

        $("#nameProduct").val(product.nameProduct);
        $("#priceProduct").val(product.priceProduct);
        $("#quantityProduct").val(product.quantityProduct);
        $("#description").val(product.descriptionProduct);
        $("#updateIndex").val(index);

        $("#addProduct").hide();
        $("#updateProduct").show();
    });

    $("#updateProduct").click(function () {
        let index = $("#updateIndex").val();
        let name = $("#nameProduct").val().trim();
        let price = parseFloat($("#priceProduct").val());
        let quantity = parseInt($("#quantityProduct").val());
        let description = $("#description").val().trim();

        if (name === "" || name.length > 50 || isNaN(price) || price <= 0 || isNaN(quantity) || quantity < 1) {
            alert("Dữ liệu không hợp lệ!");
            return;
        }

        productList[index] = { 
            nameProduct: name, 
            priceProduct: price, 
            quantityProduct: quantity, 
            descriptionProduct: description 
        };
        
        displayProducts();
        $("#productForm")[0].reset();
        $("#updateIndex").val("");
        $("#addProduct").show();
        $("#updateProduct").hide();
    });

    $(document).on("click", ".delete-btn", function () {
        let index = $(this).data("index");

        if (confirm("Bạn có chắc muốn xóa sản phẩm này?")) {
            productList.splice(index, 1);
            displayProducts();
        }
    });

    $("#updateProduct").hide(); // Ẩn nút "Cập nhật" khi tải trang
    displayProducts();
});
