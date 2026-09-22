package controllers;

import dao.MobileDAO;
import models.Mobile;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/home")
public class HomeServlet extends HttpServlet {
    private MobileDAO mobileDAO;

    public void init() { 
        mobileDAO = new MobileDAO(); 
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Mobile> listMobile = mobileDAO.selectAllMobiles();
        request.setAttribute("listMobile", listMobile);
        request.getRequestDispatcher("home.jsp").forward(request, response);
    }
}
