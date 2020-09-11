class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    '''
    一下为错误解法
    她的问题在于边界条件下 如m=1   range（1，1）是不进入循环的
    导致f[i][0]无法赋值
        可以单独开循环赋值
        public int uniquePaths(int m, int n) {
        int[][] f = new int[m][n];
        f[0][0] = 1;
        for (int i = 0; i <m; i++) {
            f[i][0]=1;
        }
        for (int i = 0; i < n; i++) {
            f[0][i]=1;
        }
        for (int i = 1; i < m; i++) {
            f[i][0]=1;
            for (int j = 1; j < n; j++) {
                f[0][j]=1;
                f[i][j]=f[i-1][j]+f[i][j-1];
            }
        }
    return f[m-1][n-1];
    }
    
    '''
    def uniquePaths(self,m , n):
        # write your code here
        f = [[0] * n for _ in range(m)]
        f[0][0]=1
        for i in range(1,m):
            f[i][0]=1
            for j in range(1,n):
                f[0][j]=1
                f[i][j]=f[i-1][j]+f[i][j-1]
        return f[m-1][n-1]
    #正确解法
    def uniquePaths1(self,m , n):
        # write your code here
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            f[i][0]=1
            for j in range(n):
                f[0][j]=1
                if i>=1 and j>=1:
                    f[i][j]=f[i-1][j]+f[i][j-1]
        return f[m-1][n-1]

## todo min  max  是一个多选1 的过程，而，共有多少种是，多个的和的过程，所以，A->B 最多有几种走法没啥意义
    def uniquePathsmax(self,m , n):
        # write your code here
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            f[i][0]=1
            for j in range(n):
                f[0][j]=1
                if i>=1 and j>=1:
                    f[i][j]=f[i-1][j]+f[i][j-1]
        return f[m-1][n-1]


s=Solution()
print(s.uniquePaths1(3, 3))
print(s.uniquePathsmax(3, 3))