package BTVN_Java2.Day3.Stream_API;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Product {
    private Long id;
    private String name;
    private String category;
    private Double price;

    public Product() {

    }

    public Product(Long id, String name, String category, Double price) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
    }
    public Long getId() {
        return id;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public String getCategory() {
        return category;
    }
    public void setCategory(String category) {
        this.category = category;
    }
    public Double getPrice() {
        return price;
    }
    public void setPrice(Double price) {
        this.price = price;
    }
    @Override
    public String toString() {
        return "Product:{id=" + id + ", name=" + name + ", category=" + category + ", price=" + price + "}";
    }
}

class Order {
    private Long id;
    private String status;
    private LocalDate orderDate;
    private List<Product> products;

    public Order(Long id, String status, List<Product> products) {
        this.id = id;
        this.status = status;
        this.products = products;
    }

    public List<Product> getProducts() {
        return products;
    }

    @Override
    public String toString() {
        return "Order{id=" + id + ", status='" + status + "'}";
    }
}

public class LambdaFilterProductExample {

    public static void main(String[] args) {

        Product p1 = new Product(1L, "Java 8 in Action", "Books", 120.0);
        Product p2 = new Product(2L, "Baby Toy Set", "Baby", 50.0);
        Product p3 = new Product(3L, "Laptop Stand", "Electronics", 150.0);
        Product p4 = new Product(4L, "Clean Code", "Books", 105.0);
        Product p5 = new Product(5L, "Spring Boot Guide", "Books", 95.0);
        Product p6 = new Product(6L, "Advanced Java", "Books", 180.0);

        List<Product> allProducts = Arrays.asList(p1, p2, p3, p4, p5, p6);

        System.out.println("--- Danh sách sản phẩm gốc ---");
        allProducts.forEach(System.out::println);

        List<Order> allOrders = Arrays.asList(
                new Order(101L, "New", Arrays.asList(p1, p2, p3)),
                new Order(102L, "Delivered", Arrays.asList(p1, p3, p4)),
                new Order(103L, "Shipped", Arrays.asList(p2, p4))
        );


        List<Product> filteredBooks = allProducts.stream()
                .filter(p -> p.getCategory().equals("Books"))
                .filter(p -> p.getPrice() > 100.0)
                .collect(Collectors.toList());

        System.out.println("\n--- KẾT QUẢ LỌC (Category: Books & Price > 100) ---");
        filteredBooks.forEach(System.out::println);


        List<Order> babyOrders = allOrders.stream()
                .filter(order ->
                        order.getProducts().stream()
                                .anyMatch(product -> product.getCategory().equals("Baby"))
                )
                .collect(Collectors.toList());

        System.out.println("\n--- KẾT QUẢ LỌC (Đơn hàng có SP thuộc Category: Baby) ---");
        babyOrders.forEach(System.out::println);
    }
}