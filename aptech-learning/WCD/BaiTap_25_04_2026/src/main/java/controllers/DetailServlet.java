package controllers;

import dao.MobileDAO;
import models.Mobile;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/detail")
public class DetailServlet extends HttpServlet {
    private MobileDAO mobileDAO;

    public void init() { 
        mobileDAO = new MobileDAO(); 
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String idParam = request.getParameter("id");
        if (idParam != null && !idParam.isEmpty()) {
            int id = Integer.parseInt(idParam);
            Mobile mobile = mobileDAO.selectMobile(id);
            request.setAttribute("mobile", mobile);
        }
        request.getRequestDispatcher("mobileDetail.jsp").forward(request, response);
    }
}
