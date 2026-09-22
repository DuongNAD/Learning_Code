package com.tourbooking.servlet;

import com.tourbooking.entity.Booking;
import com.tourbooking.entity.Destination;
import com.tourbooking.entity.User;
import com.tourbooking.util.JPAUtil;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

@WebServlet("/bookTour")
public class BookTourServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        try {
            List<Destination> destinations = em.createQuery("SELECT d FROM Destination d WHERE d.availableSpots > 0", Destination.class).getResultList();
            request.setAttribute("destinations", destinations);
            request.getRequestDispatcher("book_tour.jsp").forward(request, response);
        } finally {
            em.close();
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User sessionUser = (User) session.getAttribute("user");
        String destinationName = request.getParameter("destination");
        String departureDateStr = request.getParameter("departureDate");
        String priceStr = request.getParameter("price");

        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        EntityTransaction tx = em.getTransaction();

        try {
            Date departureDate = new SimpleDateFormat("yyyy-MM-dd").parse(departureDateStr);
            Double price = Double.parseDouble(priceStr);

            if (price < 100) {
                request.setAttribute("error", "Price must be at least 100.");
                doGet(request, response);
                return;
            }
            if (departureDate.before(new Date())) {
                request.setAttribute("error", "Departure date must be in the future.");
                doGet(request, response);
                return;
            }

            tx.begin();
            // Re-fetch user in current entity manager context
            User user = em.find(User.class, sessionUser.getId());
            
            Booking booking = new Booking();
            booking.setUser(user);
            booking.setDestination(destinationName);
            booking.setDepartureDate(departureDate);
            booking.setPrice(price);
            booking.setStatus("Pending");
            
            em.persist(booking);
            tx.commit();

            response.sendRedirect("viewBookings?success=Booking created successfully");
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            request.setAttribute("error", "Error creating booking.");
            doGet(request, response);
        } finally {
            em.close();
        }
    }
}
