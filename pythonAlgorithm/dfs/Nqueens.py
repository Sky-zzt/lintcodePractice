class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    # todo 把他当成排列 做就行
    def solveNQueens(self, n):
        # result用于存储答案
        results = []
        self.search(n, [], results)
        return results

    # search函数为搜索函数，n表示已经放置了n个皇后，col表示每个皇后所在的列
    def search(self, n, col, results):
        if len(col)==n:results.append(self.Draw(col))
        for colIndex in range(n):
            if not self.isValid(col,colIndex):continue
            col.append(colIndex)
            self.search(n,col,results)
            col.pop()


    def isValid(self, cols, colIndex):
        def isValid(self, cols, row, now_col):
            for r, c in enumerate(cols):
                # 若有其他皇后在同一列或同一斜线上则不合法
                if c == now_col:
                    return False
                if abs(r - row) == abs(c - now_col):
                    return False
            return True

    # Draw函数为将col数组转换为答案的绘制函数
    def Draw(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board


s = Solution()
print(s.solveNQueens(4))
