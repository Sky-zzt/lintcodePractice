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

        best = sys.maxsize
        self.traverse(0, 0, 0, len(triangle), triangle, best)
        return best

    def traverse(self, m, n, sum, rows, triangle, best):
        if m == rows:
            best = min(best,
                       sum)  # todo  it is vital to think why best is list work ,numberic not work (I mean can take elemet out or not )
            return
        sum += triangle[m][n]
        self.traverse(m + 1, n, sum, rows, triangle, best)
        self.traverse(m + 1, n + 1, sum, rows, triangle, best)


s = Solution()
print(s.minimumTotal([[-10]]))
