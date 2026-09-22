package com.tourbooking.servlet;

import com.tourbooking.entity.Booking;
import com.tourbooking.entity.User;
import com.tourbooking.util.JPAUtil;

import javax.persistence.EntityManager;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.List;

@WebServlet("/viewBookings")
public class ViewBookingsServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session = request.getSession(false);
        if (session == null || session.getAttribute("user") == null) {
            response.sendRedirect("login.jsp");
            return;
        }

        User sessionUser = (User) session.getAttribute("user");
        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();

        try {
            List<Booking> bookings = em.createQuery("SELECT b FROM Booking b WHERE b.user.id = :userId", Booking.class)
                    .setParameter("userId", sessionUser.getId())
                    .getResultList();

            request.setAttribute("bookings", bookings);
            request.getRequestDispatcher("dashboard.jsp").forward(request, response);
        } finally {
            em.close();
        }
    }
}
