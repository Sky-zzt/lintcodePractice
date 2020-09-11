class Solution:
    # 需要len（a）<len(b)
    def LongestConsecutiveSequence(self, A, B):
        m = len(A)
        n = len(B)
        f = [0] * (m)
        if A[0] == B[0]: f[0] = 1
        '''
        f[i] is 以A[i] B[i] 结尾的连续子序列的长度
        
        LCS 是 设f[i][j]为A前i个字符A[0..i-1]和B前j个字符[0..j-1]的最长公共子串的长度
        '''
        for i in range(1, m):
            for j in range(1, n):
                if (A[i] == B[j]):
                    f[i] = max(f[i - 1] + 1, 1)

        print(f)
        return max(f)




s = Solution()
print(s.LongestConsecutiveSequence('abcwc', 'abcd'))
#print(s.LongestConsecutiveSequenceOne([1,2,3,4,2]))
