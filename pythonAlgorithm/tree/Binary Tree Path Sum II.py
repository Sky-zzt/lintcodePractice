"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

        给一棵二叉树和一个目标值，设计一个算法找到二叉树上的和为该目标值的所有路径。路径可以从任何节点出发和结束，但是需要是一条一直往下走的路线。也就是说，路径上的节点的层级是逐个递增的。

Have you met this question in a real interview?
Example
样例1：

输入:
{1,2,3,4,#,2}
6
输出:
[[2, 4],[1, 3, 2]]
解释:
这棵二叉树如图所示：
    1
   / \
  2   3
 /   /
4   2
对于给定目标值6, 很显然有 2 + 4 = 6 和 1 + 3 + 2 = 6 两条路径。
样例2：

输入:
{1,2,3,4}
10
输出:
[]
解释:
这棵二叉树如图所示：
    1
   / \
  2   3
 /
4
对于给定目标值10, 没有符合条件的答案。
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        # write your code here
        pass
