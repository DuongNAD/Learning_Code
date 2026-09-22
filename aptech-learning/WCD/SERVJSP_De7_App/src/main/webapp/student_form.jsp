<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Student Registration</title>
    <style>
        .error { color: red; margin-left: 10px; }
        .form-group { margin-bottom: 15px; }
        label { display: inline-block; width: 100px; }
    </style>
</head>
<body>
    <h2>Student Registration Form</h2>
    <% 
        String errorMsg = (String) request.getAttribute("errorMsg");
        if(errorMsg != null) {
            out.println("<p style='color:red;'>" + errorMsg + "</p>");
        }
        
        String idError = (String) request.getAttribute("idError");
        String nameError = (String) request.getAttribute("nameError");
        String ageError = (String) request.getAttribute("ageError");
    %>
    <form action="StudentServlet" method="POST">
        <div class="form-group">
            <label>Student ID:</label>
            <input type="text" name="studentId" value="${param.studentId}">
            <% if(idError != null) { %><span class="error"><%= idError %></span><% } %>
        </div>
        <div class="form-group">
            <label>Student Name:</label>
            <input type="text" name="studentName" value="${param.studentName}">
            <% if(nameError != null) { %><span class="error"><%= nameError %></span><% } %>
        </div>
        <div class="form-group">
            <label>Age:</label>
            <input type="text" name="age" value="${param.age}">
            <% if(ageError != null) { %><span class="error"><%= ageError %></span><% } %>
        </div>
        <div class="form-group">
            <button type="submit">Submit</button>
        </div>
    </form>
</body>
</html>
