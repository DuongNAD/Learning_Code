package StudentSytem;

import javax.swing.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DatabaseStudentConnection {

    private static final String URL = "jdbc:mysql://localhost:3306/studentdb";
    private static final String USER = "root";
    private static final String PASS = "";

    public static Connection getConnection(){
        Connection conn = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn =  DriverManager.getConnection(URL, USER, PASS);
            System.out.println("Connected to database successfully");
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Connect failed!");
            e.printStackTrace();
        }
        return conn;
    }
}
