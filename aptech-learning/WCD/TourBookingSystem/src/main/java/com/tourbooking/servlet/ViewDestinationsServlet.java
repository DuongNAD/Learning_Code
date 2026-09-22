package com.tourbooking.servlet;

import com.tourbooking.entity.Destination;
import com.tourbooking.util.JPAUtil;

import javax.persistence.EntityManager;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/viewDestinations")
public class ViewDestinationsServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        
        try {
            List<Destination> destinations = em.createQuery("SELECT d FROM Destination d", Destination.class).getResultList();
            request.setAttribute("destinations", destinations);
            request.getRequestDispatcher("view_destinations.jsp").forward(request, response);
        } finally {
            em.close();
        }
    }
}
