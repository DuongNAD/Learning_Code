package BTVN_Java2.Day4.LE_Ex10;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class LE_FilterBooks {
    public static void main(String[] args) {
        List<Order> orders = OrderRepository.getOrders();

        System.out.println("--- Sách có giá > 100 ---");

        orders.stream()
                .flatMap(order -> order.getProducts().stream())
                .filter(p -> p.getCategory().equals("Books"))
                .filter(p->p.getPrice()>100)
                .collect(Collectors.toList())
                .forEach(System.out::println);
    }
}
