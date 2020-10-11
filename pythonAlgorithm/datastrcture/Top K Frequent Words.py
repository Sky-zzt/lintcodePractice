import heapq

from heapq import heappush, heappop
from collections import defaultdict
import collections


class Node(object):
    def __init__(self, int, str):
        self.freq = int
        self.word = str

    # 自定义less than comparator
    # freq不同的话正常比较
    # freq相同时，看word, 词典序小的排在前面
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        return self.word > other.word


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        if not words or k <= 0:
            return []

        map = collections.defaultdict(int)
        ans = []

        for word in words:
            map[word] += 1

            heap = []

        for word, freq in map.items():
            heapq.heappush(heap, Node(freq, word))

            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            ans.append(heapq.heappop(heap).word)
        ans.reverse()

        return ans


map = {4: 2, 2: 3}

map = sorted(map.items(), key=lambda kv: (kv[0], kv[1]))
print()
