package BTVN_Java2.Day3;

public class Ex1_Sum {

    @FunctionalInterface
    interface Calculator {
        int sum(int a, int b);
    }

    public static void main(String[] args) {
        int num1 = 15;
        int num2 = 24;

        Calculator addition = (a,b) -> a+b;
        int sum = addition.sum(num1,num2);
        System.out.println("Tong: " + sum);
    }
}