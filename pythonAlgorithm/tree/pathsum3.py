class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        result = []
        if not root: return result
        path = [root.val]
        self.helper(root, path, root.val, target, result)
        return result

    # dfs 加回溯
    def helper(self, root, path, sum, target, res):
        if not root: return
        if sum == target and root.left is None and root.right is None:  # 到达叶节点 已经和等于target时  将path 加入res
            # if path not in res:
            res.append(list(path))
            return

        # if root.left is not None:          # todo 如果把 if 写上面，  root.left.val 会空指针，如果只是root.left是可以的，把if 写上面 ，    下面的hasPathSum 之所以可以都写上面是因为只是一个root.left，所以 可以写上面 而不用对两个递归分别判空
        path.append(root.left.val)
        sum += root.left.val
        self.helper(root.left, path, sum, target, res)
        sum -= root.left.val
        path.remove(path[-1])

        # if root.right is not None:
        path.append(root.right.val)
        sum += root.right.val
        self.helper(root.right, path, sum, target, res)
        sum -= root.right.val
        path.remove(path[-1])


s = Solution()
from tree.defTree import tree

print(s.binaryTreePathSum(tree, 6))


class Solution:
    def hasPathSum(self, root, sum):
        if not root: return False
        if root.left is None and root.right is None and sum == root.val: return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right
