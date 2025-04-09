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

const randomId = generateRandomId();
console.log(randomId);
document.getElementById("categoryForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const name = document.getElementById("catNameInput").value;
  const description = document.getElementById("catDescInput").value;
  const id = generateRandomId();
  const category = new Category(id, name, description);
  categories.push(category);
  updateCategoryList();
  updateCategoryDropdown();

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
  categoryDropdown.innerHTML = `<option value ="">-- Chọn Category --</option>`;

  categories.forEach(category => {
    const option = document.createElement("option");
    option.value = String(category.id);
    option.textContent = category.name;
    categoryDropdown.appendChild(option);
  });
}

document.getElementById("productForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const name = document.getElementById("prodName").value;
  const price = parseFloat(document.getElementById("prodPrice").value);
  const oldPriceInput = document.getElementById("prodOldPrice").value;
  const oldPrice = oldPriceInput ? parseFloat(oldPriceInput) : 0;
  const description = document.getElementById("prodDesc").value;
  const image = document.getElementById("prodImage").value;
  const categoryId = Number(document.getElementById("prodCategory").value);
  const category = categories.find(cat => cat.id === categoryId);

  if (!name || isNaN(price) || price <= 0) {
    alert("Vui lòng nhập tên sản phẩm và giá hợp lệ!");
    return;
  }

  if (!category) {
    alert("Vui long chon mot danh muc hop le");
    return;
  }

  const id = generateRandomId();
  const product = new Product(id, name, price, oldPrice, description, image, category);

  products.push(product);
  category.addProduct(product);

  updateProductList();

  document.getElementById("prodName").value = "";
  document.getElementById("prodPrice").value = "";
  document.getElementById("prodOldPrice").value = "";
  document.getElementById("prodDesc").value = "";
  document.getElementById("prodImage").value = "";
  document.getElementById("prodCategory").selectedIndex = 0;
});

function updateProductList() {
  const productList = document.getElementById("productList");
  productList.innerHTML = "";
  const container = document.createElement("div");
  container.classList.add("flex-container");

  productList.appendChild(container);

  categories.forEach(category => {
    if (category.products.length > 0) {
      const categoryColumn = document.createElement("div");
      categoryColumn.classList.add("category-column");

      container.appendChild(categoryColumn);

      const categoryTitle = document.createElement("h3");
      categoryTitle.textContent = `Danh mục: ${category.name}`;
      categoryTitle.style.color = "blue";
      categoryColumn.appendChild(categoryTitle);

      category.products.forEach(product => {
        const productItem = document.createElement("li");
        productItem.innerHTML = `
          <b>${product.name}</b> - <span style="color:green;">Giá: ${product.price}đ</span> 
          <span style="color:red; text-decoration: line-through;">${product.oldPrice}đ</span> <br>
          <i>Danh mục: ${category.name}</i><br>
          ${product.description}<br>
          <img src="${product.image}" alt="${product.name}" style="max-width:150px; display:block; margin-top:5px;">
        `;
        categoryColumn.appendChild(productItem);
      });
    }
  });
}
