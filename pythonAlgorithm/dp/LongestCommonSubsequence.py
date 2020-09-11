class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    '''
    对子中没有A[m-1]
    对子中没有B[-1]
    对子中没有A[m-1]和B[-1]
    对子中有A[m-1]和B[-1]
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
        # print(f)
        return f[m][n]

    def LongestConsecutiveSequence(self, A, B):
        m = len(A)
        n = len(B)
        f = [0] * (m)
        if A[0] == B[0]: f[0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if (A[i] == B[j] and A[i - 1] != B[j]):
                    f[i] = max(f[i - 1] + 1, 1)

        print(f)
        return max(f)

    # TODO LongestConsecutiveSequence是最长连续公共子串，把 f[i]=max(f[i],f[i-1])语句移到外面就变成了LCS
    def LongestConsecutiveSequenceMax(self, A, B):
        m = len(A)
        n = len(B)
        f = [0] * (m)
        if A[0] == B[0]: f[0] = 1

        for i in range(1, m):
            for j in range(1,n):
                f[i]=max(f[i],f[i-1])
                if (A[i] == B[j] ):
                    f[i] = max(f[i - 1] + 1, f[i])

        print(f)
        return f[m-1]


s = Solution()
print(s.LongestConsecutiveSequence('abcwc', 'abcd'))
print(s.LongestConsecutiveSequenceMax('abcfwcc', 'abcdwccccc'))
print(s.longestCommonSubsequence("jiuzhang", "lijiang"))
print(s.longestCommonSubsequence('abcfwcc', 'abcdwccccc'))
