'''
给定二叉搜索树(BST)，将其转换为更大的树，使原始BST上每个节点的值都更改为在原始树中大于等于该节点值的节点值之和(包括该节点)。

样例
样例1:

输入 : {5,2,13}
              5
            /   \
           2     13
输出 : {18,20,13}
             18
            /   \
          20     13
样例2:

输入 : {5,3,15}
              5
            /   \
           3     15
输出 : {20,23,15}
             20
            /   \
          23     15


解题思路
这题考查的是二叉树的中序遍历，由于要将节点累加上大于等于它的所有值，所以要优先遍历右子树，得到所有大于等于当前值的和。然后更新当前节点的值，再搜索左子树的值。对于总和值sum，我们可以传一个值的引用来实现。

代码思路
令sum值等于0。
遍历二叉树，如果为空则返回。
优先遍历值较大的右子树。
更新当前节点的值。
再遍历值小于当前节点的左子树。
C++中可以用引用来维护计算过程中的now_sum值。

Java和Python中可以用回调的形式维护计算过程中的now_sum值

复杂度分析
设二叉树的节点数为N。

时间复杂度
遍历一次二叉树的时间复杂度为O(N)。
空间复杂度
遍历的空间复杂度取决于二叉树的最大深度，空间复杂度为O(N)。
'''


class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """

    def convertBST(self, root):
        self.travel(root, 0)
        return root

    """
    @param root: the node that is traveled
    @param sum: the reference of the sum value from largest to smallest
    """

    def travel(self, root, now_sum):
        # 递归出口
        if root is None:
            return now_sum

        # 先遍历右子树
        now_sum = self.travel(root.right, now_sum)

        # 先加上大于等于这个数的和，并令sum加上这个数
        now_sum += root.val
        root.val = now_sum

        # 再遍历左子树
        now_sum = self.travel(root.left, now_sum)

        return now_sum
