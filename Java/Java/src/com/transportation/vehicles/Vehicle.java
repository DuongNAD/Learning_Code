package com.transportation.vehicles;

import com.transportation.interfaces.IVehicle;

import java.util.Scanner;

public abstract class Vehicle implements IVehicle {
    protected String id;
    protected String name;
    protected int year;
    protected double price;

    public Vehicle(){

    }

    public Vehicle(String id, String name, int year, double price) {
        this.id = id;
        this.name = name;
        this.year = year;
        this.price = price;
    }

    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getYear() {
        return year;
    }
    public void setYear(int year) {
        this.year = year;
    }
    public double getPrice() {
        return price;
    }
    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public abstract void input(Scanner scanner);

    @Override
    public abstract void display();
}
