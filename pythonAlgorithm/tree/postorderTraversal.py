"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from tree.defTree import TreeNode


class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        result = []
        if not root:
            return result
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        #   result.append(root.val)  preorder
        result.extend(left)
        result.extend(right)
        result.append(root.val)  # postorder
        return result

    def traverse(self, root, res=None):
        if not root: return
        res.append(root.val)
        self.traverse(root.left, res)
        self.traverse(root.right, res)

