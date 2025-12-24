package BTVN_Java2.Day3;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Ex2_ChuoiSangChu {

    public static void main(String[] args) {
        List<String> words = Arrays.asList("Java", "c#", "PyThon", "JavaScript", "Golang");

        System.out.println("--- Danh sách gốc ---");
        System.out.println(words);
        List<String> uppercaseWords = words.stream()
                .map(s -> s.toUpperCase())
                .collect(Collectors.toList());

        System.out.println("\n--- Chuyển sang CHỮ HOA ---");
        System.out.println(uppercaseWords);

        List<String> lowercaseWords = words.stream()
                .map(s -> s.toLowerCase())
                .collect(Collectors.toList());

        System.out.println("\n--- Chuyển sang chữ thường ---");
        System.out.println(lowercaseWords);
    }
}