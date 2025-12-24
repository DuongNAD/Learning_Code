package BTVN_Java2.OnTap.OnTap1;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner =  new Scanner(System.in);

        List<Vulnerability> list = new ArrayList<>();

        System.out.println("Enter Vulnerability List: ");
        for(int i = 0; i < 3; i++){
            System.out.print("Enter cveID: ");
            String cveID = scanner.nextLine();
            System.out.print("Enter description: ");
            String description = scanner.nextLine();
            System.out.print("Enter cvssScore: ");
            double cvssScore = scanner.nextDouble();

            scanner.nextLine();

            list.add(new Vulnerability(cveID, description, cvssScore));
        }

        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("vulnerability.txt"))) {
            oos.writeObject(list);
            System.out.println("Vulnerability List written to disk");
        }
        catch (Exception e){
            e.printStackTrace();
        }

        List<Vulnerability> list1 = new ArrayList<>();
        try(ObjectInputStream osis = new ObjectInputStream(new FileInputStream("vulnerability.txt"))){
            list1 = (List<Vulnerability>) osis.readObject();
        }
        catch (Exception e){
            e.printStackTrace();
        }

        Collections.sort(list1);
        System.out.println("Vulnerability sort: ");
        for(int i = 0; i < list1.size(); i++){
            System.out.println(list1.get(i));
        }
    }
}
