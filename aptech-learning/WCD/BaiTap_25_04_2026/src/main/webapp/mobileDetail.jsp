<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%@ taglib uri="jakarta.tags.fmt" prefix="fmt" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mobile Detail</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .detail-container { display: flex; gap: 30px; margin-top: 20px; }
        .detail-info { font-size: 16px; line-height: 1.6; }
    </style>
</head>
<body>
    <h2>Mobile Detail</h2>
    <a href="home">Home</a>
    <hr>
    
    <c:if test="${not empty mobile}">
        <div class="detail-container">
            <div>
                <img src="${mobile.image}" width="250" alt="${mobile.name}" onerror="this.src='https://via.placeholder.com/250x350?text=No+Image'"/>
            </div>
            <div class="detail-info">
                <p><b>Mobile Name:</b> ${mobile.name}</p>
                <p><b>Price:</b> <fmt:formatNumber value="${mobile.price}" type="currency" currencySymbol="$"/></p>
                <p><b>Warranty:</b> ${mobile.warranty}</p>
                <p><b>Accessories:</b> ${mobile.accessories}</p>
                <p><b>In/Out Stock:</b> 
                    <span style="color: ${mobile.inOutStock ? 'green' : 'red'}; font-weight: bold;">
                        ${mobile.inOutStock ? 'In Stock' : 'Out of Stock'}
                    </span>
                </p>
            </div>
        </div>
    </c:if>
    <c:if test="${empty mobile}">
        <p>Mobile not found!</p>
    </c:if>
</body>
</html>
