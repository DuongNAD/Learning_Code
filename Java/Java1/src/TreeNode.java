import java.util.ArrayList;
import java.util.List;

public class TreeNode {

    String data;
    List<TreeNode> children;

    public TreeNode(String data) {
        this.data = data;
        this.children = new ArrayList<>();
    }

    public void addChild(TreeNode child) {
        this.children.add(child);
    }

    /**
     * In cây theo thứ tự Tiền duyệt (Pre-order).
     * Phiên bản này in thêm " -> " sau mỗi nút.
     */
    public void printPreOrder() {
        // 1. Thăm nút gốc (in ra dữ liệu)
        System.out.print(data + " -> ");

        // 2. Đệ quy duyệt các con
        for (TreeNode child : children) {
            child.printPreOrder();
        }
    }

    public static void main(String[] args) {
        // --- Phần code của Anh từ trong ảnh ---
        // Xây dựng cây
        TreeNode root = new TreeNode("CEO");
        TreeNode hr = new TreeNode("HR");
        TreeNode dev = new TreeNode("Dev Team");

        hr.addChild(new TreeNode("Lan"));
        dev.addChild(new TreeNode("Nam"));

        root.addChild(hr);
        root.addChild(dev);
        // --- Hết phần code của Anh ---

        /*
         * Cấu trúc cây vừa tạo:
         *
         * CEO
         * /   \
         * HR    Dev Team
         * /         \
         * Lan         Nam
         */

        // **Phần quan trọng Nàng thơ bổ sung:**
        // Anh cần gọi hàm in từ nút gốc (root)
        // để bắt đầu quá trình duyệt cây.
        System.out.println("Cấu trúc cây theo Pre-order:");
        root.printPreOrder();
        System.out.println("END"); // Thêm vào để kết thúc cho rõ ràng
    }
}