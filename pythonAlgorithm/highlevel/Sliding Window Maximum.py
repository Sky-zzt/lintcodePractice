import collections


class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.

    双端队列  deque
    【                   】
    头  大--> 小不能相等   尾
   加数 如果尾部比新来的小弹出，保持从大到小的结构
    减数  就是L 右边移动，deque的 头部弹出扔掉
    头部的第一个位置就是当前窗口的最大值
    """

    def maxSlidingWindow(self, nums, k):
        # write your code here
        # write your code here
        # 答案数组
        ans = []
        # 单调队列
        qmax = collections.deque()
        # 队列里元素数量
        cnt = 0
        n = len(nums)
        for i in range(n):
            # 维护单调性
            while cnt != 0 and nums[i] > nums[qmax[-1]]:
                qmax.pop()
                cnt -= 1
            # 滑动窗口的长度超过了k 删掉超过的部分
            if cnt != 0 and i - qmax[0] >= k:
                qmax.popleft()
                cnt -= 1
            qmax.append(i)
            cnt += 1
            if i >= k - 1:
                ans.append(nums[qmax[0]])
            # print(qmax)
        return ans

    def maxSlideWin(self, nums, k):
        ans = []
        qmax = collections.deque()
        cnt = 0
        n = len(nums)
        for i in range(n):
            # if qmax.pop()
            qmax.append(nums[i])
