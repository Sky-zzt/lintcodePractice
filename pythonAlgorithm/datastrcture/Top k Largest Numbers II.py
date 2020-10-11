import heapq

'''
实现一个数据结构，提供下面两个接口
1.add(number) 添加一个元素
2.topk() 返回前K大的数
    前K大 不是第K大
    用minheap 而不是maxheap。
    维持一个大小为K的minheap ，然后来一个数和最小值比较，比最小值大就弹出最先值加入新来的， 这个heap就是topk
    
    那么maxheap为啥不行呢，首先如果是maxheap肯定不能维持一个大小为k的heap，加入这个maxheap是5，3，1，，K==3，那么新来的数如果是100
    我没法弹出
    [1，3，5，100，4，5，12]
'''
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