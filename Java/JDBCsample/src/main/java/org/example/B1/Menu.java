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
                    case 4:
                        String query3 = "Delete from students WHERE id=?";
                        PreparedStatement pstm3 = null;

                        System.out.print("Enter student id: ");
                        int id3 = scanner.nextInt();

                        try{
                            pstm3 = conn.prepareStatement(query3);
                            pstm3.setInt(1,id3);
                            int row = pstm3.executeUpdate();

                            if(row>0){
                                System.out.println("Deleted student id - "+id3);
                            }
                            else {
                                System.out.println("Can't find student id - "+id3);
                            }
                            conn.close();
                        }
                        catch(SQLException e){
                            e.printStackTrace();
                        }
                        break;
                    case 3:
                        System.out.println("=== UPDATE STUDENT INFO ===");
                        String  query4 = "UPDATE students SET name=?,age=?,email=? WHERE id=?";
                        PreparedStatement pstm4 = null;

                        System.out.println("Enter student id: ");
                        int  id4 = scanner.nextInt();
                        System.out.println("Enter set student name: ");
                        String  name4 = scanner.next();
                        System.out.println("Enter set student age: ");
                        int age4 = scanner.nextInt();
                        System.out.println("Enter set student email: ");
                        String email4 = scanner.next();

                        try{
                            pstm4 = conn.prepareStatement(query4);
                            pstm4.setInt(4,id4);
                            pstm4.setString(1,name4);
                            pstm4.setInt(2,age4);
                            pstm4.setString(3,email4);
                            int rows = pstm4.executeUpdate();

                            if (rows > 0) {
                                System.out.println("Cập nhật thành công! (Update successful)");
                            } else {
                                System.out.println("Không tìm thấy sinh viên có ID: " + id4);
                            }
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
