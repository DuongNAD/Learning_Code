package Day5;

public class Car extends Vehicle {

    public Car(String brand, String model, int year, double maxSpeed) {
        super(brand, model, year, maxSpeed);
    }

    @Override
    public void displayInfo() {
        System.out.println("--- Thông tin Xe Ô tô ---");
        System.out.println("Hãng sản xuất: " + brand);
        System.out.println("Mẫu xe: " + model);
        System.out.println("Năm sản xuất: " + year);
        System.out.println("Tốc độ tối đa: " + maxSpeed + " km/h");
    }

    @Override
    public double getSpeed() {
        return this.maxSpeed;
    }

    @Override
    public void chargeBattery(int percent) {

    }
}