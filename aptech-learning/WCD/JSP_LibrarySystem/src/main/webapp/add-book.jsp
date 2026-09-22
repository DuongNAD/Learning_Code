<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <title>Add New Book</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<div class="container">
    <h2>Add New Book</h2>
    <nav>
        <a href="${pageContext.request.contextPath}/">Home</a>
        <a href="${pageContext.request.contextPath}/books">Book Inventory</a>
    </nav>
    <c:if test="${not empty error}">
        <div class="error">${error}</div>
    </c:if>
    <form action="${pageContext.request.contextPath}/add-book" method="post">
        <div class="form-group">
            <label>Title:</label>
            <input type="text" name="title" required minlength="3">
        </div>
        <div class="form-group">
            <label>Author:</label>
            <input type="text" name="author" required>
        </div>
        <div class="form-group">
            <label>Total Copies:</label>
            <input type="number" name="totalCopies" required min="1">
        </div>
        <button type="submit" class="btn btn-primary">Add Book</button>
    </form>
</div>
</body>
</html>
