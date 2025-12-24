package BTVN_Java2.Day4.LE_Ex10;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

public class OrderRepository {
    public static List<Order> getOrders() {
        Customer c1 = new Customer(1L, "Anh Duong", 1);
        Customer c2 = new Customer(2L, "Hoang Hieu", 2);
        Customer c3 = new Customer(3L, "Pham Vu", 1);

        // 2. Tạo Sản phẩm (Đủ các loại Books, Baby, Toys)
        Product p1 = new Product(1L, "Effective Java", "Books", 120.0);
        Product p2 = new Product(2L, "Head First Java", "Books", 50.0);
        Product p3 = new Product(3L, "Clean Code", "Books", 150.0);

        Product p4 = new Product(4L, "Bỉm Huggies", "Baby", 20.0);
        Product p5 = new Product(5L, "Sữa Meiji", "Baby", 40.0);

        Product p6 = new Product(6L, "Lego Robot", "Toys", 200.0);
        Product p7 = new Product(7L, "Xe điều khiển", "Toys", 50.0);

        Order o1 = new Order(101L, "Delivered", LocalDate.of(2021, 2, 15), LocalDate.of(2021, 2, 17),
                Arrays.asList(p1, p2), c1);

        Order o2 = new Order(102L, "Pending", LocalDate.of(2021, 3, 14), null,
                Arrays.asList(p4, p5), c2);

        Order o3 = new Order(103L, "Delivered", LocalDate.of(2021, 4, 1), LocalDate.of(2021, 4, 3),
                Arrays.asList(p3, p5, p6), c2);

        Order o4 = new Order(104L, "New", LocalDate.of(2021, 4, 5), null,
                Arrays.asList(p7), c3);

        return Arrays.asList(o1, o2, o3, o4);
    }
}
