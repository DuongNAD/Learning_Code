<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Danh Mục Sản Phẩm</title>
</head>
<body>

    <h2>Danh Mục Sản Phẩm</h2>
    
    <ul>
        <c:forEach var="category" items="${categoryList}">
            <li>${category}</li>
        </c:forEach>
    </ul>

</body>
</html>
