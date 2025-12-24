package Day5;

public class Motorbike extends Vehicle {
    private int engineCapacity;

    public Motorbike(String brand, String model, int year, double maxSpeed, int engineCapacity) {
        super(brand, model, year, maxSpeed);
        this.engineCapacity = engineCapacity;
    }

    @Override
    public void displayInfo() {
        System.out.println("--- Thông tin Xe Máy ---");
        System.out.println("Hãng sản xuất: " + brand);
        System.out.println("Mẫu xe: " + model);
        System.out.println("Năm sản xuất: " + year);
        System.out.println("Tốc độ tối đa: " + maxSpeed + " km/h");
        System.out.println("Dung tích xi lanh: " + engineCapacity + "cc");
    }

    @Override
    public double getSpeed() {
        return this.maxSpeed;
    }

    @Override
    public void chargeBattery(int percent) {

    }
}