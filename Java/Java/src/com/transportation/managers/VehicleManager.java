package com.transportation.managers;

import com.transportation.vehicles.Vehicle;
import com.transportation.vehicles.bike.Motorbike;
import com.transportation.vehicles.car.Car;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class VehicleManager {
    private List<Car> cars;
    private List<Motorbike> motorbikes;

    public VehicleManager() {
        this.cars = new ArrayList<>();
        this.motorbikes = new ArrayList<>();
    }

    public void inputCars(Scanner scanner) {
        System.out.print("Nhap so Car: ");
        int n = Integer.parseInt(scanner.nextLine());

        for (int i = 0; i < n; i++) {
            System.out.println("Nhap Car Thu " + (i + 1) + " : ");
            Car newCar = new Car();
            newCar.input(scanner);
            this.cars.add(newCar);
        }
    }

    public void inputMotorbikes(Scanner scanner) {
        System.out.println("Nhap so Motorbike: ");
        int n = Integer.parseInt(scanner.nextLine());
        for (int i = 0; i < n; i++) {
            System.out.print("Nhap Motorbike Thu " + (i + 1) + " : ");
            Motorbike newMotorbike = new Motorbike();
            newMotorbike.input(scanner);
            this.motorbikes.add(newMotorbike);
        }
    }

    public void displayCarsSortedByPriceDesc() {
        if (this.cars.isEmpty()) {
            System.out.println("Danh sách xe hơi trống!");
            return;
        }

        List<Car> sortedCars = new ArrayList<>(this.cars);

        sortedCars.sort((Car c1, Car c2) -> Double.compare(c2.getPrice(), c1.getPrice()));

        System.out.println("\n--- DANH SÁCH XE HƠI SẮP XẾP THEO GIÁ GIẢM DẦN ---");
        for (Car car : sortedCars) {
            System.out.println(car);
        }
    }

    public void filterBikesByEngineType(Scanner scanner) {
        if (this.motorbikes.isEmpty()) {
            System.out.println("Danh sách xe Mô tô trống");
            return;
        }
        System.out.print("Nhập loại động cơ bạn muốn tìm: ");
        String engineTypeToFind = scanner.nextLine();

        System.out.println("\n--- KẾT QUẢ TÌM KIẾM XE MÁY VỚI ĐỘNG CƠ '" + engineTypeToFind + "' ---");

        boolean found = false;
        for (Motorbike bike : this.motorbikes) {
            if (bike.getEngineType().equalsIgnoreCase(engineTypeToFind)) {
                bike.display();
                found = true;
            }
        }

        if(!found) {
            System.out.println("Không tìm thấy xe máy nào có loại động cơ phù hợp.");
        }
    }

}
