class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    import sys

    best = sys.maxsize

    def minimumTotal(self, triangle):
        # write your code here

        best = self.traverse(0, 0, triangle)
        return best

    def traverse(self, m, n, triangle):
        if m == len(triangle):  # 越界  返回  0
            return 0
        left = self.traverse(m + 1, n, triangle)
        right = self.traverse(m + 1, n + 1, triangle)
        return min(left, right) + triangle[m][n]


s = Solution()

b = [[1],
     [2, 3],
     [4, 5, 6],
     [-1, 3, 8, 3]]
print(s.minimumTotal(b))
