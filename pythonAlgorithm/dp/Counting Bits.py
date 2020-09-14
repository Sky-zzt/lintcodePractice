class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    设f[i]表示i的二进制表示中有多少个1
    f[i] = f[i>>1] + (i mod 2)
    """

    #  todo  太秒了
    def countBits(self, num):
        dp = [0]
        for i in range(1, num + 1):
            dp.append(dp[i >> 1] + i % 2)
        return dp


print(323432 % 2)
