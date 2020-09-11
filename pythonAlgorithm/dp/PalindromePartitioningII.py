class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def minCut(self, s):
        # write your code here
        l=len(s)
        f=[0]*l
        f[0]=1
        for i in range(l):
            import sys
            f[i]=sys.maxsize
            for j in range(i):
                if self.isPalindrom(s[j:i]) and f[j]!=sys.maxsize:
                    f[i]=min(f[j]+1,f[i])
        return f[l]
    def isPalindrom(self,s):
        pass

s='sdssd'

print(s[2:5])