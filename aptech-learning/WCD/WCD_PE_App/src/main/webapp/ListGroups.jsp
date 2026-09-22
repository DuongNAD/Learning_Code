<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="com.exercise.dao.GroupDAO" %>
<%@ page import="com.exercise.entity.Group" %>
<%@ page import="java.util.List" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%
    if (request.getAttribute("groupList") == null) {
        GroupDAO groupDAO = new GroupDAO();
        List<Group> groupList = groupDAO.getAllGroups();
        request.setAttribute("groupList", groupList);
    }
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List Of Group</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <div class="container">
        <h1>List Of Group</h1>
        <p class="subtitle">All contact categorization groups in the database</p>

        <div class="table-responsive">
            <table id="groupTable">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Group Name</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach var="g" items="${groupList}">
                        <tr>
                            <td>${g.id}</td>
                            <td>${g.name}</td>
                            <td>${g.description}</td>
                        </tr>
                    </c:forEach>
                    <c:if test="${empty groupList}">
                        <tr>
                            <td colspan="3" style="text-align: center;">No groups found.</td>
                        </tr>
                    </c:if>
                </tbody>
            </table>
        </div>

        <div class="btn-group">
            <a href="AddGroup.jsp" class="btn btn-primary" id="btnAddGroup">Add Group</a>
            <a href="ContactServlet?action=list" class="btn btn-secondary" id="btnListContact">List Contact</a>
        </div>
    </div>
</body>
</html>
