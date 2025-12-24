package Day4;

import java.util.ArrayList;

public class Library {
    private ArrayList<Book> books;
    private ArrayList<User> users;

    public Library() {
        this.books = new ArrayList<>();
        this.users = new ArrayList<>();
    }

    public Book findBook (String bookId){
        for(Book book : this.books){
            if(book.getBookId().equals(bookId)){
                return book;
            }
        }
        return null;
    }

    public User findUser(String username){
        for(User user : this.users){
            if(user.getUserId().equals(username)){
                return user;
            }
        }
        return null;
    }

    public void addBook(Book book){
        if(findBook(book.getBookId()) != null){
            System.out.println("Sách đã tồn tại");
        }
        else{
            this.books.add(book);
            System.out.println("Thêm sách thành công: " + book.getTitle());
        }
    }

    public void removeBook(String bookId){
        Book bookToRemove =  findBook(bookId);
        if(bookToRemove != null){
            this.books.remove(bookToRemove);
            System.out.println("Đã xóa sách " + bookToRemove.getTitle());
        }
        else {
            System.out.println("Lỗi! Không tìm thấy sách với Id: "+bookId);
        }
    }

    public void displayAllBooks(){
        System.out.println("\n===== DANH SÁCH TẤT CẢ SÁCH TRONG THƯ VIỆN (" + books.size() + " cuốn) =====");
        if (books.isEmpty()) {
            System.out.println("Thư viện hiện chưa có cuốn sách nào");
            return;
        }
        for (Book book : books) {
            book.displayBookInfo();
            System.out.println("Trạng thái: " + (book.isBorrowed() ? "Đã mượn" : "Còn sẵn"));
            System.out.println("------------------------------------");
        }
    }

    public void addUser(User user){
        if(findUser(user.getUserId()) != null){
            System.out.println("Người dùng đã tồn tại");
        }
        else {
            this.users.add(user);
            System.out.println("Đã thêm người dùng mới: " + user.getName());
        }
    }

    public void removeUser(User user){
        User userToRemove = findUser(user.getUserId());
        if(userToRemove != null){
            this.users.remove(user);
            System.out.println("Đã xóa ngưười dùng: " + user.getName());
        }
        else {
            System.out.println("Lỗi! Không tìm thấy người dùng: "+user.getUserId());
        }
    }

    public void displayAllUsers(){
        System.out.println("\n===== DANH SÁCH TẤT CẢ NGƯỜI DÙNG TRONG THƯ VIỆN (" + users.size() + " cuốn) =====");
        if(users.isEmpty()) {
            System.out.println("Hiện chưa có người dùng nào");
            return;
        }
        for(User user : this.users) {
            user.displayUserInfo();
        }
        System.out.println("==============================================");
    }

    public void returnBook(String userId, String bookId) {
        User user = findUser(userId);
        Book book = findBook(bookId);

        if (user == null) {
            System.out.println("Lỗi: Không tìm thấy người dùng với ID " + userId);
            return;
        }
        if (book == null) {
            System.out.println("Lỗi: Không tìm thấy sách với ID: " + bookId);
            return;
        }

        if (!user.getBorrowedBooks().contains(book)) {
            System.out.println("Lỗi: Người dùng " + user.getName() + " chưa mượn cuốn sách này.");
            return;
        }

        book.returnBook();
        user.returnBook(book);

        System.out.println("Giao dịch TRẢ SÁCH thành công: " + user.getName() + " đã trả '" + book.getTitle() + "'.");
    }

    public void borrowBook(String userId, String bookId) {
        User user = findUser(userId);
        Book book = findBook(bookId);

        if (user == null) {
            System.out.println("Lỗi MƯỢN SÁCH: Không tìm thấy người dùng với ID " + userId);
            return;
        }
        if (book == null) {
            System.out.println("Lỗi MƯỢN SÁCH: Không tìm thấy sách với ID: " + bookId);
            return;
        }
        if (book.isBorrowed()) {
            System.out.println("Lỗi MƯỢN SÁCH: Cuốn sách '" + book.getTitle() + "' đã có người mượn.");
            return;
        }

        book.borrowBook();
        user.borrowBook(book);

        System.out.println("Giao dịch MƯỢN SÁCH thành công!");
    }
}
