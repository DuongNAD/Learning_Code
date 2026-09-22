package org.example.javafx_project2;

import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.image.PixelReader;
import javafx.scene.image.WritableImage;
import javafx.scene.input.MouseEvent;
import javafx.scene.paint.ImagePattern;
import javafx.scene.shape.Circle;
import javafx.stage.FileChooser;

import java.io.File;
import java.net.URL;
import java.util.ResourceBundle;

public class RegisterController implements Initializable {
    @FXML
    private Label appNameLabel;

    @FXML
    private Label emailLabel;
    @FXML
    private Label phoneLabel;

    @FXML
    private TextField fullNameTextField;
    @FXML
    private TextField userNameTextField;
    @FXML
    private TextField emailTextField;
    @FXML
    private TextField phoneTextField;
    @FXML
    private PasswordField passwordField;
    @FXML
    private PasswordField confirmPasswordField;
    @FXML
    private Button registerButton;
    @FXML
    private Button backToLoginButton;

    @FXML
    private Circle avatarCircle;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        fullNameTextField.textProperty().addListener((observable, oldValue, newValue) -> {
            if (newValue.trim().isEmpty()) {
                appNameLabel.setText("Nguyễn Văn A");
            }
            else {
                appNameLabel.setText(newValue.trim());
            }
        });

        try{
            Image image = new Image(getClass().getResourceAsStream("avatar.png"));
            if(!image.isError()){
                setAvatarImage(image);
            }
        }
        catch (Exception e){
            System.err.println("Không tìm thấy ảnh avatar mặc định: " + e.getMessage());
        }
    }

    private void setAvatarImage(Image image) {
        double w = image.getWidth();
        double h = image.getHeight();

        double size = Math.min(w, h);
        int x = (int) ((w - size) / 2);
        int y = (int) ((h - size) / 2);
        PixelReader reader = image.getPixelReader();
        WritableImage croppedImage = new WritableImage(reader, x, y, (int) size, (int) size);
        avatarCircle.setFill(new ImagePattern(croppedImage));
    }


    public void initialize() {
        Image img = new Image(getClass().getResourceAsStream("avatar.jpg"));
        avatarCircle.setFill(new ImagePattern(img));

    }

    @FXML
    public void handleAvatarClick(MouseEvent event) {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Chọn ảnh đại diện");
        fileChooser.getExtensionFilters().add(
                new FileChooser.ExtensionFilter("Image Files",  "*.png", "*.jpg", "*.gif", "*.bmp")
        );
        File selectedFile = fileChooser.showOpenDialog(avatarCircle.getScene().getWindow());
        if (selectedFile != null) {
            Image newImage = new Image(selectedFile.toURI().toString());
            setAvatarImage(newImage);
        }

    }

    @FXML
    public void onRegisterButtonClick() {
        String username = userNameTextField.getText();
        String email = emailTextField.getText();
        String phone = phoneTextField.getText();
        String password = passwordField.getText();
        String confirmPassword = confirmPasswordField.getText();
        if(username.isEmpty() || email.isEmpty() || phone.isEmpty() || password.isEmpty() || confirmPassword.isEmpty()) {
            showAlert(Alert.AlertType.ERROR,"Lỗi nhập liệu","Vui lòng điền đầy đủ thông tin!");
            return;
        }

        if(!isValidEmail(email)) {
            showAlert(Alert.AlertType.ERROR,"Lỗi Email","Email không đúng định dạng (VD: abc@gmail.com)!");
            return;
        }

        if (!isValidPassword(password)) {
            showAlert(Alert.AlertType.ERROR,"Lỗi mật khẩu","Mật khẩu");
        }

        if(password.equals(confirmPassword)) {
            System.out.println("Đăng ký thành công: " + username);
            showAlert(Alert.AlertType.INFORMATION,"Thành công", "Đăng ký tài khoản thành công!");
            clearFields();
        }
        else {
            showAlert(Alert.AlertType.ERROR, "Sai mật khẩu", "Mật khẩu nhập lại không khớp!");
            confirmPasswordField.clear();
        }
    }

    private void showAlert(Alert.AlertType alertType, String title, String message) {
        Alert alert = new Alert(alertType);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    private void clearFields() {
        userNameTextField.clear();
        emailTextField.clear();
        phoneTextField.clear();
        passwordField.clear();
        confirmPasswordField.clear();
        fullNameTextField.clear();
    }

    private boolean isValidEmail(String email) {
        String emailRegax = "^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$";
        return email.matches(emailRegax);
    }

    private boolean isValidPassword(String password) {
        String passwordRegex = "^(?=.*[A-Za-z])(?=.*\\d).{8,}$";
        return password.matches(passwordRegex) && password.length() >= 6;
    }
}
