import heapq


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
    """

    #  todo  用java的treeset 自带排序 remove还是log的

    def kthSmallest(self, nums, k):
        # write your code here
        self.minheap, self.maxheap = [], []
        medians = []
        for i in range(len(nums)):
            self.add(nums[i], i, k)
            medians.append(self.median)
        return medians

    @property
    def median(self):
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        return -self.maxheap[0]

    def add(self, value, index, winsize):
        if len(self.maxheap) + len(self.minheap) > winsize:  # todo
            self.remove(index - winsize)
        if len(self.maxheap) == 0:
            heapq.heappush(self.maxheap, -value)
            return
        if -self.maxheap[0] < value:
            heapq.heappush(self.minheap, value)
        else:
            heapq.heappush(self.maxheap, -value)
        self.modifyTwoHeapsSize()

    def remove(self, idx):
        if idx in self.minheap:
            self.minheap.remove(idx)
        else:
            self.maxheap.remove(idx)

    def modifyTwoHeapsSize(self):
        if len(self.maxheap) + 2 == len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        if len(self.minheap) + 2 == len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
