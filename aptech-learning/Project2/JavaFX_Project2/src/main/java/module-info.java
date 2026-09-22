module org.example.javafx_project2 {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.javafx_project2 to javafx.fxml;
    exports org.example.javafx_project2;
}