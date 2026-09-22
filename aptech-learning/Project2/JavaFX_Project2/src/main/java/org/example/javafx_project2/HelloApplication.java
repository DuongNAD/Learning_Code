package org.example.javafx_project2;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("register.fxml"));

        Scene scene = new Scene(fxmlLoader.load(), 800, 500);

        stage.setTitle("Đăng Ký Tài Khoản");
        stage.setScene(scene);
        stage.show();
    }
}
