class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        # write your code here
        res = set()
        hash = [[-1] * len(board[0]) for _ in range(len(board))]
        mark = [[True] * len(board[0]) for _ in range(len(board))]  # 标记矩阵
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if self.dfs(board, i, j, res, mark, hash):
                        board[i][j] = 'X'
                    res.clear()  # TODO  每次递归前先清空 因为我的思路是 上下左右都为都是'X'的时候，才更新
        return board

    def dfs(self, board, x, y, res, mark, hash):
        directionX = [-1, 1, 0, 0]
        directionY = [0, 0, -1, 1]
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return False  # 越界
        if board[x][y] == 'X': return True
        if hash[x][y] != -1:
            return hash[x][y]  # 记忆化
        if mark[x][y]:
            for i in range(4):  # 上下左右搜
                if board[x][y] == 'O': mark[x][y] = False
                isOk = self.dfs(board, directionX[i] + x, directionY[i] + y, res, mark, hash)
                if board[x][y] == 'O': mark[x][y] = True  # 回溯
                res.add(isOk)  # TODO  res 存的是四个方向 的结果，都为true 说明O都被  'X'围绕，可以替换为 X
        hash[x][y] = False not in res  #
        return hash[x][y]
