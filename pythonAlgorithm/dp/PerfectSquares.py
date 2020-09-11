import math
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    '''
    给一个正整数 n, 请问最少多少个完全平方数(比如1, 4, 9...)的和等于n。
    
    思考 如何判断一个数是否可以拆为完全数之和  
    '''
    def numSquares(self, n):
        # write your code here
        f=[0]*(n)
        f[0]=0
        ##这种的必须用序列型的思想，即，因为我们必须取到n这个数，
        for i in range(1,n):
            print(i)
            import sys
            f[i]=sys.maxsize-1
            for j in range(1,i):
                if i>=j**2>=1:
                    f[i]=min(f[i-j**2]+1,f[i])
        #  不是return max（f）
        return f[n-1]
s=Solution()
print(s.numSquares(13))

'''
        正确做法
    def numSquares(self, n):
        # write your code here
        f=[0]*(n+1)
        f[0]=0
        for i in range(1,n+1):
            import sys
            f[i]=sys.maxsize-1
            for j in range(1,i+1):
                if i>=j**2>=0:
                    f[i]=min(f[i-j**2]+1,f[i])
        #  不是return max（f）
        return f[n]
'''

