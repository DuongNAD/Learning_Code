package BTVN_Java2.OnTap;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class StudentManager {
    private static final String FILE_NAME = "students_data.txt";
    Scanner scanner =  new Scanner(System.in);
    private List<Student> studentList = new ArrayList<>();
    public void addStudent(){
        System.out.print("Enter Student ID: ");
        String id = scanner.nextLine();

        String name;
        while(true){
            System.out.print("Student Name (at least 4 characters): ");
            name = scanner.nextLine();
            if(name.length()>=4){
                break;
            }
            System.out.println("Student Name must be at least 4 characters");
        }

        String email;
        while(true){
            System.out.print("Enter email (must contain @ and end with .com): ");
            email = scanner.nextLine();
            if(email.contains("@") && email.contains(".com")){
                break;
            }
            System.out.println("Invalid input! Please check your email format.");
        }

        System.out.print("Enter Course: ");
        String course = scanner.nextLine();

        System.out.print("Is paid? (true/false): ");
        boolean status = Boolean.parseBoolean(scanner.nextLine());

        studentList.add(new Student(id,name,email,course,status));
        System.out.println("Student added successfully.");
    }

    public void saveToFile(){
        try( BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_NAME))){
            for(Student student : studentList){
                bw.write(student.toString());
                bw.newLine();
            }
            System.out.println("Data saved to: " + FILE_NAME);
        }
        catch (IOException e){
            System.out.println("Error saving to file: " + e.getMessage());
        }
    }

    public void readFromFile() {
        System.out.println("\n--- Student List (Tabular Format) ---");
        System.out.printf("%ss %s %s %s %s\n", "ID", "Name", "Email", "Course", "Paid");
        System.out.println("---------------------------------------------------------------------------------------------");

        try (BufferedReader br = new BufferedReader(new FileReader(FILE_NAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length == 5) {
                    System.out.printf("%-10s %-20s %-25s %-20s %-10s\n", data[0], data[1], data[2], data[3], data[4]);
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public void searchByCourse(){
        System.out.print("Enter course title to search: ");
        String title = scanner.nextLine();
        boolean found = false;
        for(Student student : studentList){
            if (student.getEnrolledCourse().equalsIgnoreCase(title)){
                System.out.println("Found student: "+ student.getId() + " - " + student.getName() + " - " + student.getEmail());
                found = true;
            }
        }
        if(!found){
            System.out.println("Invalid course title");
        }
    }
}
