package aptech.data.manager;

import aptech.data.impl.Book;

import java.util.ArrayList;
import java.util.Scanner;

public class DocumentManager {
    private ArrayList<Book> bookList;

    private Scanner scanner = new Scanner(System.in);

    public DocumentManager(){
        bookList = new ArrayList<>();
    }

    public void addDocument(){
        System.out.println("Enter number of books you want to add: ");
        int n = Integer.parseInt(scanner.nextLine());

        for(int i = 0; i < n; i++){
            System.out.println("\n--- Input new book " + (i + 1) + " ---");
            Book newBook = new Book();
            newBook.input();
            this.bookList.add(newBook);
        }
    }

    public void displayAllDocuments(){
        if(bookList.isEmpty()){
            System.out.println("There are no books in the system");
            return;
        }
        System.out.println("=== All Documents ===");
        for(Book book : bookList){
            book.show();
            System.out.println("--------------------");
        }
    }

    public void searchByAuthorName(){
        if(bookList.isEmpty()){
            System.out.println("There are no books in the system");
            return;
        }

        System.out.print("\nEnter author name to search: ");
        String authorName = scanner.nextLine();

        System.out.println("\n--- SEARCH RESULTS ---");
        boolean found = false;

        for(Book book : bookList){
            if(authorName.equals(book.getAuthorName())){
                book.show();
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("No books found for author: " + authorName);
        }
    }
}
