'''
小易有n根柱子，第i根柱子的高度为h_ih
​i
​​ ,一开地小易站在第一根柱子上。小易可以从i根柱子跳到第j根柱子，当且仅当 h_j \leq h_ih
​j
​​ ≤h
​i
​​  并且 1 \leq j-i \leq k1≤j−i≤k ,其中k为指定的一个数字。另外小易拥有一次放超能力的机会,这个超能力能让小易从柱子i跳到任意满足 1 \leq j-i \leq k1≤j−i≤k的柱子而无视柱子高度的限制。
现在小易想知通,小易是否能到达第n根柱子。

Example
例1:

输入:h=[3,2,7,4],k=2
输出:true
解释:你可以使用超能力，从第一根跳到第三根。然后按照规则，从第三根跳到第四根
例2:

输入:h=[3,4,5,6],k=2
输出:false
Notice
2 \leq n,k \leq 10002≤n,k≤1000
1 \leq h[i] \leq 10^91≤h[i]≤10
​9
​​



'''


class Solution:
    """
    @param h: the height of n pillar
    @param k: the limit
    @return: Xiao Yi can or can't reach the n-th pillar
    """
    def jumpPillar(self, h, k):
        # write your code here.
        # write your code here.
        dp = [[0,0] for i in range(10500)]
        n = len(h)
        dp[0][0] = 1
        for i in range(0, n):
            for j in range(i + 1,min(n - 1, i + k) + 1):
                if h[i] >= h[j]:
                    dp[j][0] = max(dp[j][0], dp[i][0])
                    dp[j][1] = max(dp[j][1], dp[i][0])
                dp[j][1] = max(dp[j][1], dp[i][0])
        if not dp[n - 1][0] + dp[n - 1][1] == 0:
            return  True
        return False