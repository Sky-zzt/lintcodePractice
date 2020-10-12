"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


        给定一个二叉树，找出所有路径中各节点相加总和等于给定 目标值 的路径。

一个有效的路径，指的是从根节点到叶节点的路径。

Example
样例1:

输入:
{1,2,4,2,3}
5
输出: [[1, 2, 2],[1, 4]]
说明:
这棵树如下图所示：
	     1
	    / \
	   2   4
	  / \
	 2   3
对于目标总和为5，很显然1 + 2 + 2 = 1 + 4 = 5
样例2:

输入:
{1,2,4,2,3}
3
输出: []
说明:
这棵树如下图所示：
	     1
	    / \
	   2   4
	  / \
	 2   3
注意到题目要求我们寻找从根节点到叶子节点的路径。
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5
这里没有合法的路径满足和等于3.
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum(self, root, target):
        # write your code here
        res = []
        self.helper(root, target, res, [], 0)
        return res

    # dfs 加回溯
    def helper(self, root, target, res, path, ans):
        if ans == target and root is None and root is None:  # 到达叶节点 已经和等于target时  将path 加入res
            if path not in res:
                res.append(list(path))
            return
        if root is not None:
            path.append(root.val)
            ans += root.val
            self.helper(root.left, target, res, path, ans)  # 左子树dfs
            ans -= root.val
            path.remove(path[-1])

        if root is not None:
            path.append(root.val)
            ans += root.val
            self.helper(root.right, target, res, path, ans)  # # 右子树dfs
            ans -= root.val
            path.remove(path[-1])
