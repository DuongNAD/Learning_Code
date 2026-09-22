package controllers;

import entities.Book;
import entities.Borrower;
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

@WebServlet(name = "BorrowerServlet", urlPatterns = {"/borrowers", "/add-borrower"})
public class BorrowerServlet extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String path = request.getServletPath();
        EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
        try {
            if ("/borrowers".equals(path)) {
                String bookIdStr = request.getParameter("bookId");
                List<Book> books = em.createQuery("SELECT b FROM Book b", Book.class).getResultList();
                request.setAttribute("books", books);
                
                if (bookIdStr != null && !bookIdStr.isEmpty()) {
                    int bookId = Integer.parseInt(bookIdStr);
                    Book selectedBook = em.find(Book.class, bookId);
                    List<Borrower> borrowers = em.createQuery("SELECT br FROM Borrower br WHERE br.book.id = :bookId", Borrower.class)
                            .setParameter("bookId", bookId)
                            .getResultList();
                    request.setAttribute("borrowers", borrowers);
                    request.setAttribute("selectedBook", selectedBook);
                }
                request.getRequestDispatcher("/borrowers.jsp").forward(request, response);
            } else if ("/add-borrower".equals(path)) {
                List<Book> books = em.createQuery("SELECT b FROM Book b", Book.class).getResultList();
                request.setAttribute("books", books);
                request.getRequestDispatcher("/add-borrower.jsp").forward(request, response);
            }
        } finally {
            em.close();
        }
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        String path = request.getServletPath();
        if ("/add-borrower".equals(path)) {
            String name = request.getParameter("name");
            String email = request.getParameter("email");
            String bookIdStr = request.getParameter("bookId");

            if (name == null || name.trim().length() < 3 || email == null || !email.contains("@")) {
                request.setAttribute("error", "Validation failed. Name must be >= 3 chars and valid email.");
                doGet(request, response);
                return;
            }

            EntityManager em = JPAUtil.getEntityManagerFactory().createEntityManager();
            EntityTransaction tx = em.getTransaction();
            try {
                tx.begin();
                Book book = em.find(Book.class, Integer.parseInt(bookIdStr));
                if (book != null) {
                    Borrower borrower = new Borrower();
                    borrower.setName(name);
                    borrower.setEmail(email);
                    borrower.setBook(book);
                    em.persist(borrower);
                }
                tx.commit();
                response.sendRedirect(request.getContextPath() + "/borrowers?bookId=" + bookIdStr);
            } catch (Exception e) {
                if (tx.isActive()) tx.rollback();
                request.setAttribute("error", "Error saving borrower.");
                doGet(request, response);
            } finally {
                em.close();
            }
        }
    }
}
