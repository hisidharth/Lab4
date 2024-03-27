class TreeNode(object):

     def __init__(self, val=0, left=None, right=None):

         self.val = val

         self.left = left

         self.right = right

class InvertTree:
    def invertTree(self, root):
        if root is None:
            return root
        temp1 = self.invertTree(root.right)
        temp2 = self.invertTree(root.left)
        root.right = temp2
        root.left = temp1
        return root

    @staticmethod
    def printTree(node):
        if node is None:
            return
        print(node.val, " ")
        InvertTree.printTree(node.left)
        InvertTree.printTree(node.right)

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(10)
    root.right.right = TreeNode(10)

    invert_tree_instance = InvertTree()

    InvertTree.printTree(root)

    print("\n")

    invert_tree_instance.invertTree(root)
    InvertTree.printTree(root)
