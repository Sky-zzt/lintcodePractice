class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m=0, A=None, V=None):
        if A is None:
            A = []
        l = len(A)
        f = [[0] * (m + 1) for _ in range(l + 1)]
        f[0][0] = 0
        for i in range(1,m + 1):
            f[0][i] = -1
        # for i in range(1,l + 1):
        #     f[i][0] = 0

        for i in range(1, l+1):
            for w in range(m+1):
                if w >=A[i - 1] and f[i - 1][w - A[i - 1]] != -1:
                    f[i][w] = max(f[i - 1][w], f[i - 1][w - A[i - 1]] + V[i - 1])
                    ##有缺了else的内容
                else:
                    f[i][w] = f[i - 1][w]


        return max(max(row) for row in f)
s=Solution()
print(s.backPackII(m=10, A=[2, 3, 5, 7], V=[1, 5, 2, 4]))