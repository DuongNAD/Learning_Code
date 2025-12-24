module org.example.javafxdemo {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.desktop;
    requires java.sql;
    requires javafx.graphics;


    opens org.example.javafxdemo to javafx.fxml;
    exports org.example.javafxdemo;

    exports StudentSytem;
    opens StudentSytem to javafx.fxml;
}