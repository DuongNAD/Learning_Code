package com.exercise.controller;

import com.exercise.dao.EmployeeDAO;
import com.exercise.entity.Employee;

import java.io.IOException;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/EmployeeServlet")
public class EmployeeServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private EmployeeDAO employeeDAO = new EmployeeDAO();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if (action == null) {
            action = "list";
        }

        switch (action) {
            case "delete":
                deleteEmployee(request, response);
                break;
            case "list":
            default:
                listEmployees(request, response);
                break;
        }
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("add".equals(action)) {
            addEmployee(request, response);
        } else {
            doGet(request, response);
        }
    }

    private void listEmployees(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Employee> list = employeeDAO.getAllEmployees();
        request.setAttribute("employeeList", list);
        request.getRequestDispatcher("employee_list.jsp").forward(request, response);
    }

    private void deleteEmployee(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String employeeNo = request.getParameter("employeeNo");
        employeeDAO.deleteEmployee(employeeNo);
        response.sendRedirect("EmployeeServlet?action=list");
    }

    private void addEmployee(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String employeeNo = request.getParameter("employeeNo");
        String employeeName = request.getParameter("employeeName");
        String placeOfWork = request.getParameter("placeOfWork");
        String phoneNo = request.getParameter("phoneNo");

        boolean hasError = false;

        if (employeeNo == null || employeeNo.trim().isEmpty()) {
            request.setAttribute("noError", "Employee No is required");
            hasError = true;
        }
        if (employeeName == null || employeeName.trim().isEmpty()) {
            request.setAttribute("nameError", "Employee Name is required");
            hasError = true;
        }
        if (placeOfWork == null || placeOfWork.trim().isEmpty()) {
            request.setAttribute("placeError", "Place of Work is required");
            hasError = true;
        }
        if (phoneNo == null || phoneNo.trim().isEmpty()) {
            request.setAttribute("phoneError", "Phone No is required");
            hasError = true;
        }

        if (hasError) {
            request.getRequestDispatcher("add_employee.jsp").forward(request, response);
            return;
        }

        if (employeeDAO.isEmployeeExists(employeeNo)) {
            request.setAttribute("globalError", "Employee No already exists!");
            request.getRequestDispatcher("add_employee.jsp").forward(request, response);
            return;
        }

        Employee emp = new Employee(employeeNo, employeeName, placeOfWork, phoneNo);
        employeeDAO.addEmployee(emp);
        response.sendRedirect("EmployeeServlet?action=list");
    }
}
