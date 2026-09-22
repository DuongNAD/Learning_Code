<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <title>Borrower List</title>
    <link rel="stylesheet" type="text/css" href="${pageContext.request.contextPath}/css/style.css">
</head>
<body>
<div class="container">
    <h2>Borrowers List</h2>
    <nav>
        <a href="${pageContext.request.contextPath}/">Home</a>
        <a href="${pageContext.request.contextPath}/add-borrower">Register Borrower</a>
    </nav>
    <form action="${pageContext.request.contextPath}/borrowers" method="get">
        <div class="form-group">
            <label>Select Book to view borrowers:</label>
            <select name="bookId" onchange="this.form.submit()">
                <option value="">-- Select a Book --</option>
                <c:forEach var="book" items="${books}">
                    <option value="${book.id}" ${param.bookId == book.id ? 'selected' : ''}>
                        ${book.title}
                    </option>
                </c:forEach>
            </select>
        </div>
    </form>

    <c:if test="${not empty param.bookId}">
        <h3>Borrowers for "${selectedBook.title}"</h3>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <c:forEach var="borrower" items="${borrowers}">
                    <tr>
                        <td>${borrower.id}</td>
                        <td>${borrower.name}</td>
                        <td>${borrower.email}</td>
                    </tr>
                </c:forEach>
                <c:if test="${empty borrowers}">
                    <tr><td colspan="3" style="text-align:center">No borrowers yet</td></tr>
                </c:if>
            </tbody>
        </table>
    </c:if>
</div>
</body>
</html>
