<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <title>Register Borrower</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<div class="container">
    <h2>Register Borrower</h2>
    <nav>
        <a href="${pageContext.request.contextPath}/">Home</a>
        <a href="${pageContext.request.contextPath}/borrowers">Borrowers List</a>
    </nav>
    <c:if test="${not empty error}">
        <div class="error">${error}</div>
    </c:if>
    <form action="${pageContext.request.contextPath}/add-borrower" method="post">
        <div class="form-group">
            <label>Name:</label>
            <input type="text" name="name" required minlength="3">
        </div>
        <div class="form-group">
            <label>Email:</label>
            <input type="email" name="email" required>
        </div>
        <div class="form-group">
            <label>Select Book:</label>
            <select name="bookId" required>
                <c:forEach var="book" items="${books}">
                    <option value="${book.id}">${book.title} (${book.author})</option>
                </c:forEach>
            </select>
        </div>
        <button type="submit" class="btn btn-primary">Add Borrower</button>
    </form>
</div>
</body>
</html>
