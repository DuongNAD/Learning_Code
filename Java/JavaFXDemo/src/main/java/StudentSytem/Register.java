package StudentSytem;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.TextField;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import javafx.scene.control.Alert;
import javafx.stage.Stage;

public class Register {
    @FXML
    private TextField inputFullName;
    @FXML
    private TextField inputAccount;
    @FXML
    private TextField inputPassword;
    @FXML
    private TextField inputConfirmPassword;

    public void handleRegister(ActionEvent event) throws SQLException {
        String fullName = inputFullName.getText();
        String account = inputAccount.getText();
        String password = inputPassword.getText();
        String confirmPassword = inputConfirmPassword.getText();

        if(fullName.isEmpty() || account.isEmpty() || password.isEmpty() || confirmPassword.isEmpty()) {
            showAlert("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin!");
            return;
        }
        if(!password.equals(confirmPassword)) {
            showAlert("Lỗi", "Mật khẩu xác nhận không khớp");
            return;
        }

        String sql = "insert into admin(full_name,username,password) values (?, ?, ?)";

        try {
            Connection conn = DatabaseLoginConnection.getConnection();
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, fullName);
            stmt.setString(2, account);
            stmt.setString(3, password);

            int rows = stmt.executeUpdate();
            if(rows > 0) {
                showAlert("Thành công", "Đăng ký tài khoản thành công!");
            }

            stmt.close();
            conn.close();
        }
        catch(Exception e){
            e.printStackTrace();
            showAlert("Lỗi Database", "Không thể đăng ký: " + e.getMessage());
        }
    }

    public void backToLogin(ActionEvent event) throws SQLException {
        try{
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/StudentSytemManager/Login.fxml"));
            Parent root = loader.load();
            Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
            Scene scene = new Scene(root);
            stage.setTitle("Đăng nhập hệ thống");
            stage.setScene(scene);
            stage.show();
        }
        catch(Exception e){
            e.printStackTrace();
            showAlert("Lỗi", "Không thể quay lại màn hình đăng nhập: " + e.getMessage());
        }
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
