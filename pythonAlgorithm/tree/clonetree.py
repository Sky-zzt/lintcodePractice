from tree.defTree import TreeNode


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    # 其实就是 二叉树的遍历
    def cloneTree(self, root):
        # Write your code here
        if root is None:
            return None
        clone_root = TreeNode(root.val)
        clone_root.left = self.cloneTree(root.left)
        clone_root.right = self.cloneTree(root.right)
        return clone_root
