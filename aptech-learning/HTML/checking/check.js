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
      } else {
        console.error("Invalid product");
      }
    }
  }
  
  class Product {
    constructor(id, name, price, oldPrice, description, image, category = null) {
      this.id = id;
      this.name = name;
      this.price = price;
      this.oldPrice = oldPrice;
      this.description = description;
      this.image = image;
      this.category = category;
    }
  }
  
  const categories = [];
  const products = [];
  
  function generateRandomId() {
    return Math.floor(Math.random() * 1000000) + 1;
  }
  
  // Xử lý form thêm danh mục
  document.getElementById("categoryForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const name = document.getElementById("catNameInput").value;
    const description = document.getElementById("catDescInput").value;
    const id = generateRandomId();
    const category = new Category(id, name, description);
    categories.push(category);
    updateCategoryList();
    updateCategoryDropdown();
  
    // Xóa dữ liệu trong form
    document.getElementById("catNameInput").value = "";
    document.getElementById("catDescInput").value = "";
  });
  
  function updateCategoryList() {
    const categoryList = document.getElementById("categoryList");
    categoryList.innerHTML = "";
    categories.forEach(category => {
      const li = document.createElement("li");
      li.textContent = `${category.name} - ${category.description}`;
      categoryList.appendChild(li);
    });
  }
  
  function updateCategoryDropdown() {
    const categoryDropdown = document.getElementById("prodCategory");
    // Tạo option mặc định
    categoryDropdown.innerHTML = `<option value="">-- Chọn Category --</option>`;
    categories.forEach(category => {
      const option = document.createElement("option");
      option.value = category.id;
      option.textContent = category.name;
      categoryDropdown.appendChild(option);
    });
  }
  
  // Xử lý form thêm sản phẩm
  document.getElementById("productForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const name = document.getElementById("prodName").value;
    const price = parseFloat(document.getElementById("prodPrice").value);
    const oldPrice = parseFloat(document.getElementById("prodOldPrice").value) || 0;
    const description = document.getElementById("prodDesc").value;
    const image = document.getElementById("prodImage").value;
    const categoryId = parseInt(document.getElementById("prodCategory").value);
    const category = categories.find(cat => cat.id === categoryId);
  
    if (!category) {
      alert("Vui lòng chọn một danh mục hợp lệ.");
      return;
    }
  
    const id = generateRandomId();
    const product = new Product(id, name, price, oldPrice, description, image, category);
  
    // Thêm sản phẩm vào mảng products và danh mục tương ứng
    products.push(product);
    category.addProduct(product);
  
    updateProductList();
  
    // Xóa dữ liệu trong form sản phẩm
    document.getElementById("prodName").value = "";
    document.getElementById("prodPrice").value = "";
    document.getElementById("prodOldPrice").value = "";
    document.getElementById("prodDesc").value = "";
    document.getElementById("prodImage").value = "";
    document.getElementById("prodCategory").value = "";
  });
  
  function updateProductList() {
    const productList = document.getElementById("productList");
    productList.innerHTML = "";
    products.forEach(product => {
      const li = document.createElement("li");
      li.textContent = `${product.name} - ${product.price} (Danh mục: ${product.category.name})`;
      productList.appendChild(li);
    });
  }
  