package End_DSA;

import java.util.ArrayList;
import java.util.List;

public class TreeNode {
    String data;
    double revenue;
    List<TreeNode> children;

    public TreeNode(String data, double revenue) {
        this.data = data;
        this.revenue = revenue;
        this.children = new ArrayList<>();
    }

    public void addChild(TreeNode child) {
        this.children.add(child);
    }
}
