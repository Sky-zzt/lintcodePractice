import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers

    l用堆结构找中位数  有一个流 一直在吐数字  我想知道每时每刻的的中位数
准备一个大根堆和一个小根堆  第一个数先进大根堆，下一个数字在进去的时候，如果大于于大根堆的顶部 则进入小根堆
小于 大根堆的顶部 进入大根堆  若 大小堆里的数字数量差大于1，则把多的里面的树拿出来 放进少的里面；
具体 按如下规则放置；
大根堆 多了  把大根堆里的顶部放进小根堆，heapsize--，然后在heapfy ，
小堆heapfy heapsize++；
然后两个堆顶部就是中位数

    """

    # todo 核心在于这句话，你大堆 收集小的数，堆顶是小的里面的最大的，反之， 小堆 堆顶是大的里面最小的，那这俩堆顶不就是中位数吗

    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians

    @property
    def median(self):
        if len(self.minheap) > len(self.maxheap):  # todo   属于无奈之举，奇数的话mid在 minheap，偶数在maxheap ，但是 只有一个数，奇数，却在maxheap
            return self.minheap[0]
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) == 0:
            heapq.heappush(self.maxheap, -value)
            return
        if -self.maxheap[0] < value:
            heapq.heappush(self.minheap, value)
        else:
            heapq.heappush(self.maxheap, -value)
        self.modifyTwoHeapsSize()

    def modifyTwoHeapsSize(self):
        if len(self.maxheap) + 2 == len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))  # 此题 右诸多细节需要注意，从大堆拿和插入都要加负号
        if len(self.minheap) + 2 == len(self.maxheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))


s = Solution()
print(s.medianII([1, 0, 1]))
# todo push(e)改为push(-e)，pop(e)为-pop(e)，也就是说存入和取出的数都是相反数，其他逻辑和TopK相
