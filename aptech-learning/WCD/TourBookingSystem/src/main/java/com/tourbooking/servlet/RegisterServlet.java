package com.tourbooking.servlet;

import com.tourbooking.entity.User;
import com.tourbooking.util.JPAUtil;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/register")
public class RegisterServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("register.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        String email = request.getParameter("email");
        String password = request.getParameter("password");

        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        EntityTransaction tx = em.getTransaction();
        
        try {
            // Basic validation
            if (username == null || email == null || password == null || password.length() < 6) {
                request.setAttribute("error", "Invalid inputs or password less than 6 characters.");
                request.getRequestDispatcher("register.jsp").forward(request, response);
                return;
            }

            // Check if username or email exists
            List<User> existingUsers = em.createQuery("SELECT u FROM User u WHERE u.username = :username OR u.email = :email", User.class)
                    .setParameter("username", username)
                    .setParameter("email", email)
                    .getResultList();

            if (!existingUsers.isEmpty()) {
                request.setAttribute("error", "Username or Email already exists.");
                request.getRequestDispatcher("register.jsp").forward(request, response);
                return;
            }

            tx.begin();
            User user = new User();
            user.setUsername(username);
            user.setEmail(email);
            user.setPassword(password); // In production, hash the password!
            em.persist(user);
            tx.commit();
            
            response.sendRedirect("login.jsp?registered=true");
        } catch (Exception e) {
            if (tx.isActive()) tx.rollback();
            e.printStackTrace();
            request.setAttribute("error", "An error occurred during registration.");
            request.getRequestDispatcher("register.jsp").forward(request, response);
        } finally {
            em.close();
        }
    }
}
