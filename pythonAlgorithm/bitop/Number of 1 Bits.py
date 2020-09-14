class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    '''
    	
C语言中循环结束应该是flag==0，但是python 整数存取的时候没有位数限制。
因为python的int是无线精度的，c++的int是32为的，所以python的负数相当于前面有无限个1，要对python的负数做处理
    '''

    # todo https://blog.csdn.net/u010005281/article/details/79851154
    def hammingWeight(self, n):
        # write your code here
        num = n
        flag = 1
        count = 0
        while flag <= 0xffffffff:
            if num & flag:
                count += 1
            flag = flag << 1
        return count


s = Solution()
s.hammingWeight(2)
