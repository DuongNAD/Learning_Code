package org.example;

import java.util.Scanner;

public class Validator {
    private static final Scanner scanner =  new Scanner(System.in);

    public static int checkInput(){
        while(true){
            try{
                int result = Integer.parseInt(scanner.nextLine());
                if(result <0){
                    System.out.println("Enter grater than 0");
                    continue;
                }
                return result;
            } catch (NumberFormatException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
