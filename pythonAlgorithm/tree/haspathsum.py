class Solution:
    def hasPathSum(self, root, sum):
        if not root: return False
        if root.left is None and root.right is None and sum == root.val: return True
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return left or right

    def dfs(self, root, target, sum):

        if not root: return
        if root.left is None and root.right is None and sum == target: return True
        sum += root.val  # todo 写这里需要回溯。|  这么写要提前把 root.val加入到sum中（参考Balanced Binary Tree的java 写法），不加的话有问题，画个图模拟一下就知道了
        # todo 为了避免提前把root提前加入到 sum  可以把sum += root.val 写到 12 行的 return 前 ，但是这种写 就不需要 回溯了（参考pathsum2）
        self.dfs(root.left, target, sum)
        sum -= root.val

        sum += root.val
        self.dfs(root.right, target, sum)
        sum -= root.val
