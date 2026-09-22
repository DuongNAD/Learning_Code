<%@ page import="com.tourbooking.entity.User" %>
<%@ page import="java.util.List" %>
<%@ page import="com.tourbooking.entity.Booking" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    User user = (User) session.getAttribute("user");
    if (user == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    List<Booking> bookings = (List<Booking>) request.getAttribute("bookings");
%>
<!DOCTYPE html>
<html>
<head>
    <title>My Dashboard</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
    <header>
        <h1>Tour Booking System</h1>
        <nav>
            <a href="bookTour">Book a Tour</a>
            <a href="logout">Logout (<%= user.getUsername() %>)</a>
        </nav>
    </header>

    <div class="container">
        <h2>My Tour Bookings</h2>
        
        <% if (request.getParameter("message") != null) { %>
            <div class="success"><%= request.getParameter("message") %></div>
        <% } %>
        <% if (request.getParameter("error") != null) { %>
            <div class="error"><%= request.getParameter("error") %></div>
        <% } %>
        <% if (request.getParameter("success") != null) { %>
            <div class="success"><%= request.getParameter("success") %></div>
        <% } %>

        <% if (bookings != null && !bookings.isEmpty()) { %>
            <table>
                <thead>
                    <tr>
                        <th>Booking ID</th>
                        <th>Destination</th>
                        <th>Departure Date</th>
                        <th>Price</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <% for (Booking b : bookings) { %>
                        <tr>
                            <td><%= b.getBookingId() %></td>
                            <td><%= b.getDestination() %></td>
                            <td><%= b.getDepartureDate() %></td>
                            <td>$<%= b.getPrice() %></td>
                            <td><%= b.getStatus() %></td>
                            <td>
                                <% if ("Pending".equals(b.getStatus())) { %>
                                    <form action="cancelBooking" method="POST" style="display:inline;">
                                        <input type="hidden" name="bookingId" value="<%= b.getBookingId() %>">
                                        <button type="submit" class="action-btn" onclick="return confirm('Are you sure you want to cancel this booking?');">Cancel</button>
                                    </form>
                                <% } else { %>
                                    <span class="disabled-btn">-</span>
                                <% } %>
                            </td>
                        </tr>
                    <% } %>
                </tbody>
            </table>
        <% } else { %>
            <p>You have no bookings yet. <a href="bookTour">Book a tour now!</a></p>
        <% } %>
    </div>
</body>
</html>
