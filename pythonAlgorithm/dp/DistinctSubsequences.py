class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    '''
    f[i][j] = f[i-1][j-1]|A[i-1]=B[j-1] + f[i-1][j]
 
    设f[i][j]为B前j个字符B[0..j-1]在A前i个字符A[0..i-1]中出现多少次
    '''
    # todo dp方程没有加1，也不是max，记住，不是max，min的一般没有+1 +A[i]的操作
    def numDistinct(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 0
        for i in range(1, n + 1):
            f[0][i] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = f[i - 1][j]
                if A[i - 1] == B[j - 1]:
                    # f[i][j] = max(f[i - 1][j - 1]+1, f[i][j]) # 6   这个求的是，B的字符在A中出现了几次
                    # f[i][j] += f[i - 1][j - 1] + 1  # 14
                    f[i][j] = f[i - 1][j - 1] + 1  # 6  那么思考一下，B的字符在A中出现了几次 这个的动态规划怎们写，然后，对比一下
        return f[m][n]


'''
此题需要好好琢磨一下
'''
s = Solution()
S = "rabbbit"
T = "rabbit"
print(s.numDistinct(S, T))
'''
正确做法：
    def numDistinct(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 1
        for i in range(1,n+1):
            f[0][i]=0
        for i in range(1, m+1):
            for j in range(1, n+1):
                f[i][j] = f[i - 1][j]
                if A[i - 1] == B[j - 1]:
                    f[i][j] += f[i - 1][j - 1]

        return f[m][n]

'''
