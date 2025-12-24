package com.library.literature;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Year;
import java.util.Scanner;

public class LiteraryWork implements ILiteraryWork {
    private String title;
    private String author;
    private int publicationYear;
    private int pageCount;

    public LiteraryWork() {}
    public LiteraryWork(String title, String author, int publicationYear, int pageCount) {
        this.title = title;
        this.author = author;
        this.publicationYear = publicationYear;
        this.pageCount = pageCount;
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
    public int getPublicationYear() {
        return publicationYear;
    }
    public void setPublicationYear(int publicationYear) {
        this.publicationYear = publicationYear;
    }
    public int getPageCount() {
        return pageCount;
    }
    public void setPageCount(int pageCount) {
        this.pageCount = pageCount;
    }

    @Override
    public void inputDetails() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        int currentYear = Year.now().getValue();

        try {
            while (true) {
                System.out.print("Nhập tiêu đề (title) (ít nhất 3 ký tự): ");
                this.title = reader.readLine();
                if (this.title.length() >= 3) {
                    break;
                }
                System.out.println("Lỗi: Tiêu đề phải có ít nhất 3 ký tự. Vui lòng nhập lại.");
            }

            while (true) {
                System.out.print("Nhập tác giả (author) (ít nhất 3 ký tự): ");
                this.author = reader.readLine();
                if (this.author.length() >= 3) {
                    break;
                }
                System.out.println("Lỗi: Tên tác giả phải có ít nhất 3 ký tự. Vui lòng nhập lại.");
            }

            while (true) {
                try {
                    System.out.print("Nhập năm xuất bản (publicationYear) ( > 1500 và <= " + currentYear + "): ");
                    this.publicationYear = Integer.parseInt(reader.readLine());
                    if (this.publicationYear > 1500 && this.publicationYear <= currentYear) {
                        break;
                    }
                    System.out.println("Lỗi: Năm xuất bản phải lớn hơn 1500 và không quá " + currentYear + ".");
                } catch (NumberFormatException e) {
                    System.out.println("Lỗi: Vui lòng nhập một con số hợp lệ cho năm.");
                }
            }

            while (true) {
                try {
                    System.out.print("Nhập số trang (pageCount) (phải > 0): ");
                    this.pageCount = Integer.parseInt(reader.readLine());
                    if (this.pageCount > 0) {
                        break;
                    }
                    System.out.println("Lỗi: Số trang phải lớn hơn 0.");
                } catch (NumberFormatException e) {
                    System.out.println("Lỗi: Vui lòng nhập một con số hợp lệ cho số trang.");
                }
            }


        } catch (IOException e) {
            System.out.println("Đã xảy ra lỗi khi đọc dữ liệu đầu vào: " + e.getMessage());
        }
    }

    public boolean isClassic() {
        return this.publicationYear < 1970;
    }


    @Override
    public void displayDetails() {
        System.out.println("--- Chi tiết tác phẩm ---");
        System.out.println("Title: " + this.title);
        System.out.println("Author: " + this.author);
        System.out.println("Publication Year: " + this.publicationYear);
        System.out.println("Page Count: " + this.pageCount);
    }
}
