class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。
Example
例1:

输入:
[[3,4]]
target=3
输出:1
例2:

输入:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
输出:2
Challenge
要求O(m+n) 时间复杂度和O(1) 额外空间
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or len(matrix) == 0: return 0
        if not matrix[0] or len(matrix) == 0: return 0

        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m - 1
        count = 0
        x = 0
        y = n - 1
        while x < m and 0 <= y:
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            elif target == matrix[x][y]:
                count += 1
                x += 1
                y -= 1
        return count
