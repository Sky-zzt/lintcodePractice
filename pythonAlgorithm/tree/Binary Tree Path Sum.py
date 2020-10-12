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
        result = []
        if not root:return result
        path=[root.val]
        self.helper(root, path, root.val, target, result)
        return result

    # dfs 加回溯
    def helper(self, root, path, sum, target, res):


        if sum == target and root.left is None and root.right is None:  # 到达叶节点 已经和等于target时  将path 加入res
            #if path not in res:
            res.append(list(path))
            return

        if root.left is not None:
            path.append(root.left.val)
            sum += root.left.val
            self.helper(root.left,  path, sum, target, res)
            sum -= root.left.val
            path.remove(path[-1])

        if root.right is not None:
            path.append(root.right.val)
            sum += root.right.val
            self.helper(root.right,  path, sum, target, res)
            sum -= root.right.val
            path.remove(path[-1])

    '''
    class Solution(object):
        def pathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: List[List[int]]
            """
            res, path = [], []
    
            def recur(root, tar,sum):
                if not root: return
                path.append(root.val)
                sum += root.val
                if tar == sum and not root.left and not root.right:
                    res.append(list(path))
                recur(root.left, tar,sum)
                recur(root.right, tar,sum)
                path.pop()
    
            recur(root, sum,0)
            return res
    '''

        '''
        
       fllowing works!
       
 public List<List<Integer>> binaryTreePathSum(TreeNode root, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        
        ArrayList<Integer> path = new ArrayList<Integer>();
        path.add(root.val);
        helper(root, path, root.val, target, result);
        return result;
    }
    
    private void helper(TreeNode root,
                        ArrayList<Integer> path,
                        int sum,
                        int target,
                        List<List<Integer>> result) {
                            
        // meet leaf
        if (root.left == null && root.right == null&&sum == target) {
                result.add(new ArrayList<Integer>(path));
            return;
        }
        
        // go left
        if (root.left != null) {
            path.add(root.left.val);
            sum=sum + root.left.val;
            helper(root.left, path, sum, target, result);
            path.remove(path.size() - 1);
            sum=sum - root.left.val;
        }
        
        // go right
        if (root.right != null) {
            path.add(root.right.val);
            sum=sum + root.right.val;
            helper(root.right, path, sum, target, result);
            path.remove(path.size() - 1);
            sum=sum - root.right.val;
        }
    }
        '''

