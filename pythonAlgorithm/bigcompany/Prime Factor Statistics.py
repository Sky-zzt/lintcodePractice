class Solution:
    """
    @param N: a number
    @return: the number of prime numbers.
    题目给定一个正整数N，你需要统计(1,N]之间所有整数质数分解后，所有质数的总个数。

Example
输入：6
输出：7
解释：2=2, 3=3, 4=2*2, 5=5, 6=2*3, 个数和为1+1+2+1+2=7
Notice
1<N<=100000

解题思路 利用一个递推的思路，例如40 = 4*10 ,那么40的质数分解个数等于4的质数分解个数加上10的质数分解个数。 开一个数组prime，prime[i]代表i的质数分解个数；当遍历到i时，所有小于等于i的prime值均已得到，故可得到所以i*j的prime值（1<j<i） 复杂度分析

时间复杂度：O(N):每个数计算一次prime值
    """

    def Count_PrimeNum(self, N):
        ans = 0
        vis = [False] * 100005
        prime = [1] * 100005
        for i in range(2, N + 1):
            ans += prime[i]
            k = int(min(N / i, i))
            for j in range(2, k + 1):
                if vis[i * j]:
                    continue
                vis[i * j] = True
                prime[i * j] = prime[i] + prime[j]
        return ans
