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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # write your code here
        res=[]
        if not root:return res
        if root.left == None and root.right == None:return res.append(root.val)
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)

        for i in left:
            res.append(root.val+"{}"+i.format("->"))
        for i in right:
            res.append(root.val + "{}" + i.format("->"))
        return res

    def binaryTreePaths1(self, root):
        # write your code here
        paths = []

        if root is None:
            return paths
        if root.left == None and root.right == None:# todo 注意 考虑一下一个节点的情况
            paths.append(str(root.val))

        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)

        for path in leftPaths:
            paths.append(str(root.val) + '->' + path)
        for path in rightPaths:
            paths.append(str(root.val) + '->' + path)

        return paths
s=Solution()
s.binaryTreePaths1(tree)
