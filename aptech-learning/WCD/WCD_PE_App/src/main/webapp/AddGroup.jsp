<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Group</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Add a Group</h1>
        <p class="subtitle">Create a new contact categorization group</p>

        <form action="ContactServlet?action=addGroup" method="POST" id="groupForm">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" class="input-control" value="${nameVal}">
                <c:if test="${not empty nameError}">
                    <span class="error-msg">${nameError}</span>
                </c:if>
            </div>

            <div class="form-group">
                <label for="description">Description:</label>
                <input type="text" id="description" name="description" class="input-control" value="${descriptionVal}">
                <c:if test="${not empty descriptionError}">
                    <span class="error-msg">${descriptionError}</span>
                </c:if>
            </div>

            <div class="btn-group">
                <button type="submit" class="btn btn-primary" id="btnGroupAdd">Add</button>
                <a href="ContactServlet?action=listGroups" class="btn btn-secondary" id="btnReturnGroupList">Return To Group List</a>
            </div>
        </form>
    </div>
</body>
</html>
