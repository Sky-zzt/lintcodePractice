import sys


class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):
        # write your code here
        MAX = sys.maxsize
        # f=[MAX for i in range(amount+1)]
        f = [MAX] * (amount + 1)
        f[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                '''
                f(x)=min(f(x-2)+1,f(x-5)+1,f(x-3)+1)
                你要保证x-2,x-5...大于0，列表才有意义，才能计算
                而且f[i] != MAX才行，不然没法计算
                f[i] = min(f[i], f[i - coin] + 1) 其实就是打擂台式秋初最小值
                '''
                if i - coin >= 0 & f[i] != MAX:
                    f[i] = min(f[i], f[i - coin] + 1)
        if f[amount] == MAX:
            return -1
        return f[amount]
