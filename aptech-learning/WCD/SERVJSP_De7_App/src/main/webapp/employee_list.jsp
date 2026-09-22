<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Employee List</title>
    <style>
        table { border-collapse: collapse; width: 80%; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Employee List</h2>
    <a href="add_employee.jsp">Add New Employee</a>
    <table>
        <tr>
            <th>Employee No</th>
            <th>Employee Name</th>
            <th>Place Of Work</th>
            <th>Phone No</th>
            <th>Action</th>
        </tr>
        <c:forEach var="emp" items="${employeeList}">
            <tr>
                <td>${emp.employeeNo}</td>
                <td>${emp.employeeName}</td>
                <td>${emp.placeOfWork}</td>
                <td>${emp.phoneNo}</td>
                <td>
                    <a href="EmployeeServlet?action=delete&employeeNo=${emp.employeeNo}" 
                       onclick="return confirm('Are you sure you want to delete this employee?');">Delete</a>
                </td>
            </tr>
        </c:forEach>
    </table>
    <br>
    <a href="index.jsp">Back to Home</a>
</body>
</html>
