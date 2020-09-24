class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    import sys

    best = sys.maxsize

    def minimumTotal(self, triangle):
        # write your code here
        import sys

        hash = [[sys.maxsize] * len(triangle[len(triangle) - 1]) for _ in range(len(triangle))]
        best = self.traverse(0, 0, triangle, hash)
        return best

    def traverse(self, m, n, triangle, hash):
        if m == len(triangle):  # 越界  返回  0
            return 0
        import sys
        if hash[m][n] != sys.maxsize:  # 记住的是每个节点向下的和最小的值，然后下次有人来就不用了在去重复计算这个节点的向下的最下的值了 ，这个三角形和树还是不一样的，树上的节点不能重复到达
            return hash[m][n]
        left = self.traverse(m + 1, n, triangle, hash)
        right = self.traverse(m + 1, n + 1, triangle, hash)
        hash[m][n] = min(left, right) + triangle[m][n]
        return hash[m][n]


s = Solution()

b = [[1],
     [2, 3],
     [4, 5, 6]]
print(s.minimumTotal(b))
