<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>User Login</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <div class="container" style="max-width: 400px;">
        <h2>User Login</h2>
        
        <% if (request.getAttribute("error") != null) { %>
            <div class="error"><%= request.getAttribute("error") %></div>
        <% } %>
        <% if ("true".equals(request.getParameter("registered"))) { %>
            <div class="success">Registration successful! Please login.</div>
        <% } %>
        
        <form action="login" method="POST">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            
            <button type="submit">Login</button>
        </form>
        <p style="text-align: center; margin-top: 15px;">
            Don't have an account? <a href="register.jsp">Register here</a>
        </p>
        <p style="text-align: center; margin-top: 15px; font-size: 0.9em;">
            <a href="viewDestinations">Admin: Manage Destinations</a>
        </p>
    </div>
</body>
</html>
