class Category {
    constructor(id, name, description) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.products = [];
    }
    addProduct(product) {
        if (product instanceof Product) {
            this.products.push(product);
            product.category = this;
        }
        else {
            console.error("Invalid product");
        }
    }
}

class Product {
    constructor(id, name, price, oldPrice, category = null, description, image) {
        this.id = id;
        this.name = name;
        this.description = description;
        this.price = price;
        this.oldPrice = oldPrice;
        this.category = category;
        this.image = image;
    }
}

const categories = [];
const products = [];

function randomId() {
    return Math.floor(Math.random() * 100000) + 1;
}
$(document).ready(function () {
    $("#categoryForm").submit(function (event) {
        event.preventDefault();

        let name = $("#nameCategory").val().trim();
        let description = $("#description").val().trim();

        if (name === "" || description === "") {
            alert("Vui long nhap day du thong tin");
            return;
        }

        let category = new Category(randomId(), name, description);
        categories.push(category);

        localStorage.setItem('categories', JSON.stringify(categories));

        $("#categorySelect").append(`<option value="${category.id}">${category.name}</option>`);

        $("#categoriesContainer").append(`
            <div class="category-block" id="category-${category.id}">
                <h3>${category.name}</h3>
                <p>${category.description}</p>
                <div class="product-list" id="product-list-${category.id}">
                    <!-- Sản phẩm sẽ hiển thị tại đây -->
                </div>
            </div>
        `);

        $("#nameCategory").val("");
        $("#description").val("");

        console.log("Danh sách danh mục:", categories);
    });

    $("#productForm").submit(function (event) {
        event.preventDefault();

        let name = $("#nameProduct").val().trim();
        let price = parseFloat($("#priceProduct").val());
        let oldPrice = parseFloat($("#oldpriceProduct").val());
        let description = $("#descriptionProduct").val().trim();
        let image = $("#imageProduct").val().trim();
        let categoryId = $("#categorySelect").val().trim();

        if (name === "" || price === "" || oldPrice === "" || description === "" || image === "" || categoryId === "") {
            alert("Vui long nhap thong tin san pham");
            return;
        }

        let category = categories.find(cat => cat.id == categoryId);
        let product = new Product(randomId(), name, price, oldPrice, category, description, image);
        products.push(product);
localStorage.setItem('products', JSON.stringify(products));
        if (category) {
            category.addProduct(product);
        }
        $(`#product-list-${category.id}`).append(`
            <div class="product-item">
                <img src="${product.image}" alt="${product.name}" />
                <p><strong>${product.name}</strong></p>
                <p>Giá cũ: <s>${product.oldPrice} VNĐ</s></p>
                <p>Giá mới: <strong>${product.price} VNĐ</strong></p>
                <p>Mô tả: ${product.description}</p>
            </div>
        `);
        $("#productForm")[0].reset();

        console.log("Danh sach san pham", products);
    });
});