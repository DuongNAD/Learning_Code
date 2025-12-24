package org.example.B1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Connect {

        String url = "jdbc:mysql://localhost:3306/studentdb";
        String username = "root";
        String password = "";

        public Connection connect(){
            //Tạo đối tượng Connection
            Connection conn = null;

            try {
                conn = DriverManager.getConnection(url,username,password);
                System.out.println("Kết nối thành công");
            } catch (SQLException e) {
                e.printStackTrace();
            }

            return conn;
        }
}
