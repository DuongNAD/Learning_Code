const laptop = [
    {
        name: "laptop - Dell XPS 13",
        price: 49000000,
    },
    {
        name: "MacBook Pro 16 M4 ",
        price: 102000000
    },
    {
        name: "Laptop Lenovo Gaming Legion 5 Pro ",
        price: 51500000,
    },
]
const smart_phone = [
    {
        name: "Sam Sung S24 Untra",
        price: 40000000,
    },
    {
        name: "Samsung Galaxy Z Fold6",
        price: 31500000,
    },

    {
        name: "Iphone 16 Promax",
        price: 30000000,
    },
]

const other_items = [
    {
        name: "Keyboard",
        price: 1300000,
    },

    {
        name: "Mouse",
        price: 750000,
    },
    {
        name: "Tai nghe Bluetooth True Wireless Huawei FreeBuds 5i",
        price: 840000,
    },
]

function displaylaptop (items,containerID){  
    const container =  document.getElementById(containerID);
    container.innerHTML = "";

    const table = document.createElement("table");
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");

    const headers = [
        "Name",
        "Price",
    ];
    headers.forEach(headerText => {
        const th = document.createElement("th");
        th.textContent = headerText;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);

    const tbody = document.createElement("tbody");

    items.forEach(item => {
        const row = document.createElement("tr");

        const tdName = document.createElement("td");
        tdName.textContent = item.name;
        tdName.classList.add("col-name");
        row.appendChild(tdName);

        const tdPrice = document.createElement("td");
        tdPrice.textContent = item.price.toLocaleString("vi-VN");
        tdPrice.classList.add("col-price");
        row.appendChild(tdPrice);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);
    container.appendChild(table);
}

displaylaptop(laptop, "ItemContainer");

const form = document.getElementById("ItemForm");
form.addEventListener("submit", function(event) {
  event.preventDefault(); 

  const nameInput = document.getElementById("ItemName");
  const priceInput = document.getElementById("ItemPrice");

  const newName = nameInput.value.trim();
  const newPrice = Number(priceInput.value);


  if (newName && newPrice>0) {
    const newItem = {
      name: newName,
      price: newPrice
    };

    laptop.push(newItem);

    displaylaptop(laptop, "ItemContainer");

    nameInput.value = "";
    priceInput.value = "";
  }
});