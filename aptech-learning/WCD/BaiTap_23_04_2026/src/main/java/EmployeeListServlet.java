import java.io.IOException;
import java.util.ArrayList;

// Import thư viện chuẩn Jakarta cho Tomcat 10
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

@WebServlet("/employees")
public class EmployeeListServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        // Tạo danh sách
        ArrayList<Employee> employeeList = new ArrayList<>();
        
        // Thêm ít nhất 4 nhân viên (có người kinh nghiệm > 5 năm và < 5 năm)
        employeeList.add(new Employee(101, "Nguyễn Văn A", "IT", 1500.0, 6)); // Senior
        employeeList.add(new Employee(102, "Trần Thị B", "Kế toán", 1000.0, 3)); // Junior
        employeeList.add(new Employee(103, "Lê Văn C", "HR", 1200.0, 2)); // Junior
        employeeList.add(new Employee(104, "Phạm Thị D", "IT", 2500.0, 8)); // Senior
        
        // Đưa danh sách vào Request
        request.setAttribute("employeeList", employeeList);
        
        // Chuyển tiếp sang file JSP
        request.getRequestDispatcher("/employee-list.jsp").forward(request, response);
    }
}
