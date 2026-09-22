<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.exercise.dao.ContactDAO" %>
<%@ page import="com.exercise.entity.Contact" %>
<%@ page import="java.util.List" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn" %>
<%
    if (request.getAttribute("contactList") == null) {
        ContactDAO contactDAO = new ContactDAO();
        List<Contact> contactList = contactDAO.getAllContacts();
        request.setAttribute("contactList", contactList);
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List Of Contacts</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>List Of Contacts</h1>
        
        <div class="counter-box" id="contactCounter">
            There are ${fn:length(contactList)} contacts in the List
        </div>

        <div class="table-responsive">
            <table id="contactTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Group</th>
                        <th>Phone Number</th>
                        <th>Operations</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach var="c" items="${contactList}">
                        <tr>
                            <td>${c.id}</td>
                            <td>${c.firstName}</td>
                            <td>${c.lastName}</td>
                            <td>${c.groupName}</td>
                            <td>${c.phoneNumber}</td>
                            <td>
                                <a href="ContactServlet?action=edit&id=${c.id}" class="link-action" id="edit-${c.id}">Edit</a>
                                <a href="ContactServlet?action=delete&id=${c.id}" class="link-action link-danger" id="remove-${c.id}"
                                   onclick="return confirm('Are you sure you want to remove this contact?');">Remove</a>
                            </td>
                        </tr>
                    </c:forEach>
                    <c:if test="${empty contactList}">
                        <tr>
                            <td colspan="6" style="text-align: center;">No contacts found.</td>
                        </tr>
                    </c:if>
                </tbody>
            </table>
        </div>

        <div class="btn-group">
            <a href="AddContact.jsp" class="btn btn-primary" id="btnAddContact">Add Contact</a>
            <a href="ContactServlet?action=listGroups" class="btn btn-secondary" id="btnListGroup">List Group</a>
        </div>
    </div>
</body>
</html>
