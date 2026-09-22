<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.exercise.dao.GroupDAO" %>
<%@ page import="com.exercise.entity.Group" %>
<%@ page import="java.util.List" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%
    GroupDAO groupDAO = new GroupDAO();
    List<Group> groupsList = groupDAO.getAllGroups();
    request.setAttribute("groupsList", groupsList);
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Contact</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Add a Contact</h1>
        <p class="subtitle">Create a new contact entry in the directory</p>

        <form action="ContactServlet?action=add" method="POST" id="contactForm">
            <div class="form-group">
                <label for="firstName">First Name:</label>
                <input type="text" id="firstName" name="firstName" class="input-control" value="${firstNameVal}">
                <c:if test="${not empty firstNameError}">
                    <span class="error-msg">${firstNameError}</span>
                </c:if>
            </div>

            <div class="form-group">
                <label for="lastName">Last Name:</label>
                <input type="text" id="lastName" name="lastName" class="input-control" value="${lastNameVal}">
                <c:if test="${not empty lastNameError}">
                    <span class="error-msg">${lastNameError}</span>
                </c:if>
            </div>

            <div class="form-group">
                <label for="groupId">Group:</label>
                <select id="groupId" name="groupId" class="input-control">
                    <c:forEach var="g" items="${groupsList}">
                        <option value="${g.id}" <c:if test="${g.id == groupIdVal}">selected</c:if>>${g.name} - ${g.description}</option>
                    </c:forEach>
                </select>
            </div>

            <div class="form-group">
                <label for="phoneNumber">Phone Number:</label>
                <input type="text" id="phoneNumber" name="phoneNumber" class="input-control" value="${phoneNumberVal}">
                <c:if test="${not empty phoneNumberError}">
                    <span class="error-msg">${phoneNumberError}</span>
                </c:if>
            </div>

            <div class="btn-group">
                <button type="submit" class="btn btn-primary" id="btnAdd">Add</button>
                <a href="ContactServlet?action=list" class="btn btn-secondary" id="btnReturn">Return To Contact List</a>
            </div>
        </form>
    </div>
</body>
</html>
