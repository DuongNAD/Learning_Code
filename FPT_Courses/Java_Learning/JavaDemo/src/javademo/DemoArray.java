/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javademo;

import java.util.Arrays;
import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class DemoArray {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int arr[] = new int[10];
        try {
            for (int i = 0; i < 10; i++) {
                System.out.print("Enter number " + (i + 1) + ": ");
                arr[i] = scanner.nextInt();
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        int sumEven = 0;
        int sumOdd = 0;
        for (int i = 0; i < 10; i++) {
            if (arr[i] % 2 == 0) {
                sumEven = sumEven + arr[i];
            } else {
                sumOdd = sumOdd + arr[i];
            }
        }
        System.out.println("Sum even number = " + sumEven);
        System.out.println("Sum odd number = " + sumOdd);

        for (int i = 0; i <10; i++) {
            if (arr[i] < 2) continue;
            
            boolean isPrime = true;
            
            for (int j = 2; j <= Math.sqrt(arr[i]); j++) {
                if (arr[i] % j ==0) {
                    isPrime = false;
                    break;
                }
            }
            if(isPrime == true){
                System.out.println(arr[i] + " ");
            }
        }
        int[] sortedArr = Arrays.copyOf(arr, arr.length);
        Arrays.sort(sortedArr);
        System.out.println("Min = " + sortedArr[0]);
        System.out.println("Max = " + sortedArr[sortedArr.length-1]);
        
        int count = 0;
        int index = 0;
        for (int i = 0; i < arr.length;i++){
            if (arr[i] == sortedArr[sortedArr.length -1]){
                count++;
            }
            else if(count == 2){
                index = i;
            }
            
        }
    }

}
