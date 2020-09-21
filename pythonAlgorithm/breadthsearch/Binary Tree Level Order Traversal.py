"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        # write your code here
        if not root: return []
        from collections import deque
        q = deque()
        res = []
        q.append(root)
        while q :
            size = len(q)
            partres = []
            for i in range(size):
                ele = q.popleft()
                partres.append(ele.val)
                if ele.left is not None:
                    q.append(ele.left)
                if ele.right is not None:
                    q.append(ele.right)
            res.append(partres)
        return res