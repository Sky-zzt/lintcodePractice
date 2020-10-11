"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from tree.defTree import tree

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):
        # write your code here
        self.helper(root)

    def helper(self, root):
        if not root:return None
        leftlast = self.helper(root.left)
        rightlast = self.helper(root.right)
        if leftlast is not  None:
            leftlast.right = root.right
            root.right = root.left
            root.left = None
        if leftlast is not None:  # todo  顺序反了  28 30 换一下
            return leftlast
        if rightlast is not None:
            return rightlast
        return root


s = Solution()
s.flatten(tree)
