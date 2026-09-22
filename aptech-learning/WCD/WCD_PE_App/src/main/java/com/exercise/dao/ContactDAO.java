package com.exercise.dao;

import com.exercise.entity.Contact;
import com.exercise.util.DBUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class ContactDAO {

    public List<Contact> getAllContacts() {
        List<Contact> list = new ArrayList<>();
        String sql = "SELECT c.id, c.firstName, c.lastName, c.groupId, g.name AS groupName, c.phoneNumber " +
                     "FROM `Contact` c LEFT JOIN `Group` g ON c.groupId = g.id ORDER BY c.id ASC";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                Contact c = new Contact();
                c.setId(rs.getInt("id"));
                c.setFirstName(rs.getString("firstName"));
                c.setLastName(rs.getString("lastName"));
                c.setGroupId(rs.getInt("groupId"));
                c.setGroupName(rs.getString("groupName"));
                c.setPhoneNumber(rs.getString("phoneNumber"));
                list.add(c);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return list;
    }

    public boolean addContact(Contact c) {
        String sql = "INSERT INTO `Contact` (firstName, lastName, groupId, phoneNumber) VALUES (?, ?, ?, ?)";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, c.getFirstName());
            ps.setString(2, c.getLastName());
            if (c.getGroupId() > 0) {
                ps.setInt(3, c.getGroupId());
            } else {
                ps.setNull(3, java.sql.Types.INTEGER);
            }
            ps.setString(4, c.getPhoneNumber());
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public Contact getContactById(int id) {
        String sql = "SELECT c.id, c.firstName, c.lastName, c.groupId, g.name AS groupName, c.phoneNumber " +
                     "FROM `Contact` c LEFT JOIN `Group` g ON c.groupId = g.id WHERE c.id = ?";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    Contact c = new Contact();
                    c.setId(rs.getInt("id"));
                    c.setFirstName(rs.getString("firstName"));
                    c.setLastName(rs.getString("lastName"));
                    c.setGroupId(rs.getInt("groupId"));
                    c.setGroupName(rs.getString("groupName"));
                    c.setPhoneNumber(rs.getString("phoneNumber"));
                    return c;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public boolean updateContact(Contact c) {
        String sql = "UPDATE `Contact` SET firstName = ?, lastName = ?, groupId = ?, phoneNumber = ? WHERE id = ?";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setString(1, c.getFirstName());
            ps.setString(2, c.getLastName());
            if (c.getGroupId() > 0) {
                ps.setInt(3, c.getGroupId());
            } else {
                ps.setNull(3, java.sql.Types.INTEGER);
            }
            ps.setString(4, c.getPhoneNumber());
            ps.setInt(5, c.getId());
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteContact(int id) {
        String sql = "DELETE FROM `Contact` WHERE id = ?";
        try (Connection conn = DBUtil.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {
            ps.setInt(1, id);
            return ps.executeUpdate() > 0;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
