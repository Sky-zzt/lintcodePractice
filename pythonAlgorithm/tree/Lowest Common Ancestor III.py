"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    # todo why it is work
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        res=[]
        if not root or A==root or B==root:
            res.append(root)
            return res
        left = self.lowestCommonAncestor3(root.left, A, B)
        right = self.lowestCommonAncestor3(root.right, A, B)

        if left is not None and right is not None:
            res.append(root)
            return res
        if left is not None:
            res.extend(left)
            return res
        if right is not None:
            res.extend(right)
            return res
        return None   

from tree.defTree import tree,TreeNode
s=Solution()
l=s.lowestCommonAncestor3(tree,TreeNode(4),TreeNode(5))
for i in l:
    print(i.val)