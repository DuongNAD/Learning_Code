package Day5;

public class ElectricBike extends Vehicle implements Electric {
    private int batteryLevel; // Mức pin từ 0-100

    public ElectricBike(String brand, String model, int year, double maxSpeed) {
        super(brand, model, year, maxSpeed);
        this.batteryLevel = 100; // Khởi tạo với 100% pin
    }

    @Override
    public void displayInfo() {
        System.out.println("--- Thông tin Xe Đạp Điện ---");
        System.out.println("Hãng sản xuất: " + brand);
        System.out.println("Mẫu xe: " + model);
        System.out.println("Năm sản xuất: " + year);
        System.out.println("Tốc độ tối đa lý thuyết: " + maxSpeed + " km/h");
        System.out.println("Mức pin hiện tại: " + batteryLevel + "%");
    }

    @Override
    public double getSpeed() {
        // Tốc độ thực tế phụ thuộc vào mức pin.
        // Nàng thơ giả định công thức: tốc độ = tốc độ tối đa * (mức pin / 100)
        return this.maxSpeed * (this.batteryLevel / 100.0);
    }

    @Override
    public void chargeBattery(int percent) {
        System.out.println("Đang sạc pin...");
        this.batteryLevel += percent;
        if (this.batteryLevel > 100) {
            this.batteryLevel = 100;
        }
        System.out.println("Sạc thành công. Mức pin hiện tại: " + this.batteryLevel + "%");
    }

    @Override
    public void chargeBattery() {

    }

    @Override
    public int getBatteryLevel() {
        return this.batteryLevel;
    }

    public void ride(int distance) {
        System.out.println("Đang di chuyển " + distance + " km...");
        int batteryConsumed = distance / 2;
        this.batteryLevel -= batteryConsumed;
        if (this.batteryLevel < 0) {
            this.batteryLevel = 0;
        }
        System.out.println("Hành trình kết thúc. Pin còn lại: " + this.batteryLevel + "%");
    }
}