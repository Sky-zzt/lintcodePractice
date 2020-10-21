class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    给定 n 本书, 第 i 本书的页数为 pages[i]. 现在有 k 个人来复印这些书籍, 而每个人只能复印编号连续的一段的书, 比如一个人可以复印 pages[0], pages[1], pages[2], 但是不可以只复印 pages[0], pages[2], pages[3] 而不复印 pages[1].

所有人复印的速度是一样的, 复印一页需要花费一分钟, 并且所有人同时开始复印. 怎样分配这 k 个人的任务, 使得这 n 本书能够被尽快复印完?

返回完成复印任务最少需要的分钟数.

Example
样例 1:

输入: pages = [3, 2, 4], k = 2
输出: 5
解释: 第一个人复印前两本书, 耗时 5 分钟. 第二个人复印第三本书, 耗时 4 分钟.
样例 2:

输入: pages = [3, 2, 4], k = 3
输出: 4
解释: 三个人各复印一本书.
Challenge
时间复杂度 O(nk)

Notice
书籍页数总和小于等于2147483647
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





