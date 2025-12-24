package BTVN_Java2.Day4.LE_Ex10;

import java.util.List;
import java.util.stream.Collectors;

public class LE_FilterBabyOrders {
    public static void main(String[] args) {

        List<Order> orders = OrderRepository.getOrders();

        List<Order> result = orders.stream()
                .filter(order ->

                        order.getProducts().stream()
                                .anyMatch(product -> product.getCategory().equalsIgnoreCase("Baby"))
                )
                .collect(Collectors.toList());

        System.out.println("Đơn hàng có đồ Baby:");
        result.forEach(System.out::println);
    }
}
