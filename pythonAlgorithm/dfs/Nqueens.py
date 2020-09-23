class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        #result用于存储答案
        results = []
        self.search(n, [], results)
        return results
    #search函数为搜索函数，n表示已经放置了n个皇后，col表示每个皇后所在的列
    def search(self, n, col, results):
        row = len(col)
        #若已经放置了n个皇后表示出现了一种解法，绘制后加入答案result
        if row == n:
            results.append(self.Draw(col))
            return
        #枚举当前皇后放置的列，若不合法则跳过
        for now_col in range(n):
            if not self.isValid(col, row, now_col):
                continue
            #若合法则递归枚举下一行的皇后
            col.append(now_col)
            self.search(n, col, results)
            col.pop()
    #isValid函数为合法性判断函数
    def isValid(self, cols, row, now_col):
        for r, c in enumerate(cols):
            #若有其他皇后在同一列或同一斜线上则不合法
            if c == now_col:
                return False
            if abs( r - row ) == abs( c - now_col ):
                return False
        return True
    #Draw函数为将col数组转换为答案的绘制函数
    def Draw(self, cols):
        n = len(cols)
        board = []
        for i in range(n):
            row = ['Q' if j == cols[i] else '.' for j in range(n)]
            board.append(''.join(row))
        return board