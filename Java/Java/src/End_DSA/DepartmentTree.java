package End_DSA;

import java.util.LinkedList;

public class DepartmentTree {
    private TreeNode root;

    public TreeNode getRoot() {
        return root;
    }

    public void buildOrganizationTree() {
        root = new TreeNode("CEO: Ông A", 0);

        TreeNode director = new TreeNode("Giám đốc: Bà B", 50000);
        root.addChild(director);

        TreeNode headCardiology = new TreeNode("Trưởng khoa Tim Mạch", 20000);
        TreeNode headNeurology = new TreeNode("Trưởng khoa Thần Kinh", 30000);
        director.addChild(headCardiology);
        director.addChild(headNeurology);

        headCardiology.addChild(new TreeNode("Bác sĩ 1", 10000));
        headCardiology.addChild(new TreeNode("Bác sĩ 2", 12000));
        headNeurology.addChild(new TreeNode("Bác sĩ 3", 15000));

        System.out.println("Cây tổ chức đã được xây dựng.");
    }

    public void printPreOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        System.out.print(node.data + " -> ");

        for (TreeNode child : node.children) {
            printPreOrder(child);
        }
    }

    public void printPostOrder(TreeNode node) {
        if (node == null) {
            return;
        }

        for (TreeNode child : node.children) {
            printPostOrder(child);
        }

        System.out.print(node.data + " -> ");
    }

    public void printLevelOrder() {
        if (root == null) {
            System.out.println("Cây rỗng.");
            return;
        }

        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.removeFirst();
            System.out.print(node.data + " -> ");

            for (TreeNode child : node.children) {
                queue.add(child);
            }
        }
    }

    public double calculateTotalRevenue(TreeNode node) {
        if (node == null) {
            return 0;
        }

        double total = node.revenue;

        for (TreeNode child : node.children) {
            total = total + calculateTotalRevenue(child);
        }

        return total;
    }
}