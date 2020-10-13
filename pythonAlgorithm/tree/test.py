class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []

        def recur(root, tar, sum, path):
            if not root: return
            path.append(root.val)
            sum += root.val
            if tar == sum and not root.left and not root.right:
                res.append(list(path))
                return
            recur(root.left, tar, sum, path)
            recur(root.right, tar, sum, path)
            path.pop()  # 回溯

        recur(root, sum, 0, [])
        return res
