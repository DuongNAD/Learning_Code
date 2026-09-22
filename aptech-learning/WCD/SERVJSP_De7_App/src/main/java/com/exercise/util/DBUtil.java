package com.exercise.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBUtil {
    // You may need to change these to match your local database settings
    private static final String URL = "jdbc:sqlserver://localhost:1433;databaseName=EmployeeDB";
    private static final String USER = "sa";
    private static final String PASS = "password"; // Update with actual password

    public static Connection getConnection() throws SQLException, ClassNotFoundException {
        // Try SQL Server Driver First
        try {
            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            return DriverManager.getConnection(URL, USER, PASS);
        } catch (Exception e) {
            // Fallback for MySQL if needed
            try {
                Class.forName("com.mysql.cj.jdbc.Driver");
                return DriverManager.getConnection("jdbc:mysql://localhost:3306/EmployeeDB", "root", "password");
            } catch (Exception ex) {
                throw new SQLException("Could not connect to database.");
            }
        }
    }
}
