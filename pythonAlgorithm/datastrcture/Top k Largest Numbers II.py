import heapq


class Solution:

    # @param {int} k an integer
    def __init__(self, k):
        self.k = k
        self.heap = []

    # @param {int} num an integer
    def add(self, num):
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        return sorted(self.heap, reverse=True)