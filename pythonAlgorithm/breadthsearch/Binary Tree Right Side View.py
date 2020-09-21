"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    def rightSideView(self, root):
        if not root: return []
        from collections import deque
        q = deque()
        res = []
        q.append(root)
        while q:
            size = len(q)
            partres = []
            for i in range(size):
                ele = q.popleft()
                if i ==size-1:res.append(ele.val)   # 直接res append
                if ele.left is not None:
                    q.append(ele.left)
                if ele.right is not None:
                    q.append(ele.right)
                #res.append(partres)
        return res


from collections import deque

q = deque()

q.append(1)

print(q.pop(0))
