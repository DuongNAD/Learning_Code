/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package javademo;

import java.util.Scanner;

/**
 *
 * @author DELL
 */
public class InputInformationStudent {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int id = 0;
        String name = null;
        int age = 0;
        String address = null;
        try{
            System.out.print("Enter ID: ");
            id = Integer.parseInt(scanner.nextLine());
            System.out.print("Enter name: ");
            name = scanner.nextLine();
            System.out.print("Enter age: ");
            age = Integer.parseInt(scanner.nextLine());
            System.out.print("Enter address: ");
            address = scanner.nextLine();
            
        }
        catch(Exception e){
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println("ID: " + id + " - " + "Name: " + name + " - " + "Age: " +age + " - " + "Address: " + address );
    }
}
