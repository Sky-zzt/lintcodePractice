class Solution:
    """
    @param root: the tree
    @param sum: the sum
    @return:  if the tree has a root-to-leaf path
    """

    def pathSum(self, root, sum):
        # Write your code here.
        if root == None:
            return False
        elif (root.val == sum and root.left == None and root.right == None):
            return True
        else:
            return self.pathSum(root.left, sum - root.val) or self.pathSum(root.right, sum - root.val)
