package Day5;

public abstract class Vehicle {
    protected String brand;
    protected String model;
    protected int year;
    protected double maxSpeed;

    public Vehicle(String brand, String model, int year, double maxSpeed) {
        this.brand = brand;
        this.model = model;
        this.year = year;
        this.maxSpeed = maxSpeed;
    }

    public abstract void displayInfo();

    public abstract double getSpeed();

    public abstract void chargeBattery(int percent);
}