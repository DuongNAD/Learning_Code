package controllers;

import dao.MobileDAO;
import models.Mobile;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/insert")
public class InsertServlet extends HttpServlet {
    private MobileDAO mobileDAO;

    public void init() { 
        mobileDAO = new MobileDAO(); 
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.getRequestDispatcher("insertNewMobile.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        
        String name = request.getParameter("name");
        String priceStr = request.getParameter("price");
        String warranty = request.getParameter("warranty");
        String accessories = request.getParameter("accessories");
        boolean inOutStock = "true".equals(request.getParameter("inOutStock"));
        String image = request.getParameter("image");

        double price = 0;
        boolean hasError = false;

        // Validation: required, number, positive number
        try {
            if (priceStr == null || priceStr.trim().isEmpty()) {
                hasError = true;
            } else {
                price = Double.parseDouble(priceStr);
                if (price <= 0) {
                    hasError = true;
                }
            }
        } catch (NumberFormatException e) {
            hasError = true;
        }

        if (hasError) {
            // Forward back to form, preserving data
            request.setAttribute("error", "true");
            request.getRequestDispatcher("insertNewMobile.jsp").forward(request, response);
        } else {
            // Insert and redirect to home
            Mobile newMobile = new Mobile(name, price, warranty, accessories, inOutStock, image);
            mobileDAO.insertMobile(newMobile);
            response.sendRedirect("home");
        }
    }
}
