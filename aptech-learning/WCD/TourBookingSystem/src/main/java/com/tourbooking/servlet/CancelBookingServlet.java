package com.tourbooking.servlet;

import com.tourbooking.entity.Booking;
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

@WebServlet("/cancelBooking")
public class CancelBookingServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User sessionUser = (User) session.getAttribute("user");
        String bookingIdStr = request.getParameter("bookingId");

        if (bookingIdStr != null && !bookingIdStr.isEmpty()) {
            EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Booking booking = em.find(Booking.class, Integer.parseInt(bookingIdStr));
                
                // Ensure the booking belongs to the current user and is Pending
                if (booking != null && booking.getUser().getId().equals(sessionUser.getId()) && "Pending".equals(booking.getStatus())) {
                    booking.setStatus("Cancelled");
                    em.merge(booking);
                    tx.commit();
                    response.sendRedirect("viewBookings?message=Booking cancelled successfully");
                } else {
                    tx.rollback();
                    response.sendRedirect("viewBookings?error=Cannot cancel booking");
                }
            } catch (Exception e) {
                if (tx.isActive()) tx.rollback();
                e.printStackTrace();
                response.sendRedirect("viewBookings?error=An error occurred");
            } finally {
                em.close();
            }
        } else {
            response.sendRedirect("viewBookings");
        }
    }
}
