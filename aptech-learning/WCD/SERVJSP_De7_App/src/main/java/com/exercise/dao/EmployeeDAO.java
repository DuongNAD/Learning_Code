package com.exercise.dao;

import com.exercise.entity.Employee;
import com.exercise.util.DBUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

public class EmployeeDAO {

    public List<Employee> getAllEmployees() {
        List<Employee> list = new ArrayList<>();
        String sql = "SELECT * FROM tblEmployee";
        
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            
            while (rs.next()) {
                Employee emp = new Employee();
                emp.setEmployeeNo(rs.getString("employeeNo"));
                emp.setEmployeeName(rs.getString("employeeName"));
                emp.setPlaceOfWork(rs.getString("placeOfWork"));
                emp.setPhoneNo(rs.getString("phoneNo"));
                list.add(emp);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

    public boolean addEmployee(Employee emp) {
        String sql = "INSERT INTO tblEmployee (employeeNo, employeeName, placeOfWork, phoneNo) VALUES (?, ?, ?, ?)";
        
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            
            ps.setString(1, emp.getEmployeeNo());
            ps.setString(2, emp.getEmployeeName());
            ps.setString(3, emp.getPlaceOfWork());
            ps.setString(4, emp.getPhoneNo());
            
            int row = ps.executeUpdate();
            return row > 0;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteEmployee(String employeeNo) {
        String sql = "DELETE FROM tblEmployee WHERE employeeNo = ?";
        
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            
            ps.setString(1, employeeNo);
            int row = ps.executeUpdate();
            return row > 0;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean isEmployeeExists(String employeeNo) {
        String sql = "SELECT 1 FROM tblEmployee WHERE employeeNo = ?";
        
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            
            ps.setString(1, employeeNo);
            try (ResultSet rs = ps.executeQuery()) {
                return rs.next();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
