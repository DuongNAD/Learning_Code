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

@WebServlet("/deleteDestination")
public class DeleteDestinationServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String idStr = request.getParameter("id");

        if (idStr != null && !idStr.isEmpty()) {
            EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Destination dest = em.find(Destination.class, Integer.parseInt(idStr));
                if (dest != null) {
                    em.remove(dest);
                    tx.commit();
                    response.sendRedirect("viewDestinations?message=Destination deleted successfully");
                } else {
                    tx.rollback();
                    response.sendRedirect("viewDestinations?error=Destination not found");
                }
            } catch (Exception e) {
                if (tx.isActive()) tx.rollback();
                e.printStackTrace();
                response.sendRedirect("viewDestinations?error=Error deleting destination");
            } finally {
                em.close();
            }
        } else {
            response.sendRedirect("viewDestinations");
        }
    }
}
