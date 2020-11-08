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
            path.pop()

        recur(root, sum, 0, [])
        return res

    # todo vital
    def helper(self, root, path, sum, target, res):

        if sum == target and root.left is None and root.right is None:  # 到达叶节点 已经和等于target时  将path 加入res
            # if path not in res:
            res.append(list(path))
            return

        if root.left is not None:
            path.append(root.left.val)
            sum += root.left.valt
            self.helper(root.left, path, sum, target,
                        res)  # todo 这种的为啥要显式的回溯呢，因为这个是先加的值传helper进去 在判断if sum==target，return 后还是已经加值得sum
            sum -= root.left.val  # todo 而上面那个recur是 先递归，然后递归进去在加值，在判断if sum==target,所以return的时候就自动回到了sum的上一个状态
            path.remove(path[-1])

        if root.right is not None:
            path.append(root.right.val)
            sum += root.right.val
            self.helper(root.right, path, sum, target, res)
            sum -= root.right.val
            path.remove(path[-1])


from tree.defTree import tree

s = Solution()
print(s.pathSum(tree, 6))

a=(12,2,)
b=(2,3)
a=a+b
print(a)