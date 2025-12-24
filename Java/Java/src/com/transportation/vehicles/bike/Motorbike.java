package com.transportation.vehicles.bike;

import com.transportation.vehicles.Vehicle;
import java.util.Scanner;

public class Motorbike extends Vehicle {
    private String engineType;
    private double Weight;

    public Motorbike() {

    }

    public Motorbike(String id, String name, int year, double price, String engineType, double Weight) {
        super(id, name, year, price);
        this.engineType = engineType;
        this.Weight = Weight;
    }

    public String getEngineType() {
        return engineType;
    }
    public void setEngineType(String engineType) {
        this.engineType = engineType;
    }
    public double getWeight() {
        return Weight;
    }
    public void setWeight(double weight) {
        Weight = weight;
    }

    @Override
    public void input(Scanner scanner) {
        System.out.println("--- Nhập thông tin xe máy ---");

        System.out.print("Nhập ID: ");
        this.id = scanner.nextLine();
        System.out.print("Nhập Tên xe: ");
        this.name = scanner.nextLine();
        System.out.print("Nhập Loại động cơ: ");
        this.engineType = scanner.nextLine();
        System.out.print("Nhập Năm sản xuất: ");
        this.year = Integer.parseInt(scanner.nextLine());
        System.out.print("Nhập Giá bán: ");
        this.price = Double.parseDouble(scanner.nextLine());
        System.out.print("Nhập Cân nặng (kg): ");
        this.Weight = Double.parseDouble(scanner.nextLine());
    }
    @Override
    public void display() {
        System.out.println("--- Thông tin chi tiết xe máy ---");
        System.out.println("ID: " + this.id);
        System.out.println("Tên xe: " + this.name);
        System.out.println("Loại động cơ: " + this.engineType);
        System.out.println("Năm sản xuất: " + this.year);
        System.out.printf("Giá bán: %,.0f VND\n", this.price);
        System.out.println("Cân nặng: " + this.Weight + " kg");
        System.out.println("---------------------------------");
    }
}
