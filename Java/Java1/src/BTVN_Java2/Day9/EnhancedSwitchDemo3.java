package BTVN_Java2.Day9;

import java.util.Scanner;

public class EnhancedSwitchDemo3 {
    public static void main(String[] args) {
    Scanner scanner=new Scanner(System.in);
    System.out.println("Enter Product Name: ");
    int ivar = scanner.nextInt();
    String numberYieldColon = switch(ivar){
        case 0: yield "Texas";
        case 1: yield "California";
        case 2: {
            String colResult  = "Exclusively";
            colResult = colResult + "Seattle";
            yield colResult;
        }
    }
    }
}
