<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!-- Dùng URI của Jakarta EE cho JSTL (Tomcat 10+) -->
<%@ taglib uri="jakarta.tags.core" prefix="c" %>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Danh Sách Nhân Viên</title>
</head>
<body>
    <h2>Danh Sách Nhân Viên (HR System)</h2>
    
    <!-- Table HTML thuần, border 1 để nhìn thấy khung bảng -->
    <table border="1">
        <thead>
            <tr>
                <th>Mã NV</th>
                <th>Tên</th>
                <th>Phòng Ban</th>
                <th>Lương</th>
                <th>Cấp bậc</th>
            </tr>
        </thead>
        <tbody>
            <!-- Lặp qua danh sách employeeList từ Servlet -->
            <c:forEach var="emp" items="${employeeList}">
                <tr>
                    <td>${emp.empId}</td>
                    <td>${emp.fullName}</td>
                    <td>${emp.department}</td>
                    <td>${emp.baseSalary}</td>
                    
                    <!-- Dùng c:choose xử lý logic hiển thị dựa vào yearsOfExperience -->
                    <td>
                        <c:choose>
                            <c:when test="${emp.yearsOfExperience >= 5}">
                                Senior (Thâm niên)
                            </c:when>
                            <c:otherwise>
                                Junior
                            </c:otherwise>
                        </c:choose>
                    </td>
                </tr>
            </c:forEach>
        </tbody>
    </table>
</body>
</html>
