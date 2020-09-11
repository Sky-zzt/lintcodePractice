class Solution1:
    """
    最长连续单调子序列
    f[j] =以a[j]结尾的最长连续上升子序列的长度

    f[j] = max{ 1, f[j–1]+1| j>0 and a[j-1] < a[j]}
    最终答案是max{f[0], f[1], f[2], …, f[n-1]}


    """
    def longestIncreasingContinuousSubsequence(self, A):
        # 有可能单调增，有可能单调减，所以反转一下
        M = max(self.calc(A), self.calc(A[::-1]))
        # M = max(self.calc2(A), self.calc2(A[::-1]))
        return M
    def calc(self, A):
        if not A: return 0
        size = len(A)
        f = [1] * size
        for i in range(1, size):
            if A[i] > A[i - 1]:
                f[i] = max(f[i - 1] + 1, 1)
                f[i] = f[i - 1] + 1
        return max(f)   # 求max（f）  我可不可以学下面的lcs 直接f[size] 得出结果 该怎么定义dp方程


class Solution2:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    '''
    LCS中 最后一个 对子中 有没有 以下
    对子中没有A[m-1]
    对子中没有B[n-1]
    对子中没有A[m-1]和B[n-1]
    对子中有A[m-1]和B[n-1]
    
    
    设f[i][j]为A前i个字符A[0..i-1]和B前j个字符[0..j-1]的最长公共子串的长度
    f[i][j] = max{f[i-1][j], f[i][j-1], f[i-1][j-1]+1|A[i-1]=B[j-1]}
    '''

    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1], f[i - 1][j - 1])
                if A[i - 1] == B[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1, f[i - 1][j - 1])

        return f[m][n] # 我可不可以学上面的 用max（f） 得出结果，该怎么定义dp方程