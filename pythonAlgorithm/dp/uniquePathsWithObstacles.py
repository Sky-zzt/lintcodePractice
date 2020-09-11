class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    '''
    如果是求max呢  
    '''

    def uniquePathsWithObstacles(self, obstacleGrid):
        #  write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     f[i][0] = 1
        # for i in range(n):
        #     f[0][i] = 1
        f[0][0]=1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                f[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            else:
                f[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                #if obstacleGrid[i][j-1] != 1:
                   # f[i][j] = f[i][j] + f[i][j - 1]
                if obstacleGrid[i][j] != 1:
                    f[i][j] = f[i - 1][j] + f[i][j-1]
        return f[m - 1][n - 1]


s = Solution()
print(s.uniquePathsWithObstacles([[0, 0], [1, 0], [0, 0]]))
print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
