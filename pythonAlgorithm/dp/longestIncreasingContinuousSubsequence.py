class Solution:
    """
    以第i个数组元素结尾，最长的连续子序列的长度
    f[i] = max{ 1, f[i–1]+1| i>0 and a[i-1] < a[i]}
    因为，最短至少是自己 1，所以初始化为 全1
        f[i] = max(f[i - 1] + 1, 1)可以换为下面这个也可以
        f[i] = f[i - 1] + 1

    """

    def longestIncreasingContinuousSubsequence(self, A):
        # 有可能单调增，有可能单调减，所以反转一下
        # M = max(self.calc(A), self.calc(A[::-1]))
        # M = max(self.calc2(A), self.calc2(A[::-1]))
        M = self.calc(A)
        M = self.calc2(A)
        M = self.calc3(A)
        return M

    def calc(self, A):
        if not A: return 0
        size = len(A)
        f = [1] * size
        for i in range(1, size):
            if A[i] > A[i - 1]:
                f[i] = max(f[i - 1] + 1, 1)
                f[i] = f[i - 1] + 1
        print(f)
        return max(f)

    def calc2(self, A):
        if not A: return 0
        size = len(A)
        f = [1] * size
        for i in range(1, size):
            f[i] = f[i - 1]
            if A[i] > A[i - 1]:
                f[i] = max(f[i - 1] + 1, f[i])
        print(f)
        return f[size - 1]

    '''
    calc3  用LCS思想，最后一个进不进LICS来写即 f[i]=max(f[i-1],f[i-1]+1)
    这样写的话，第58行处，如果这么写，确实就和LCS一样了，就是return f[size]，
    但是呢，因为数组元素之间有大小关系，那么58行就不能真么写了，要放到if 语句里面去才可以，因为，可能有（1,2,3,1,2,3,7,8），这种情况,本来应该从1
    开始统计（1,2,3,7,8，五个连续递增的），然而却累加了1（1,2,3）前面的结果，而这个累加就是53行完成的，
    这也就解释了为什么是max（f），因为他可能是某一段的是最长的，并不是发f[n]就是最大值，如 （1,2,3,1,2,3,7,8,0,1）(可以分为连续增长的三段，显然中间的是最大的)
    
    
    '''

    def calc3(self, A):
        if not A: return 0
        size = len(A)
        f = [1] * (size + 1)
        f[0] = 1
        for i in range(1, size + 1):
            # f[i] = f[i - 1]
            if A[i - 1] > A[i - 2]:
                f[i] = f[i - 1]
                f[i] = max(f[i - 1] + 1, f[i])
        print(f)
        return max(f)

    # todo 这个的意义可以理解为，求这个字符串中所有的连续增长串的长度和(核心在于 80行写到了 if外 )
    # todo  事实上 LCS 就是求的两个字符串中，所有的公共子串的长度(即LCS)， 比如：
    '''
    jizhangfbcde       lijiangabcde 
    L:ji zh ang  f bcde   R:li jiang  a  bcde 
       1  2  3   4   5       1   2    3   4
     LCS 就是 L 1+3=2(R) 段 和 L 5/4(R)段的长度和 
     
     
     总之：LCS的那种把 f[i] = f[i - 1]之类的语句直接写到if外，暴露给所有的for循环，那么，求的就是f[n],也就是满足某种性质的所有段的和（参考上面的解释）
     反之，写到 if 内，诸如LICS,那么就是max（f），求的是满足某种性质的最长的一段
     
     用此思路，还可以，求如下：最长公共子串（LCS）-》最长连续公共子串（参考longestCommonSubsequence.py）
     
     最长连续递增公共子串-》最长递增公共子串
     最长递增序列-》最长连续递增序列
     
     题意是连续，就是求某一段 就用max（f）
     题意没说连续，就是求所有满足性质的段的和 就用f[n-1]/f[n]
     
    '''

    def calc4(self, A):
        if not A: return 0
        size = len(A)
        f = [1] * (size + 1)
        f[0] = 1
        for i in range(1, size + 1):
            f[i] = f[i - 1]
            if A[i - 1] > A[i - 2]:
                f[i] = max(f[i - 1] + 1, f[i])
        print(f)
        return f[size]


s = Solution()
print(s.longestIncreasingContinuousSubsequence([1, 2, 3, 1, 2, 3, 7, 8]))
print(s.longestIncreasingContinuousSubsequence(
    [88, 4, 24, 82, 86, 1, 56, 74, 71, 9, 8, 18, 26, 53, 77, 87, 60, 27, 69, 17, 76, 23, 67, 14, 98, 13, 10, 83, 20, 43,
     39, 29, 92, 31, 0, 30, 90, 70, 37, 59]))
