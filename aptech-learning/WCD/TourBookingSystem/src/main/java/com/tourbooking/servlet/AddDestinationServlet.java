package com.tourbooking.servlet;

import com.tourbooking.entity.Destination;
import com.tourbooking.util.JPAUtil;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/addDestination")
public class AddDestinationServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("add_destination.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String country = request.getParameter("country");
        String description = request.getParameter("description");
        String priceStr = request.getParameter("price");
        String availableSpotsStr = request.getParameter("availableSpots");

        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        EntityTransaction tx = em.getTransaction();

        try {
            Double price = Double.parseDouble(priceStr);
            Integer spots = Integer.parseInt(availableSpotsStr);

            if (price < 100) {
                request.setAttribute("error", "Price must be at least 100.");
                request.getRequestDispatcher("add_destination.jsp").forward(request, response);
                return;
            }

            tx.begin();
            Destination destination = new Destination();
            destination.setName(name);
            destination.setCountry(country);
            destination.setDescription(description);
            destination.setPrice(price);
            destination.setAvailableSpots(spots);
            
            em.persist(destination);
            tx.commit();

            request.setAttribute("success", "Destination added successfully!");
            request.getRequestDispatcher("add_destination.jsp").forward(request, response);
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            request.setAttribute("error", "Error adding destination.");
            request.getRequestDispatcher("add_destination.jsp").forward(request, response);
        } finally {
            em.close();
        }
    }
}
