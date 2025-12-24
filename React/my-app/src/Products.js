import React from "react";

const Products = () =>{
    const productList =[
        {id:1, name: 'Sản phẩm 1', price: 100},
        {id:2, name: 'Sản phẩm 2', price: 200},
        {id:3, name: 'Sản phẩm 3', price: 300}
    ];

    return(
        <div>
            <h1>Danh sách sản phẩm</h1>

            <ul>
                {productList.map((product) => (
                    <li key={product.id} style={{marginBottom: '10px'}}>
                        <strong>{product.name}</strong> - Giá: {product.price}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Products;