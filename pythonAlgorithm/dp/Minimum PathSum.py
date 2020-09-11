class Solution:
    """

    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    """
    
    f[]
    """

    def minPathSum(self, grid):
        # write your code here
        if grid is None or not grid:return 0
        m = len(grid)
        n = len(grid[0])
        f = [[0] * n for _ in range(m)]
        f[0][0] = grid[0][0]
        for i in range(1, m):
            f[i][0] = f[i - 1][0] + grid[i][0]
            for j in range(1, n):
                f[0][j] = f[0][j - 1] + grid[0][j]
                f[i][j] = min(f[i - 1][j], f[i][j - 1])+grid[i][j]
        return f[m - 1][n - 1]
s=Solution()
print(s.minPathSum( [[1,3,1],[1,5,1],[4,2,1]]))