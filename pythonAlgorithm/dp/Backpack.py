class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
        # 一维数组也可以
    def backPack(self, m, A):
        # write your code here
        l = len(A)
        f = [[False] * (m + 1) for _ in range(l + 1)]
        # f[i][w] = 能否用前i个物品拼出重量w (TRUE / FALSE)
        #f[i][w] = f[i-1][w] OR f[i-1][w-Ai-1]
        f[0][0] = True
        for i in range(1, l + 1):
            for w in range(m + 1):
                if w - A[i - 1] >=0:
                    f[i][w] = f[i - 1][w] or f[i - 1][w - A[i - 1]]
                else:
                    # 这个不能丢
                    f[i][w] = f[i - 1][w]
        for i in range(m, -1, -1):
            if f[l][i]:
                return i
        return 0



s = Solution()
a = s.backPack(10, [3,4,8,5])
print(a)

