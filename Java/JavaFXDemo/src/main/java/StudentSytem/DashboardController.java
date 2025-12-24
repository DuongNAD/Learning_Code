package StudentSytem;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.control.*;
import javafx.stage.Stage;

import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DashboardController {
    @FXML
    private TextField inputName;
    @FXML
    private TextField inputAge;
    @FXML
    private TextField inputMajor;
    @FXML
    private Button btnAdd;
    @FXML
    private Button btnUpdate;
    @FXML
    private Button btnDelete;
    @FXML
    private Button btnClear;
    @FXML
    private Button btnLogout;
    @FXML
    private Label welcomeLabel;

    @FXML
    private TableView<Student> tableStudents;
    @FXML
    private TableColumn<Student, Integer> colId;
    @FXML
    private TableColumn<Student, String> colName;
    @FXML
    private TableColumn<Student, Integer> colAge;
    @FXML
    private TableColumn<Student, String> colMajor;

    private javafx.collections.ObservableList<Student> studentList = javafx.collections.FXCollections.observableArrayList();

    private void showSimpleMessage(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    @FXML
    public void handleLogout(ActionEvent event) throws IOException {
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Đăng xuất");
        alert.setHeaderText("Đăng xuất khỏi hệ thống");
        alert.setContentText("Bạn có chắc chắn muốn thoát không?");

        alert.showAndWait().ifPresent(response -> {
            if (response == ButtonType.OK) {
                try{
                    FXMLLoader Loader = new FXMLLoader(getClass().getResource("/StudentSytemManager/Login.fxml"));
                    Parent root = Loader.load();
                    Stage currentStage = (Stage) btnLogout.getScene().getWindow();
                    currentStage.setScene(new javafx.scene.Scene(root));
                    currentStage.setTitle("Đăng nhập hệ thống");
                    currentStage.centerOnScreen();
                    currentStage.show();

                    System.out.println("Đang quay lại màn hình Login...");
                }
                catch (Exception e){
                    e.printStackTrace();
                    showAlert("Lỗi", "Không thể quay lại màn hình đăng nhập: " + e.getMessage());
                }
            }
        });
    }

    @FXML
    public void initialize() {
        colId.setCellValueFactory(new javafx.scene.control.cell.PropertyValueFactory<>("id"));
        colName.setCellValueFactory(new javafx.scene.control.cell.PropertyValueFactory<>("name"));
        colAge.setCellValueFactory(new javafx.scene.control.cell.PropertyValueFactory<>("age"));
        colMajor.setCellValueFactory(new javafx.scene.control.cell.PropertyValueFactory<>("major"));

        tableStudents.setItems(studentList);

        loadData();
    }

    public void setDisplayName(String user) {
        welcomeLabel.setText("Xin chào, " + user);
    }

    private void loadData() {
        studentList.clear();
        String sql = "SELECT * FROM student";

        try (Connection conn = DatabaseStudentConnection.getConnection();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             java.sql.ResultSet rs = pstmt.executeQuery()) {

            while (rs.next()) {
                studentList.add(new Student(
                        rs.getInt("id"),
                        rs.getString("name"),
                        rs.getInt("age"),
                        rs.getString("major")
                ));
            }
        } catch (Exception e) {
            showAlert("Lỗi tải dữ liệu", "Không thể hiển thị sinh viên: " + e.getMessage());
        }
    }

    public void addStudent(ActionEvent event) throws Exception {
        String name = inputName.getText();
        String ageRaw = inputAge.getText();
        String major = inputMajor.getText();

        if(name.isEmpty() || major.isEmpty() || ageRaw.isEmpty()){
            showAlert("Lỗi", "Vui lòng nhập đầy đủ thông tin!");
            return;
        }
        try{
            int age = Integer.parseInt(ageRaw);
            Connection conn  = DatabaseStudentConnection.getConnection();
            String sql = "insert into student(name,age,major) values(?,?,?)";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setString(3, major);
            pstmt.executeUpdate();
            showAlert("Thông báo","Đã thêm học sinh thành công");
            loadData();
            clearStudent(event);
        }
        catch(Exception e){
            showAlert("Lỗi", "Không thể thêm học sinh: " + e.getMessage());
        }
    }

    public void deleteStudent(ActionEvent event) throws Exception {

        Student selected = tableStudents.getSelectionModel().getSelectedItem();

        if(selected == null){
            showAlert("Lỗi","Vui lòng chọn 1 sinh viên trong bảng để xóa");
            return;
        }

        try{
            Connection conn  = DatabaseStudentConnection.getConnection();
            String sql = "delete from student where id = ?";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, selected.getId());
            int rowsAffected = pstmt.executeUpdate();

            if(rowsAffected > 0){
                tableStudents.getItems().remove(selected);
                showAlert("Thông báo","Đã xóa thành công sinh viên: " + selected.getName() );
            }
        }
        catch (Exception e){
            showAlert("Lỗi","Không thể xóa: "+e.getMessage());
        }
    }

    public void updateStudent(ActionEvent event) throws Exception {
        String name = inputName.getText();
        String ageRaw = inputAge.getText();
        String major = inputMajor.getText();

        if(name.isEmpty() || major.isEmpty() || ageRaw.isEmpty()){
            showAlert("Lỗi", "Vui lòng nhập đầy đủ thông tin!");
            return;
        }

        Student selected = tableStudents.getSelectionModel().getSelectedItem();

        if(selected == null){
            showAlert("Lỗi","Vui lòng chọn 1 sinh viên trong bảng để xóa");
            return;
        }
        try{
            Connection conn  = DatabaseStudentConnection.getConnection();
            int age = Integer.parseInt(ageRaw);

            String sql = "UPDATE student SET name = ?, age = ?, major = ? WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, name);
            pstmt.setInt(2, age);
            pstmt.setString(3, major);
            pstmt.setInt(4, selected.getId());

            int rowsAffected = pstmt.executeUpdate();

            if(rowsAffected > 0){
                selected.setName(name);
                selected.setAge(age);
                selected.setMajor(major);
                tableStudents.refresh();
                showAlert("Thông báo","Đã cập nhật thành công sinh viên: " + selected.getName() + " - " + selected.getAge() + " - " + selected.getMajor() );
            }
        }
        catch (NumberFormatException e){
            showAlert("Lỗi", "Tuổi phải là một con số");
        }

        catch (Exception e){
            showAlert("Lỗi","Không thể xóa: "+e.getMessage());
        }
    }

    public void clearStudent(ActionEvent event){
        inputName.setText("");
        inputAge.setText("");
        inputMajor.setText("");

        tableStudents.getSelectionModel().clearSelection();

        inputName.requestFocus();
    }

    private void showAlert(String title, String message){
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

}
