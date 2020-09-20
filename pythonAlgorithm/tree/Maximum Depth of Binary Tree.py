"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxDepth(self, root):
        # write your code here
        if not root: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(right, left) + 1


class Solution2:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    depth = 0

    def maxDepth(self, root):
        # write your code here
        self.helper(root, 1)
        return self.depth

    def helper(self, root, curdepth):
        if not root: return
        if curdepth > self.depth:
            self.depth = curdepth
        self.helper(root.left, curdepth + 1)
        self.helper(root.right, curdepth + 1)
