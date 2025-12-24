    package org.example.B1;

    import java.sql.*;
    import java.util.InputMismatchException;
    import java.util.Scanner;

    public class Menu {

        public static void main(String[] args) {
            Scanner scanner =new Scanner(System.in);
            Connect connectJDBC = new Connect();
            Connection conn = connectJDBC.connect();

            while(true){
                System.out.println("==== STUDENT MENU ====");
                System.out.println("1. Add student");
                System.out.println("2. View All students");
                System.out.println("3. Update student");
                System.out.println("4. Delete student");
                System.out.println("5. Exit");
                System.out.print("Enter your choice (1->5): ");
                int luachon = -1;

                try{
                    luachon = scanner.nextInt();
                }
                catch(InputMismatchException e){
                    System.out.println("Invalid input");
                    continue;
                }

                switch(luachon){
                    case 1:
                        System.out.print("Enter student name: ");
                        String name = scanner.next();
                        System.out.print("Enter student age: ");
                        int age = scanner.nextInt();
                        System.out.print("Enter student email: ");
                        String email = scanner.next();
                        String query1 = "INSERT INTO students (id,name,age,email) VALUES (null,?, ?, ?)";
                        PreparedStatement pstm = null;

                        try{
                            pstm = conn.prepareStatement(query1);

                            pstm.setString(1, name);
                            pstm.setInt(2, age);
                            pstm.setString(3, email);

                            int row = pstm.executeUpdate();
                            if(row != 0){
                                System.out.println("Thêm thành công: " +name +" - "+age+" - "+email);
                            }

                            conn.close();

                        }
                        catch(SQLException e){
                            e.printStackTrace();
                        }
                        break;
                    case 2:
                        String query2 = "SELECT * FROM students";
                        Statement stm = null;


                        try {
                            stm = conn.createStatement();
                            ResultSet rs = stm.executeQuery(query2);
                            System.out.println("=== DANH SÁCH HỌC SINH ===");
                            while(rs.next()){
                                int  id2 = rs.getInt("id");
                                String name2 = rs.getString("name");
                                int age2 = rs.getInt("age");
                                String email2 = rs.getString("email");

                                System.out.println(id2 + " - " + name2 + " - " + age2 + " - " + email2);

                            }
                            conn.close();
                        }
                        catch (SQLException e){
                            e.printStackTrace();
                        }
                        break;

                    case 3:
                        System.out.println("=== UPDATE STUDENT INFO ===");
                        String  query3 = "UPDATE students SET name=?,age=?,email=? WHERE id=?";
                        PreparedStatement pstm3 = null;

                        System.out.println("Enter student id: ");
                        int  id3 = scanner.nextInt();
                        System.out.println("Enter set student name: ");
                        String  name3 = scanner.next();
                        System.out.println("Enter set student age: ");
                        int age3 = scanner.nextInt();
                        System.out.println("Enter set student email: ");
                        String email3 = scanner.next();

                        try{
                            pstm3 = conn.prepareStatement(query3);
                            pstm3.setInt(4,id3);
                            pstm3.setString(1,name3);
                            pstm3.setInt(2,age3);
                            pstm3.setString(3,email3);
                            int rows = pstm3.executeUpdate();

                            if (rows > 0) {
                                System.out.println("Cập nhật thành công! (Update successful)");
                            } else {
                                System.out.println("Không tìm thấy sinh viên có ID: " + id3);
                            }
                        }
                        catch(SQLException e){
                            e.printStackTrace();
                        }
                        break;
                    case 4:
                        String query4 = "Delete from students WHERE id=?";
                        PreparedStatement pstm4 = null;

                        System.out.print("Enter student id: ");
                        int id4 = scanner.nextInt();

                        try{
                            pstm4 = conn.prepareStatement(query4);
                            pstm4.setInt(1,id4);
                            int row = pstm4.executeUpdate();

                            if(row>0){
                                System.out.println("Deleted student id - "+id4);
                            }
                            else {
                                System.out.println("Can't find student id - "+id4);
                            }
                            conn.close();
                        }
                        catch(SQLException e){
                            e.printStackTrace();
                        }
                        break;
                    case 5:
                        System.out.println("Thank you for using this program");
                        break;
                    default:
                        System.out.println("Invalid input");
                        break;
                }
            }
        }
    }
