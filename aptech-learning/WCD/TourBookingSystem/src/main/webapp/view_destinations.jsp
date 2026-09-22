<%@ page import="java.util.List" %>
<%@ page import="com.tourbooking.entity.Destination" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    List<Destination> destinations = (List<Destination>) request.getAttribute("destinations");
%>
<!DOCTYPE html>
<html>
<head>
    <title>Destination Management</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <header>
        <h1>Tour Booking System (Admin)</h1>
        <nav>
            <a href="addDestination">Add Destination</a>
            <a href="login.jsp">Back to Login</a>
        </nav>
    </header>

    <div class="container">
        <h2>Destination Management</h2>
        
        <% if (request.getParameter("message") != null) { %>
            <div class="success"><%= request.getParameter("message") %></div>
        <% } %>
        <% if (request.getParameter("error") != null) { %>
            <div class="error"><%= request.getParameter("error") %></div>
        <% } %>

        <% if (destinations != null && !destinations.isEmpty()) { %>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Country</th>
                        <th>Price</th>
                        <th>Spots</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <% for (Destination d : destinations) { %>
                        <tr>
                            <td><%= d.getId() %></td>
                            <td><%= d.getName() %></td>
                            <td><%= d.getCountry() %></td>
                            <td>$<%= d.getPrice() %></td>
                            <td><%= d.getAvailableSpots() %></td>
                            <td>
                                <form action="deleteDestination" method="POST" style="display:inline;">
                                    <input type="hidden" name="id" value="<%= d.getId() %>">
                                    <button type="submit" class="action-btn" onclick="return confirm('Are you sure you want to delete this destination?');">Delete</button>
                                </form>
                            </td>
                        </tr>
                    <% } %>
                </tbody>
            </table>
        <% } else { %>
            <p>No destinations available. <a href="addDestination">Add one now.</a></p>
        <% } %>
    </div>
</body>
</html>
