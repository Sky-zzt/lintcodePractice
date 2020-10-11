import heapq


class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """

    def medianII(self, nums):
        self.minheap, self.maxheap = [], []
        medians = []
        for num in nums:
            self.add(num)
            medians.append(self.median)
        return medians

    @property
    def median(self):
        return -self.maxheap[0]

    def add(self, value):
        if len(self.maxheap) <= len(self.minheap):
            heapq.heappush(self.maxheap, -value)
        else:
            heapq.heappush(self.minheap, value)

        if len(self.minheap) == 0 or len(self.maxheap) == 0:
            return

        if -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))


# todo push(e)改为push(-e)，pop(e)为-pop(e)，也就是说存入和取出的数都是相反数，其他逻辑和TopK相
a = []
for i in range(10):
    # print(i)
    heapq.heappush(a, -i)
print(-heapq.heappop(a))
