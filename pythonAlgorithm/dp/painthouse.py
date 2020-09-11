# f[i][0] = min{f[i-1][1] + cost[i-1][0], f[i-1][2] + cost[i-1][0]}
# f[i][1] = min{f[i-1][0] + cost[i-1][1], f[i-1][2] + cost[i-1][1]}
# f[i][2] = min{f[i-1][0] + cost[i-1][2], f[i-1][1] + cost[i-1][2]}
'''
序列型做法
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, cost):
        # write your code here
        l = len(cost)
        if (l==0): return 0
        f = [[0] * 3 for _ in range(l+1)]
        f[0][0] = f[0][1] = f[0][2] = 0
        for i in range(1,l+1):
            for j in range(3):
                f[i][j]=sys.maxsize
                for k in range(3):
                    if k != j:
                        f[i][j] = min(f[i][j], f[i - 1][k] + cost[i - 1][j])
        return min(f[l][0],f[l][1],f[l][2])
'''
#坐标型做法
import  sys
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """

    def minCost(self, cost):
        # write your code here
        l = len(cost)
        if (l==0): return 0
        f = [[0] * 3 for _ in range(l)]
        f[0][0] = cost[0][0]
        f[0][1] = cost[0][1]
        f[0][2] = cost[0][2]
        for i in range(1,l):
            for j in range(3):
                f[i][j]=sys.maxsize
                for k in range(3):
                    if k != j:
                        f[i][j] = min(f[i][j], f[i - 1][k] + cost[i][j])
        return min(f[l-1][0],f[l-1][1],f[l-1][2])


s=Solution()
print(s.minCost([[14,2,11],[11,14,5],[14,3,10]]))

