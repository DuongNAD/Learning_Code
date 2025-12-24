package Day4;

public class Book {
    private String bookId;
    private String title;
    private String author;
    private boolean isBorrowed;

    public Book(String bookId, String title, String author, boolean isBorrowed) {
        this.bookId = bookId;
        this.title = title;
        this.author = author;
        this.isBorrowed = isBorrowed;
    }

    public String getBookId() {
        return bookId;
    }
    public void setBookId(String bookId) {
        this.bookId = bookId;
    }
    public String getTitle() {
        return title;
    }
    public void setTitle(String title) {
        this.title = title;
    }
    public String getAuthor() {
        return author;
    }
    public void setAuthor(String author) {
        this.author = author;
    }
    public boolean isBorrowed() {
        return isBorrowed;
    }
    public void setBorrowed(boolean borrowed) {
        isBorrowed = borrowed;
    }

    public void borrowBook() {
        isBorrowed = true;
    }
    public void returnBook() {
        isBorrowed = false;
    }

    public void displayBookInfo() {
        System.out.println("Book ID: " + bookId);
        System.out.println("Title: " + title);
        System.out.println("Author: " + author);
        System.out.println("ISBN: " + isBorrowed);
    }

}
