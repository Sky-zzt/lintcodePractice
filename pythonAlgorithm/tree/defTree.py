class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


tree = TreeNode(1)
tree1 = TreeNode(2)
tree2 = TreeNode(5)
tree3 = TreeNode(3)
tree4 = TreeNode(4)
tree5 = TreeNode(6)
# tree6=TreeNode(7)

tree.right = tree1
tree.left = tree2
tree1.right = tree4
tree1.left = tree3

tree2.right = tree5
# tree2.left=tree3
# tree2.right=tree4
