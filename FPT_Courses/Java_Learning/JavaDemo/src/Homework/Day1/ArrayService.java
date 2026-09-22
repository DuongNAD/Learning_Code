/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Homework.Day1;

import java.util.Arrays;
import java.util.Scanner;
/**
 *
 * @author DELL
 */
public class ArrayService {

    private int[] array;

    public ArrayService(int n) {
        this.array = new int[n];
    }
    
    // Hàm nhập các phần tử của mảng
    public void InputArray(Scanner scanner) {
        try{
            System.out.println("Enter Array: ");
            for (int i = 0; i < array.length; i++) {
                System.out.print("Enter number " + (i + 1) + ": ");
                array[i] = scanner.nextInt();
            }
        }
        catch(Exception e){
            System.out.println("Error: " + e.getMessage());
        }
    }
    
    // Hàm tính tổng các phần tử trong mảng
    public void SumNumber() {
        int sumEven = 0;
        int sumOdd = 0;

        for (int i = 0; i < array.length; i++) {
            if (array[i] % 2 == 0) {
                sumEven = sumEven + array[i];
            } else {
                sumOdd = sumOdd + array[i];
            }
        }

        System.out.println("Sum even number = " + sumEven);
        System.out.println("Sum odd number =  " + sumOdd);
    }
    
    // Hàm check số nguyên tố
    public void CheckIsPrime() {
        boolean isPrime = false;
        for (int i = 0; i < array.length; i++) {
            if(array[i] <2){
                continue;
            }
            isPrime = true;
            for (int j = 2; j <= Math.sqrt(array[i]);j++) {
                if(array[i] % j == 0){
                    isPrime = false;
                    break;
                }
            }
            if(isPrime == true){
                System.out.print(array[i] + " ");
            }
        }
    }
    
    // Hàm tìm max min
    public void FindMaxMin(){
        int[] sortedArray = array.clone();
        Arrays.sort(sortedArray); 
        System.out.println("Min = " + sortedArray[0]);
        System.out.println("Max = " + sortedArray[sortedArray.length - 1]);
    }   
    
    // Hàm tìm vị trí phần tử max thứ 2
    public void FindSecondMax(){
        if (array.length < 2) {
            System.out.println("Array needs at least 2 elements.");
            return;
        }
        int maxNumber = array[0];
        for(int i =1;i<array.length;i++){
            if(array[i] > maxNumber){
                maxNumber = array[i];
            }
        }
        int count = 0;
        int index = -1;
        
        for (int i = 0; i < array.length; i++) {
            if (array[i] == maxNumber) {
                count++; 
                if (count == 2) {
                    index = i; 
                    break;     
                }
            }
        }
        
        if(index !=-1) {
            System.out.println("Max number is: " + maxNumber);
            System.out.println("Vị trí max thứ 2 là: " + index);
            for (int i = 0;i< index-1;i++){
                for (int j =i+1;j<index; j++){
                    if(array[i] > array[j]){
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }
            
            for(int i = index ;i <array.length -1 ;i++){
                for(int j =i +1;j<array.length;j++){
                    if(array[i] < array[j]){
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }
            
            System.out.print("Array sorted: " + Arrays.toString(array));
        }
        else{
            System.out.println("Không tìm thấy phần tử max thứ 2");
        }
        
        
    }
    
    public void CountNumber(Scanner scanner){
        System.out.print("Enter number find: ");
        int number = scanner.nextInt();
        int count =0;
        for(int i =0;i<array.length;i++){
            if(number == array[i]){
                count++;
            }
        }
        System.out.printf("Count %d = %d: ",number,count);
    }
    
    // Hàm thêm phần tử
    public void addNumber(Scanner scanner){
        System.out.print("Enter number want to add: ");
        int numberAdd = scanner.nextInt();
        
        System.out.printf("Enter index want to add ( >=0 & <=%d): ", array.length);
        int indexAdd = scanner.nextInt();
        
        if(indexAdd <0 || indexAdd >array.length){
            System.out.println("Error index");
            return;
        }   
        
        int[] newArray = new int[array.length+1];    
        for(int i =0;i < newArray.length;i++){
            if(i==indexAdd){
                newArray[i] = numberAdd;
            }
            else if(i < indexAdd){
                newArray[i] = array[i];
            }
            else if(i> indexAdd){
                newArray[i] = array[i-1];
            }
        }
        this.array = newArray;
        System.out.println("Array added: " + Arrays.toString(this.array));
    }
    
    // Hàm xóa phần tử 
    public void deleteNumber(Scanner scanner){
        System.out.print("Enter number want to delete: ");
        int deleteNumber = scanner.nextInt();
        int count = 0;
        for (int x : array) {
            if (x == deleteNumber) {
                count++;
            }
        }
        
        if (count == 0) {
            System.out.println("Number " + deleteNumber + " not found in array.");
            return;
        }
        
        int[] deletedArray = new int[array.length-count];
        int index =0;
        for (int i = 0; i < array.length; i++) {
            if (array[i] != deleteNumber) {
                deletedArray[index] = array[i];
                index++;
            }
        }
        this.array = deletedArray;
        System.out.println("Array deleted: " + Arrays.toString(this.array));
    }
}
