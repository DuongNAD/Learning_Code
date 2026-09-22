<%@ page import="com.tourbooking.entity.User" %>
<%@ page import="com.tourbooking.entity.Destination" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    User user = (User) session.getAttribute("user");
    if (user == null) {
        response.sendRedirect("login.jsp");
        return;
    }
    List<Destination> destinations = (List<Destination>) request.getAttribute("destinations");
%>
<!DOCTYPE html>
<html>
<head>
    <title>Book a Tour Package</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <script>
        function updatePrice() {
            var select = document.getElementById("destinationSelect");
            var priceInput = document.getElementById("price");
            var selectedOption = select.options[select.selectedIndex];
            if(selectedOption.value !== "") {
                priceInput.value = selectedOption.getAttribute("data-price");
            } else {
                priceInput.value = "";
            }
        }
    </script>
</head>
<body>
    <header>
        <h1>Tour Booking System</h1>
        <nav>
            <a href="viewBookings">My Dashboard</a>
            <a href="logout">Logout (<%= user.getUsername() %>)</a>
        </nav>
    </header>

    <div class="container" style="max-width: 500px;">
        <h2>Book a Tour Package</h2>
        
        <% if (request.getAttribute("error") != null) { %>
            <div class="error"><%= request.getAttribute("error") %></div>
        <% } %>
        
        <form action="bookTour" method="POST">
            <label for="destinationSelect">Destination:</label>
            <select id="destinationSelect" name="destination" required onchange="updatePrice()">
                <option value="">-- Select a Destination --</option>
                <% if (destinations != null) {
                    for (Destination d : destinations) { %>
                        <option value="<%= d.getName() %>" data-price="<%= d.getPrice() %>">
                            <%= d.getName() %> (<%= d.getCountry() %>) - $<%= d.getPrice() %>
                        </option>
                <%  }
                } %>
            </select>
            
            <label for="departureDate">Departure Date:</label>
            <input type="date" id="departureDate" name="departureDate" required>
            
            <label for="price">Price ($):</label>
            <input type="number" id="price" name="price" required min="100" step="0.01" readonly>
            
            <button type="submit">Book Now</button>
        </form>
    </div>
</body>
</html>
