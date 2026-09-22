<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.exercise.dao.GroupDAO" %>
<%@ page import="com.exercise.dao.ContactDAO" %>
<%@ page import="com.exercise.entity.Group" %>
<%@ page import="com.exercise.entity.Contact" %>
<%@ page import="java.util.List" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%
    GroupDAO groupDAO = new GroupDAO();
    List<Group> groupsList = groupDAO.getAllGroups();
    request.setAttribute("groupsList", groupsList);

    if (request.getAttribute("contact") == null) {
        String idStr = request.getParameter("id");
        if (idStr != null) {
            try {
                int id = Integer.parseInt(idStr);
                ContactDAO contactDAO = new ContactDAO();
                Contact contact = contactDAO.getContactById(id);
                request.setAttribute("contact", contact);
            } catch (Exception e) {
                // ignore
            }
        }
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit a Contact</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>Edit a Contact</h1>
        <p class="subtitle">Modify an existing contact entry</p>

        <c:choose>
            <c:when test="${not empty contact}">
                <form action="ContactServlet?action=edit" method="POST" id="editForm">
                    <input type="hidden" name="id" value="${contact.id}">

                    <div class="form-group">
                        <label for="idDisplay">ID:</label>
                        <input type="text" id="idDisplay" class="input-control" value="${contact.id}" disabled style="opacity: 0.6; cursor: not-allowed;">
                    </div>

                    <div class="form-group">
                        <label for="firstName">First Name:</label>
                        <input type="text" id="firstName" name="firstName" class="input-control" value="${contact.firstName}">
                        <c:if test="${not empty firstNameError}">
                            <span class="error-msg">${firstNameError}</span>
                        </c:if>
                    </div>

                    <div class="form-group">
                        <label for="lastName">Last Name:</label>
                        <input type="text" id="lastName" name="lastName" class="input-control" value="${contact.lastName}">
                        <c:if test="${not empty lastNameError}">
                            <span class="error-msg">${lastNameError}</span>
                        </c:if>
                    </div>

                    <div class="form-group">
                        <label for="groupId">Group:</label>
                        <select id="groupId" name="groupId" class="input-control">
                            <c:forEach var="g" items="${groupsList}">
                                <option value="${g.id}" <c:if test="${g.id == contact.groupId}">selected</c:if>>${g.name} - ${g.description}</option>
                            </c:forEach>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="phoneNumber">Phone Number:</label>
                        <input type="text" id="phoneNumber" name="phoneNumber" class="input-control" value="${contact.phoneNumber}">
                        <c:if test="${not empty phoneNumberError}">
                            <span class="error-msg">${phoneNumberError}</span>
                        </c:if>
                    </div>

                    <div class="btn-group">
                        <button type="submit" class="btn btn-primary" id="btnEditSave">Edit</button>
                        <a href="ContactServlet?action=list" class="btn btn-secondary" id="btnReturn">Return To Contact List</a>
                    </div>
                </form>
            </c:when>
            <c:otherwise>
                <div style="text-align: center; margin-bottom: 2rem;">
                    <p class="error-msg" style="font-size: 1.2rem;">Contact not found or invalid ID.</p>
                </div>
                <div class="btn-group" style="justify-content: center;">
                    <a href="ContactServlet?action=list" class="btn btn-secondary">Return To Contact List</a>
                </div>
            </c:otherwise>
        </c:choose>
    </div>
</body>
</html>
