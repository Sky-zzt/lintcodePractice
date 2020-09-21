"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    import sys
    subsum = sys.maxsize
    subtree = None

    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.subtree

    def helper(self, root):
        if not root: return 0
        sum = self.helper(root.left) + self.helper(root.right) + root.val
        if sum < self.subsum:
            self.subsum = sum
            self.subtree = root
        return sum


class Solution3:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    import sys
    subsum = sys.maxsize
    subtree = None

    def findSubtree(self, root):
        # write your code here
        sum=0
        tree=None
        self.helper(root,sum,tree)
        return self.subtree

    def helper(self, root, sum, tree):
        if not root: return 0
        self.helper(root.left,sum,tree ) + self.helper(root.right,sum,tree) + root.val
        if sum < self.subsum:
            self.subsum = sum
            self.subtree = root



# todo a Very excellent way
import sys
from tree.defTree import tree


class Solution2:

    def findSubtree(self, root):
        minimum, subtree, sum_of_root = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)

        sum_of_root = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum_of_root):
            return left_minimum, left_subtree, sum_of_root
        if right_minimum == min(left_minimum, right_minimum, sum_of_root):
            return right_minimum, right_subtree, sum_of_root

        return sum_of_root, root, sum_of_root


s = Solution()
s.findSubtree(tree)
