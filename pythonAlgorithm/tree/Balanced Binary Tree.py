"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class ResultType:
    def __init__(self, IsBalanced,depth):
        self.depth = depth
        self.IsBalanced = IsBalanced


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    # todo 枚举每一个节点是否平衡
    def isBalanced(self, root):
        # write your code here
        if not root:return ResultType(True,0)
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)

        if not left.IsBalanced:return ResultType(False,-1)
        if not right.IsBalanced:return ResultType(False,-1)
        if abs(left.depth-right.depth)>1:return ResultType(False,-1)
        return ResultType(True,max(left.depth,right.depth)+1)