package Day4;

public class MainLibrary {

    public static void main(String[] args) {
        Library thuVien = new Library();
        System.out.println(">>> 1. KHỞI TẠO THƯ VIỆN <<<");

        Book sachJava = new Book("J001", "Học Java Căn Bản", "Java Master", false);
        Book sachOOP = new Book("O002", "Nguyên Lý OOP", "Design Genius", false);

        User anhHocVien = new User("SV01", "Anh Học Viên");
        User chiMentor = new User("MT02", "Chị Mentor");

        thuVien.addBook(sachJava);
        thuVien.addBook(sachOOP);
        thuVien.addUser(anhHocVien);
        thuVien.addUser(chiMentor);

        System.out.println("\n>>> 2. TRẠNG THÁI BAN ĐẦU <<<");
        thuVien.displayAllBooks();
        thuVien.displayAllUsers();

        System.out.println("\n>>> 3. MƯỢN SÁCH <<<");
        thuVien.borrowBook("SV01", "J001");
        thuVien.borrowBook("MT02", "O002");

        System.out.println("\n>>> 4. TRẠNG THÁI SAU KHI MƯỢN <<<");
        thuVien.displayAllBooks();
        thuVien.displayAllUsers();



        System.out.println("\n>>> 5. TRẢ SÁCH <<<");

        thuVien.returnBook("SV01", "J001");

        System.out.println("\n>>> 6. TRẠNG THÁI CUỐI CÙNG <<<");
        thuVien.displayAllBooks();
        thuVien.displayAllUsers();
    }
}