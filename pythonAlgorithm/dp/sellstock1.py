class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        l=len(prices)
        if l==0: return 0
        maxprofit=0
        for i in range(l):
            for j in range(i):
                maxprofit=max(maxprofit,prices[i]-prices[j])
        return maxprofit

s=Solution()
print(s.maxProfit([10000] * 100))