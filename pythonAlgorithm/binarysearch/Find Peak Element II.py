'''
给定一个整数矩阵 A, 它有如下特性:

相邻的整数不同
矩阵有 n 行 m 列。
对于所有的 i < n, 都有 A[i][0] < A[i][1] && A[i][m - 2] > A[i][m - 1]
对于所有的 j < m, 都有 A[0][j] < A[1][j] && A[n - 2][j] > A[n - 1][j]
我们定义一个位置 [i,j] 是峰值, 当且仅当它满足:

  A[i][j] > A[i + 1][j] && A[i][j] > A[i - 1][j] &&
  A[i][j] > A[i][j + 1] && A[i][j] > A[i][j - 1]
找到该矩阵的一个峰值元素, 返回它的坐标.

保证至少存在一个峰值, 而如果存在多个峰值, 返回任意一个即可.
样例
样例 1:

输入:
    [
      [1, 2, 3, 6,  5],
      [16,41,23,22, 6],
      [15,17,24,21, 7],
      [14,18,19,20,10],
      [13,14,11,10, 9]
    ]
输出: [1,1]
解释: [2,2] 也是可以的. [1,1] 的元素是 41, 大于它四周的每一个元素 (2, 16, 23, 17).
样例 2:

输入:
    [
      [1, 5, 3],
      [4,10, 9],
      [2, 8, 7]
    ]
输出: [1,1]
解释: 只有这一个峰值
挑战
O(n+m) 的时间复杂度.
'''
