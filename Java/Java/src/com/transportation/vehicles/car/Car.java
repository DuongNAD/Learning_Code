package com.transportation.vehicles.car;

import com.transportation.vehicles.Vehicle;

import java.util.Scanner;

public class Car extends Vehicle {
    private int seatCount;
    private String Brand;

    public Car(){

    }

    public Car(String id, String name, int year, double price ,int seatCount, String Brand){
        super(id, name, year,price);
        this.seatCount = seatCount;
        this.Brand = Brand;
    }

    public int getSeatCount() {
        return seatCount;
    }
    public void setSeatCount(int seatCount) {
        this.seatCount = seatCount;
    }
    public String getBrand() {
        return Brand;
    }
    public void setBrand(String Brand) {
        this.Brand = Brand;
    }
    @Override
    public void input(Scanner scanner) {
        System.out.println("Nhap ID: ");
        this.id = scanner.nextLine();
        System.out.println("Nhap Ten xe: ");
        this.name = scanner.nextLine();
        System.out.print("Enter seat count: ");
        this.seatCount = scanner.nextInt();
        System.out.println("Nhap hang san xuat: ");
        this.Brand = scanner.nextLine();
        System.out.println("Nhap nam san xuat: ");
        this.year = Integer.parseInt(scanner.nextLine());
        System.out.println("Nhap gia: ");
        this.price = Double.parseDouble(scanner.nextLine());

    }

    @Override
    public void display() {
        System.out.println("--- Thông tin chi tiết xe hơi ---");
        System.out.println("ID: " + this.id);
        System.out.println("Tên xe: " + this.name);
        System.out.println("Hãng sản xuất: " + this.Brand);
        System.out.println("Năm sản xuất: " + this.year);
        System.out.printf("Giá bán: %,.0f VND\n", this.price);
        System.out.println("Số chỗ ngồi: " + this.seatCount);
        System.out.println("---------------------------------");
    }
}
