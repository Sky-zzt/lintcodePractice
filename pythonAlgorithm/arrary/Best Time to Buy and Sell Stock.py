class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        import sys
        # [3, 2, 3, 1, 2]
        globalMax, sum, minSum = -sys.maxsize, prices[0], prices[0]
        for i in range(len(prices)):
            globalMax = max(globalMax, prices[i] - minSum)
            minSum = min(prices[i], minSum)
        return globalMax


s = Solution()
print(s.maxProfit([3, 2, 3, 1, 2]))
