class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B

    常规做法：
    思路
矩阵乘法的实现：一个m行n列的矩阵A，与一个n行p列的矩阵B可以相乘，得到的结果AB是一个m行p列的矩阵，其中的第i行第j列位置上的数AB(i,j)为，矩阵A第i行上的n个数与矩阵B第j列上的n个数一一对应相乘后，所得到的n个乘积之和。直接模拟即可。

复杂度分析
空间复杂度O(n^2)

时间复杂度O(n^3)



    一种时间复杂度也为
O(k∗n2)
 的办法（k 为一行中的非零位个数） 这种办法比较巧妙，通过初始化结果矩阵，然后把非零位逐个累乘累加的办法，而不是按照原来的矩阵乘法顺序在做。
    """

    def multiply(self, A, B):
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0] * k for i in range(n)]

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for l in range(k):
                        C[i][l] += A[i][j] * B[j][l]
        return C
