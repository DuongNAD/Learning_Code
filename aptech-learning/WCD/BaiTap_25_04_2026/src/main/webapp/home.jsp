<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%@ taglib uri="jakarta.tags.fmt" prefix="fmt" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Home</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .product-grid { display: flex; flex-wrap: wrap; gap: 20px; margin-top: 20px; }
        .product-card { border: 1px solid #ccc; padding: 15px; text-align: center; width: 150px; border-radius: 8px; }
        .product-card img { max-width: 100%; height: 150px; object-fit: cover; cursor: pointer; }
        .price { color: #e74c3c; font-weight: bold; margin-top: 10px; }
    </style>
</head>
<body>
    <h2>Mobile Store</h2>
    <a href="insert">Insert New Product</a>
    <hr>
    
    <div class="product-grid">
        <c:forEach var="mobile" items="${listMobile}">
            <div class="product-card">
                <!-- Each image is a link to detail page -->
                <a href="detail?id=${mobile.id}">
                    <img src="${mobile.image}" alt="${mobile.name}" onerror="this.src='https://via.placeholder.com/100x150?text=No+Image'"/>
                </a>
                <div style="margin-top: 10px;">
                    <b>${mobile.name}</b>
                </div>
                <div class="price">
                    <fmt:formatNumber value="${mobile.price}" type="currency" currencySymbol="$"/>
                </div>
            </div>
        </c:forEach>
    </div>
</body>
</html>
