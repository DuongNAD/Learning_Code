package StudentSytem;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.stage.Stage;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class Login {
    @FXML
    private TextField username;
    @FXML
    private PasswordField password;

    @FXML
    private Button toToRegister;
    @FXML
    private Button login;

    public void login(ActionEvent event) throws Exception{
        String username = this.username.getText();
        String password = this.password.getText();
        if(username.isEmpty() || password.isEmpty()){
            showAlert("Lỗi nhập liệu", "Vui lòng điền đầy đủ thông tin ");
            return;
        }
        String sql = "select * from admin where username=? and password=?";
        try{
            Connection conn = DatabaseLoginConnection.getConnection();
            PreparedStatement ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            ps.setString(2, password);
            ResultSet rs = ps.executeQuery();

            if(rs.next()){
                showAlert("Thông báo", "Đăng nhập thành công!");

                FXMLLoader loader = new FXMLLoader(getClass().getResource("/StudentSytemManager/StudentManager.fxml"));
                Parent root = loader.load();

                Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();

                Scene scene = new Scene(root);
                stage.setScene(scene);
                stage.setTitle("Student Manager");
                stage.centerOnScreen();
                stage.show();
            }
            else{
                showAlert("Lỗi đăng nhập","Sai tên đăng nhập hoặc mật khẩu");
            }
            rs.close();
            ps.close();
            conn.close();
        }
        catch(Exception e){
            e.printStackTrace();
            showAlert("Lỗi hệ thống","Không thể kết nối Database" + e.getMessage());
        }
    }

    public void goToRegister(ActionEvent event) throws Exception{
        try{
            FXMLLoader loader = new FXMLLoader(getClass().getResource("/StudentSytemManager/Register.fxml"));
            Parent root = loader.load();

            Stage stage = (Stage) ((Node)  event.getSource()).getScene().getWindow();

            Scene scene = new Scene(root);
            stage.setScene(scene);
            stage.setTitle("Đăng ký tài khoản");
            stage.show();
        }
        catch(Exception e){
            e.printStackTrace();
            showAlert("Lỗi","Không thể mở ma hình đăng ký" + e.getMessage());
        }
    }

    private void showAlert(String message, String title){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
