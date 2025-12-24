package aptech.data.impl;

import aptech.data.IDocument;

import java.util.Scanner;

public class Book implements IDocument {
    private int id;
    private String bookName;
    private String authorName;
    private float price;

    public Book(){

    }

    public Book(int id, String bookName, String authorName, float price) {
        this.id = id;
        this.bookName = bookName;
        this.authorName = authorName;
        this.price = price;
    }

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getBookName() {
        return bookName;
    }
    public void setBookName(String bookName) {
        this.bookName = bookName;
    }
    public String getAuthorName() {
        return authorName;
    }
    public void setAuthorName(String authorName) {
        this.authorName = authorName;
    }
    public float getPrice() {
        return price;
    }
    public void setPrice(float price) {
        this.price = price;
    }
    @Override
    public void input(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter ID: ");
        this.id = Integer.parseInt(scanner.nextLine());
        System.out.print("Enter Book Name: ");
        this.bookName = scanner.nextLine();
        System.out.print("Enter Author Name: ");
        this.authorName = scanner.nextLine();
        System.out.print("Enter Price: ");
        this.price = Float.parseFloat(scanner.nextLine());
    }

    @Override
    public void show(){
        System.out.println("ID: " + id);
        System.out.println("Book Name: " + bookName);
        System.out.println("Author Name: " + authorName);
        System.out.println("Price: " + price);
    }
}
