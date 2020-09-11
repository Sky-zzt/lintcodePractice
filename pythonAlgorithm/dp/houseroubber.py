class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """

    def houseRobber(self, A):
        # write your code here
        l = len(A)
        f = [[0] * 2 for _ in range(l)]
        # 因为房子只有0,1 两种情况 所以一维数组就可以了
        f[0][0] = 0
        f[0][1] = A[0]
        i, j = 1, 0
        for i in range(1, l):
            for j in range(2):
                f[i][j] = 0
                if (j == 1):
                    f[i][j] = f[i - 1][0] + A[i]
                else:
                    f[i][j] = max(f[i - 1][1], f[i - 1][0])
        # return f [[0, 5], [5, 2], [5, 6], [6, 8]]  对于每一个房子，偷和不偷的收益
        return max(max(f))


s = Solution()
print(s.houseRobber([5, 2, 1, 3]))
