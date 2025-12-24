package BTVN_Java2.OnTap.CosmeticProductOT;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner =  new Scanner(System.in);
        List<CosmeticProduct> list = new ArrayList<>();

        System.out.println("Enter the number of cosmetic products:");
        for (int i = 0; i < 3; i++) {
            System.out.println("Nhập thông tin sản phẩm thứ " + (i + 1) + ":");
            System.out.println("ID: ");
            int id = scanner.nextInt();
            System.out.println("Name: ");
            String name = scanner.next();
            System.out.println("Price: ");
            double price = scanner.nextDouble();

            list.add(new CosmeticProduct(id, name, price));
        }

        try(ObjectOutputStream oss = new ObjectOutputStream(new FileOutputStream("cosmetics.dat"))){
            oss.writeObject(list);
            System.out.println("Cosmetic product data saved!");
        }
        catch(Exception ex){
            ex.printStackTrace();
        }

        List<CosmeticProduct> list2 = new ArrayList<>();
        try(ObjectInputStream osis = new ObjectInputStream(new FileInputStream("cosmetics.dat"))){
            list2 = (List<CosmeticProduct>) osis.readObject();
        }
        catch (IOException | ClassNotFoundException e){
            e.printStackTrace();
        }

        Collections.sort(list2);

        System.out.println("Danh sách sản phẩm sắp xếp theo giá");
        for(CosmeticProduct c : list2){
            System.out.println(c);
        }
    }
}
