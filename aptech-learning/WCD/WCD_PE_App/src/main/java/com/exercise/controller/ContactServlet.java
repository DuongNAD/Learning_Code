package com.exercise.controller;

import com.exercise.dao.ContactDAO;
import com.exercise.dao.GroupDAO;
import com.exercise.entity.Contact;
import com.exercise.entity.Group;

import java.io.IOException;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/ContactServlet")
public class ContactServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private final ContactDAO contactDAO = new ContactDAO();
    private final GroupDAO groupDAO = new GroupDAO();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if (action == null) {
            action = "list";
        }

        switch (action) {
            case "delete":
                deleteContact(request, response);
                break;
            case "edit":
                showEditForm(request, response);
                break;
            case "listGroups":
                listGroups(request, response);
                break;
            case "list":
            default:
                listContacts(request, response);
                break;
        }
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        if ("add".equals(action)) {
            addContact(request, response);
        } else if ("edit".equals(action)) {
            editContact(request, response);
        } else if ("addGroup".equals(action)) {
            addGroup(request, response);
        } else {
            doGet(request, response);
        }
    }

    private void listContacts(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Contact> list = contactDAO.getAllContacts();
        request.setAttribute("contactList", list);
        request.getRequestDispatcher("ListContacts.jsp").forward(request, response);
    }

    private void listGroups(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Group> list = groupDAO.getAllGroups();
        request.setAttribute("groupList", list);
        request.getRequestDispatcher("ListGroups.jsp").forward(request, response);
    }

    private void showEditForm(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String idStr = request.getParameter("id");
        if (idStr != null) {
            try {
                int id = Integer.parseInt(idStr);
                Contact contact = contactDAO.getContactById(id);
                if (contact != null) {
                    request.setAttribute("contact", contact);
                }
            } catch (NumberFormatException e) {
                e.printStackTrace();
            }
        }
        request.getRequestDispatcher("EditContact.jsp").forward(request, response);
    }

    private void deleteContact(HttpServletRequest request, HttpServletResponse response) throws IOException {
        String idStr = request.getParameter("id");
        if (idStr != null) {
            try {
                int id = Integer.parseInt(idStr);
                contactDAO.deleteContact(id);
            } catch (NumberFormatException e) {
                e.printStackTrace();
            }
        }
        response.sendRedirect("ContactServlet?action=list");
    }

    private void addContact(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String groupIdStr = request.getParameter("groupId");
        String phoneNumber = request.getParameter("phoneNumber");

        boolean hasError = false;

        if (firstName == null || firstName.trim().isEmpty()) {
            request.setAttribute("firstNameError", "First Name is required");
            hasError = true;
        }
        if (lastName == null || lastName.trim().isEmpty()) {
            request.setAttribute("lastNameError", "Last Name is required");
            hasError = true;
        }
        if (phoneNumber == null || phoneNumber.trim().isEmpty()) {
            request.setAttribute("phoneNumberError", "Phone Number is required");
            hasError = true;
        } else if (!phoneNumber.trim().matches("\\d+")) {
            request.setAttribute("phoneNumberError", "Phone Number must be numerical");
            hasError = true;
        }

        int groupId = 0;
        if (groupIdStr != null && !groupIdStr.trim().isEmpty()) {
            try {
                groupId = Integer.parseInt(groupIdStr);
            } catch (NumberFormatException e) {
                // ignore
            }
        }

        if (hasError) {
            // Keep parameters to populate back
            request.setAttribute("firstNameVal", firstName);
            request.setAttribute("lastNameVal", lastName);
            request.setAttribute("groupIdVal", groupId);
            request.setAttribute("phoneNumberVal", phoneNumber);
            request.getRequestDispatcher("AddContact.jsp").forward(request, response);
            return;
        }

        Contact contact = new Contact(firstName, lastName, groupId, phoneNumber);
        contactDAO.addContact(contact);
        response.sendRedirect("ContactServlet?action=list");
    }

    private void editContact(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String idStr = request.getParameter("id");
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String groupIdStr = request.getParameter("groupId");
        String phoneNumber = request.getParameter("phoneNumber");

        int id = 0;
        try {
            id = Integer.parseInt(idStr);
        } catch (NumberFormatException e) {
            response.sendRedirect("ContactServlet?action=list");
            return;
        }

        boolean hasError = false;

        if (firstName == null || firstName.trim().isEmpty()) {
            request.setAttribute("firstNameError", "First Name is required");
            hasError = true;
        }
        if (lastName == null || lastName.trim().isEmpty()) {
            request.setAttribute("lastNameError", "Last Name is required");
            hasError = true;
        }
        if (phoneNumber == null || phoneNumber.trim().isEmpty()) {
            request.setAttribute("phoneNumberError", "Phone Number is required");
            hasError = true;
        } else if (!phoneNumber.trim().matches("\\d+")) {
            request.setAttribute("phoneNumberError", "Phone Number must be numerical");
            hasError = true;
        }

        int groupId = 0;
        if (groupIdStr != null && !groupIdStr.trim().isEmpty()) {
            try {
                groupId = Integer.parseInt(groupIdStr);
            } catch (NumberFormatException e) {
                // ignore
            }
        }

        Contact contact = new Contact(id, firstName, lastName, groupId, phoneNumber);

        if (hasError) {
            request.setAttribute("contact", contact);
            request.getRequestDispatcher("EditContact.jsp").forward(request, response);
            return;
        }

        contactDAO.updateContact(contact);
        response.sendRedirect("ContactServlet?action=list");
    }

    private void addGroup(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String name = request.getParameter("name");
        String description = request.getParameter("description");

        boolean hasError = false;
        if (name == null || name.trim().isEmpty()) {
            request.setAttribute("nameError", "Group Name is required");
            hasError = true;
        }
        if (description == null || description.trim().isEmpty()) {
            request.setAttribute("descriptionError", "Description is required");
            hasError = true;
        }

        if (hasError) {
            request.setAttribute("nameVal", name);
            request.setAttribute("descriptionVal", description);
            request.getRequestDispatcher("AddGroup.jsp").forward(request, response);
            return;
        }

        Group group = new Group(name, description);
        groupDAO.addGroup(group);
        response.sendRedirect("ContactServlet?action=listGroups");
    }
}
