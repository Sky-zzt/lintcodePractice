class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, A):
        # write your code here
        return self.calc(A)


    def calc(self,A):
        if A is None or not A:return 0
        size=(len(A))
        f=[1]*size
        for i in range(size):
            # 为啥要加个for 循环取最大值呢，和转移方程以及，上一道题（longestIncreasingContinuousSubsequence没有第二个循环）不太一样，
            # 因为山道题是连续的，只需要考虑i-1就可以，而这个，不联系，所以在i位置上，有可能加上i-1是最大，也有可能是i-2，i-3，所以要循环遍历找到最大值
            for k in range(i):
                if A[i]>A[k]:
                    f[i]=max(f[k]+1,f[i])
        return max(f)

s=Solution()
print(s.longestIncreasingSubsequence([]))