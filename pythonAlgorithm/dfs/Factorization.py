import math


class Solution:
    """
    @param n: An integer
    @return: a list of combination
    一个非负数可以被视为其因数的乘积。编写一个函数来返回整数 n 的因数所有可能组合。

* 组合中的元素(a1,a2,...,ak)必须是非降序。(即，a1≤a2≤...≤ak)。 * 结果集中不能包含重复的组合。
样例
样例1

输入：8
输出： [[2,2,2],[2,4]]
解释： 8 = 2 x 2 x 2 = 2 x 4
样例2

输入：1
输出： []
    """

    def getFactors(self, n):
        ans = []

        def dfs(n: int, biggerFactor, res):
            # 空队列不能作为结果
            if len(res):
                res.append(int(n))
                ans.append(res[:])
                res.pop()
            for i in range(biggerFactor, math.floor(math.sqrt(n) + 1)):  # 从biggerFactor--sqrt(n)查找因子
                if n % i == 0:  # 若i是n的因子，则添加，然后将i作为ind去查找更大的因子
                    res.append(i)
                    dfs(n // i, i, res[:])
                    res.pop()

        dfs(n, 2, [])
        return ans
