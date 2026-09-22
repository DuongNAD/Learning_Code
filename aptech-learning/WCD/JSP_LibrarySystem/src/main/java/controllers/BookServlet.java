package controllers;

import entities.Book;
import utils.JPAUtil;

import javax.persistence.EntityManager;
import javax.persistence.EntityTransaction;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet(name = "BookServlet", urlPatterns = {"/books", "/add-book", "/delete-book"})
public class BookServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String path = request.getServletPath();
        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();

        try {
            if ("/books".equals(path)) {
                List<Book> books = em.createQuery("SELECT b FROM Book b", Book.class).getResultList();
                request.setAttribute("books", books);
                request.getRequestDispatcher("/books.jsp").forward(request, response);
            } else if ("/add-book".equals(path)) {
                request.getRequestDispatcher("/add-book.jsp").forward(request, response);
            } else if ("/delete-book".equals(path)) {
                String idStr = request.getParameter("id");
                if (idStr != null) {
                    EntityTransaction tx = em.getTransaction();
                    try {
                        tx.begin();
                        Book b = em.find(Book.class, Integer.parseInt(idStr));
                        if (b != null) {
                            em.remove(b);
                        }
                        tx.commit();
                    } catch (Exception e) {
                        if (tx.isActive()) tx.rollback();
                    }
                }
                response.sendRedirect(request.getContextPath() + "/books");
            }
        } finally {
            em.close();
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        String path = request.getServletPath();
        if ("/add-book".equals(path)) {
            String title = request.getParameter("title");
            String author = request.getParameter("author");
            String copiesStr = request.getParameter("totalCopies");

            if (title == null || title.trim().length() < 3 || copiesStr == null || Integer.parseInt(copiesStr) < 1) {
                request.setAttribute("error", "Validation failed. Title must be >= 3 chars, Copies >= 1.");
                request.getRequestDispatcher("/add-book.jsp").forward(request, response);
                return;
            }

            Book book = new Book();
            book.setTitle(title);
            book.setAuthor(author);
            book.setTotalCopies(Integer.parseInt(copiesStr));

            EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                em.persist(book);
                tx.commit();
                response.sendRedirect(request.getContextPath() + "/books");
            } catch (Exception e) {
                if (tx.isActive()) tx.rollback();
                request.setAttribute("error", "Error saving book.");
                request.getRequestDispatcher("/add-book.jsp").forward(request, response);
            } finally {
                em.close();
            }
        }
    }
}
