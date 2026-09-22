import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/categories")
public class CategoryServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        
        // 1. Khởi tạo một List<String> chứa 4 tên danh mục bất kỳ
        List<String> categories = Arrays.asList("Laptop", "Điện thoại", "Phụ kiện", "Đồng hồ thông minh");
        
        // 2. Ném List này vào Request với tên là "categoryList"
        request.setAttribute("categoryList", categories);
        
        // 3. Forward sang file JSP có tên là categories.jsp
        request.getRequestDispatcher("/categories.jsp").forward(request, response);
    }
}
