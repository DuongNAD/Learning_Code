<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Library System</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<div class="container">
    <h2>Library Book Borrowing System</h2>
    <nav>
        <a href="${pageContext.request.contextPath}/books">Book Inventory</a>
        <a href="${pageContext.request.contextPath}/add-book">Add New Book</a>
        <a href="${pageContext.request.contextPath}/borrowers">Borrowers List</a>
        <a href="${pageContext.request.contextPath}/add-borrower">Register Borrower</a>
    </nav>
    <p>Welcome to the Library System. Please select an option from the menu.</p>
</div>
</body>
</html>
