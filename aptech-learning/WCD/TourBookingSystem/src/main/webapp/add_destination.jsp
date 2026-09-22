<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <title>Add New Destination</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <header>
        <h1>Tour Booking System (Admin)</h1>
        <nav>
            <a href="viewDestinations">Manage Destinations</a>
            <a href="login.jsp">Back to Login</a>
        </nav>
    </header>

    <div class="container" style="max-width: 500px;">
        <h2>Add New Destination</h2>
        
        <% if (request.getAttribute("error") != null) { %>
            <div class="error"><%= request.getAttribute("error") %></div>
        <% } %>
        <% if (request.getAttribute("success") != null) { %>
            <div class="success"><%= request.getAttribute("success") %></div>
        <% } %>
        
        <form action="addDestination" method="POST">
            <label for="name">Destination Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="country">Country:</label>
            <input type="text" id="country" name="country" required>
            
            <label for="description">Description:</label>
            <textarea id="description" name="description" rows="4"></textarea>
            
            <label for="price">Price ($):</label>
            <input type="number" id="price" name="price" required min="100" step="0.01">
            
            <label for="availableSpots">Available Spots:</label>
            <input type="number" id="availableSpots" name="availableSpots" required min="1">
            
            <button type="submit">Add Destination</button>
        </form>
    </div>
</body>
</html>
