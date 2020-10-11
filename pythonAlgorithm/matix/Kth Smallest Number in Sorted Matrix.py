class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    在一个排序矩阵中找从小到大的第 k 个整数。
排序矩阵的定义为：每一行递增，每一列也递增。
    Example
    样例 1:

    输入:
    [
      [1 ,5 ,7],
      [3 ,7 ,8],
      [4 ,8 ,9],
    ]
    k = 4
    输出: 5
    样例 2:

    输入:
    [
      [1, 2],
      [3, 4]
    ]
    k = 3
    输出: 3
    Challenge
    时间复杂度 O(klogn), n 是矩阵的宽度和高度的最大值

    用堆解决:

定义一个小根堆, 起始仅仅放入第一行第一列的元素.

循环 k次, 每一次取出一个元素, 然后把该元素右方以及下方的元素放入堆中, 第 k次取出的元素即为答案.

其中, 要注意一个元素不能重复入堆, 需要记录.hashset
    """

    def kthSmallest(self, matrix, k):
        # write your code here
        pass
