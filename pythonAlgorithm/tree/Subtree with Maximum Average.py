"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class ResultType:
    def __init__(self, size, sum):
        self.size = size
        self.sum = sum


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    import sys
    maxavg = -sys.maxsize
    maxtree = None

    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.maxtree
    def helper(self,root):
        if not root:return ResultType(0,0)
        left = self.helper(root.left)
        right = self.helper(root.right)
        avg = (left.sum + right.sum + root.val) / (left.size + right.size + 1)
        if avg > self.maxavg:
            self.maxavg = avg
            self.maxtree = root
        return ResultType(left.size + right.size + 1, left.sum + right.sum + root.val)

from tree.defTree import tree

s=Solution()
s.findSubtree2(tree)
print(s.maxavg)