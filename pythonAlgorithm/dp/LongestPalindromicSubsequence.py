class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    '''
    设f[i][j]为S[i..j]的最长回文子串的长度
    注意 f[i][j]是指i-j的回文串长度，不是指i-j是回文串
    '''

    def longestPalindromeSubseq(self, s):
        # write your code here
        l = len(s)
        f = [[0] * (l) for _ in range(l)]
        for i in range(l):
            f[i][i]=1

        for i in range(l-1):
            if s[i]==s[i+1]:
                f[i][i+1]=2
            else:
                f[i][i+1]=1
        for length in range(3, l+1):
            for i in range(l - length+1):
                j = i + length - 1
                f[i][j] = max(f[i + 1][j], f[i][j - 1])
                if s[i] == [j]:
                    f[i][j] = max(f[i][j], f[i + 1][j - 1] + 2)
        print(f)
        return f[0][l-1]
s=Solution()

print(s.longestPalindromeSubseq("bbbab"))