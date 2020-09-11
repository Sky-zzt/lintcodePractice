class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        '''
        python 的并且是and 不是&
        :param A:
        :return:
        '''
        i=0
        l=len(A)
        f=[False]*l
        f[0]=True
        for i in range(1,l):
            for j in range(i):
                if(f[j]&(A[j]>=i-j)):
                    f[i]=True
        return f[l-1]

s=Solution()
print(s.canJump([4,6,9,5,9,3,0]))
