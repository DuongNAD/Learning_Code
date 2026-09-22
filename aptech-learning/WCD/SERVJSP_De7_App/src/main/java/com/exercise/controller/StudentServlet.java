package com.exercise.controller;

import java.io.IOException;
import java.net.URLEncoder;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/StudentServlet")
public class StudentServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String studentId = request.getParameter("studentId");
        String studentName = request.getParameter("studentName");
        String age = request.getParameter("age");

        boolean hasError = false;

        if (studentId == null || studentId.trim().isEmpty()) {
            request.setAttribute("idError", "Student ID is required");
            hasError = true;
        }
        if (studentName == null || studentName.trim().isEmpty()) {
            request.setAttribute("nameError", "Student Name is required");
            hasError = true;
        }
        if (age == null || age.trim().isEmpty()) {
            request.setAttribute("ageError", "Age is required");
            hasError = true;
        }

        if (hasError) {
            request.getRequestDispatcher("student_form.jsp").forward(request, response);
        } else {
            // Encode value to handle spaces in cookies
            Cookie idCookie = new Cookie("studentId", URLEncoder.encode(studentId, "UTF-8"));
            Cookie nameCookie = new Cookie("studentName", URLEncoder.encode(studentName, "UTF-8"));
            Cookie ageCookie = new Cookie("age", URLEncoder.encode(age, "UTF-8"));

            // Set max age to 1 day
            idCookie.setMaxAge(24 * 60 * 60);
            nameCookie.setMaxAge(24 * 60 * 60);
            ageCookie.setMaxAge(24 * 60 * 60);

            response.addCookie(idCookie);
            response.addCookie(nameCookie);
            response.addCookie(ageCookie);

            response.sendRedirect("student_info.jsp");
        }
    }
}
