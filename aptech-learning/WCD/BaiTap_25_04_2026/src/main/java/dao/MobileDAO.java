package dao;

import models.Mobile;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class MobileDAO {
    // THAY ĐỔI USERNAME / PASSWORD MYSQL CỦA BẠN TẠI ĐÂY
    private String jdbcURL = "jdbc:mysql://localhost:3306/MobileDB";
    private String jdbcUsername = "root";
    private String jdbcPassword = ""; 

    protected Connection getConnection() {
        Connection connection = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(jdbcURL, jdbcUsername, jdbcPassword);
        } catch (SQLException | ClassNotFoundException e) {
            e.printStackTrace();
        }
        return connection;
    }

    public List<Mobile> selectAllMobiles() {
        List<Mobile> mobiles = new ArrayList<>();
        String query = "SELECT * FROM Mobile";
        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query);
             ResultSet rs = preparedStatement.executeQuery()) {
            while (rs.next()) {
                mobiles.add(new Mobile(rs.getInt("id"), rs.getString("name"), rs.getDouble("price"),
                        rs.getString("warranty"), rs.getString("accessories"), rs.getBoolean("inOutStock"), rs.getString("image")));
            }
        } catch (SQLException e) { e.printStackTrace(); }
        return mobiles;
    }

    public Mobile selectMobile(int id) {
        Mobile mobile = null;
        String query = "SELECT * FROM Mobile WHERE id = ?";
        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setInt(1, id);
            ResultSet rs = preparedStatement.executeQuery();
            if (rs.next()) {
                mobile = new Mobile(rs.getInt("id"), rs.getString("name"), rs.getDouble("price"),
                        rs.getString("warranty"), rs.getString("accessories"), rs.getBoolean("inOutStock"), rs.getString("image"));
            }
        } catch (SQLException e) { e.printStackTrace(); }
        return mobile;
    }

    public void insertMobile(Mobile mobile) {
        String query = "INSERT INTO Mobile (name, price, warranty, accessories, inOutStock, image) VALUES (?, ?, ?, ?, ?, ?)";
        try (Connection connection = getConnection();
             PreparedStatement preparedStatement = connection.prepareStatement(query)) {
            preparedStatement.setString(1, mobile.getName());
            preparedStatement.setDouble(2, mobile.getPrice());
            preparedStatement.setString(3, mobile.getWarranty());
            preparedStatement.setString(4, mobile.getAccessories());
            preparedStatement.setBoolean(5, mobile.isInOutStock());
            preparedStatement.setString(6, mobile.getImage());
            preparedStatement.executeUpdate();
        } catch (SQLException e) { e.printStackTrace(); }
    }
}
