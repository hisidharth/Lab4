public class invertTree {


    public TreeNode invertTree(TreeNode root) {

        if(root == null){

            return root;
        }

        TreeNode temp1 = invertTree(root.right);
        TreeNode temp2 = invertTree(root.left);

        root.right = temp2;
        root.left = temp1;
        return root;
    }

    static void printTree(TreeNode node)
    {
        if(node == null) return;

        System.out.println(node.val + " ");
        printTree(node.left);
        printTree(node.right);
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(2);
        root.right = new TreeNode(10);
        root.right.right = new TreeNode(10);

        invertTree test = new invertTree();

        invertTree.printTree(root);

        System.out.println("");

        test.invertTree(root);

        invertTree.printTree(root);

    }


}