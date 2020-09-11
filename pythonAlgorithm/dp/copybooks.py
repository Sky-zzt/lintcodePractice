class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        l=len(pages)
        f=[[0]*(l+1) for _ in range(k+1)]
        import sys

        for k in range(k+1):
            f[k][0]=0
        for i in range(1, l+ 1):
            f[0][i] = sys.maxsize
        p=0
        if k > l: k = l
        for k in range(1,k+1):
            for i in range(1,l+1):
                for j in range(i+1):
                    for x in range(j,i):
                        p+=pages[x]

                    f[k][i]=min(max(f[k-1][j],p),f[k][i])
        print(f)
        return f[k][l]

s=Solution()
print(s.copyBooks([3, 2, 4], 2))





