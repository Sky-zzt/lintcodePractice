class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    '''
    
    将所有信封按照长度从小到大：E0, E1, …, En-1
    如果信封Ei能放入信封Ej里，一定有i<j
    f[i]是以Ei为最外层信封是最多的嵌套层数
    发f[i]=max{1,f[j]+1|Ej能放在Ei里}
    
    其实就是longestIncreasingSubsequence的变种，
    如果是三维数组，那该怎们做呢
    '''

    def maxEnvelopes(self, A):
        if A is None or not A:return 0
        l = len(A)
        f = [1] * l
        A = sorted(A, key=lambda x: (x[0], -x[1]))
        for i in range(l):
            for j in range(i):
                #注意题意是长宽严格小于，所以还要加A[i][0] > A[j][0]
                if A[i][1] > A[j][1] and A[i][0] > A[j][0]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)


s = Solution()
print(s.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))
