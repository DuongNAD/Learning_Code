<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.net.URLDecoder" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Student Information</title>
</head>
<body>
    <h2>Student Information</h2>
    <%
        Cookie[] cookies = request.getCookies();
        String studentId = "";
        String studentName = "";
        String age = "";
        
        if (cookies != null) {
            for (Cookie c : cookies) {
                if (c.getName().equals("studentId")) {
                    studentId = URLDecoder.decode(c.getValue(), "UTF-8");
                }
                if (c.getName().equals("studentName")) {
                    studentName = URLDecoder.decode(c.getValue(), "UTF-8");
                }
                if (c.getName().equals("age")) {
                    age = URLDecoder.decode(c.getValue(), "UTF-8");
                }
            }
        }
    %>
    
    <% if (!studentId.isEmpty()) { %>
        <p><strong>Student ID:</strong> <%= studentId %></p>
        <p><strong>Student Name:</strong> <%= studentName %></p>
        <p><strong>Age:</strong> <%= age %></p>
    <% } else { %>
        <p>No student information found in cookies.</p>
    <% } %>
    
    <br>
    <a href="student_form.jsp">Back to Form</a>
</body>
</html>
