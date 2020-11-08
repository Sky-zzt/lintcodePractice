import collections


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.

    双端队列  deque
    【                   】
    头  大-->小  不能相等   尾
   加数 如果尾部比新来的小弹出，保持从大到小的结构
    减数  就是L 右边移动，deque的 头部弹出扔掉
    头部的第一个位置就是当前窗口的最大值
    """
        # three ways   one is double for ,another is a way to keep a k step win  using two pointer i and j ,then use treemap to get max  treemao(num[i],i)
    def maxSlidingWindow(self, nums, k):
        # write your code here
        # 答案数组
        ans = []
        # 单调队列
        qmax = collections.deque()
        # 队列里元素数量
        n = len(nums)
        for i in range(n):
            # 维护单调性
            while len(qmax) != 0 and nums[i] > nums[qmax[-1]]:  # TODO python 的 peek 用-1 和0 实现了 呵呵
                qmax.pop()
            qmax.append(i)
            # 滑动窗口的长度超过了k 删掉超过的部分
            if i - qmax[0] >= k:  # todo 这里已经在维护一个 窗口为k的队列 ，所以，下面i>k-1后就可以无脑 取队列的第一个了
                qmax.popleft()

            if i >= k - 1:
                ans.append(nums[qmax[0]])
        return ans

# todo queue 不能用len（），自带qsize，不能while q，deque可以用len（）
