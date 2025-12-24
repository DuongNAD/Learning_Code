package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class Main {
    public static void main(String[] args) {

        String url = "jdbc:mysql://localhost:3306/user_management";
        String username = "root";
        String password = "";

        System.out.println("Connecting to database...");


        try (Connection connection = DriverManager.getConnection(url, username, password)) {

            if (connection != null) {
                System.out.println("SUCCESS! Connection established successfully.");
            }

            String sqlQuery = "SELECT username, full_name, role FROM users";

            try (Statement statement = connection.createStatement()) {

                try (ResultSet resultSet = statement.executeQuery(sqlQuery)) {

                    System.out.println("\n--- Fetched User Data (Dữ liệu người dùng lấy về) ---");

                    while (resultSet.next()) {


                        String user = resultSet.getString("username");
                        String name = resultSet.getString("full_name");
                        String role = resultSet.getString("role");

                        System.out.printf("Username: %-15s | Full Name: %-20s | Role: %s\n", user, name, role);
                    }

                    System.out.println("----------------------------------------------");
                }
            }

        } catch (SQLException e) {

            System.err.println("\nConnection or Query failed!");
            System.err.println("SQL State: " + e.getSQLState());
            System.err.println("Error Message: " + e.getMessage());
        }
    }
}