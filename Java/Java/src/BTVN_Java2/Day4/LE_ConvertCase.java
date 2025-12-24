package BTVN_Java2.Day4;

import Day4.User;

import java.util.ArrayList;
import java.util.List;

import java.util.Arrays;
import java.util.List;
import java.util.function.UnaryOperator;

public class LE_ConvertCase {

    public static void main(String[] args) {
        List<String> names = Arrays.asList("Java", "Python", "C++", "Php");

        System.out.println("Original: " + names);

        System.out.print("To UpperCase: ");
        transformList(names, s -> s.toUpperCase());

        System.out.print("To LowerCase: ");
        transformList(names, s -> s.toLowerCase());
    }

    public static void transformList(List<String> list, UnaryOperator<String> operator) {
        for (String item : list) {
            String result = operator.apply(item);
            System.out.print(result + " ");
        }
        System.out.println();
    }
}
