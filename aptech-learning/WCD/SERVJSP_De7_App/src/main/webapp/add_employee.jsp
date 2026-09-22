<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Add New Employee</title>
    <style>
        .error { color: red; margin-left: 10px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 150px; }
    </style>
</head>
<body>
    <h2>Add New Employee</h2>
    <% 
        String globalError = (String) request.getAttribute("globalError");
        if(globalError != null) {
            out.println("<p style='color:red; font-weight:bold;'>" + globalError + "</p>");
        }
    %>
    <form action="EmployeeServlet" method="POST">
        <input type="hidden" name="action" value="add">
        
        <div class="form-group">
            <label>Employee No:</label>
            <input type="text" name="employeeNo" value="${param.employeeNo}">
            <% String noError = (String) request.getAttribute("noError");
               if(noError != null) { %><span class="error"><%= noError %></span><% } %>
        </div>
        
        <div class="form-group">
            <label>Employee Name:</label>
            <input type="text" name="employeeName" value="${param.employeeName}">
            <% String nameError = (String) request.getAttribute("nameError");
               if(nameError != null) { %><span class="error"><%= nameError %></span><% } %>
        </div>
        
        <div class="form-group">
            <label>Place of Work:</label>
            <input type="text" name="placeOfWork" value="${param.placeOfWork}">
            <% String placeError = (String) request.getAttribute("placeError");
               if(placeError != null) { %><span class="error"><%= placeError %></span><% } %>
        </div>
        
        <div class="form-group">
            <label>Phone No:</label>
            <input type="text" name="phoneNo" value="${param.phoneNo}">
            <% String phoneError = (String) request.getAttribute("phoneError");
               if(phoneError != null) { %><span class="error"><%= phoneError %></span><% } %>
        </div>
        
        <div class="form-group">
            <button type="submit">Save</button>
            <button type="button" onclick="window.location.href='EmployeeServlet?action=list'">Cancel</button>
        </div>
    </form>
</body>
</html>
