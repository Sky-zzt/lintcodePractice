"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1
