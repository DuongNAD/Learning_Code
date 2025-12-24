package Day4;

import java.util.ArrayList;

public class User {
    private String userId;
    private String name;
    private ArrayList<Book> borrowedBooks;

    public User(String userId, String name) {
        this.userId = userId;
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public String getUserId() {
        return userId;
    }
    public void setUserId(String userId) {
        this.userId = userId;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public ArrayList<Book> getBorrowedBooks() {
        return borrowedBooks;
    }
    public void borrowBook(Book book) {
        this.borrowedBooks.add(book);
        System.out.println("Thành viên '" + name + "' đã mượn cuốn sách: '" + book.getTitle() + "'");
    }

    public void returnBook(Book book) {
        this.borrowedBooks.remove(book);
    }

    public void displayUserInfo() {
        System.out.println("------------------------------------");
        System.out.println("User ID: " + this.userId + " | Name: " + this.name);

        if (borrowedBooks.isEmpty()) {
            System.out.println("  -> Hiện chưa mượn cuốn sách nào.");
        } else {
            System.out.println("  -> Các sách đã mượn (" + borrowedBooks.size() + " cuốn):");
            for (Book book : this.borrowedBooks) {
                System.out.println("     - " + book.getTitle() + " (ID: " + book.getBookId() + ")");
            }
        }
    }
}
