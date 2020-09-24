class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    import sys

    best = sys.maxsize

    def minimumTotal(self, triangle):
        # write your code here
        f = [[0] * len(triangle[len(triangle) - 1]) for _ in range(len(triangle))]
        f[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        for i in range(1, len(triangle)):
            for j in range(1, i):  # i 不能等于j，因为这种特殊情况已经前面初始化过了
                f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        return min(f[len(triangle) - 1])


s = Solution()

b = [[-1],
     [2, 3],
     [1, -1, -3]]
print(s.minimumTotal(b))
