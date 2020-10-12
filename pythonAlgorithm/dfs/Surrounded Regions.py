class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    def surroundedRegions(self, board):
        # write your code here
        if not board: return board
        markMatrix = [[True] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if self.dfs(board, i, j, markMatrix): board[i][j] = 'X'
        return board

    def dfs(self, board, x, y, mark):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return False
        if board[x][y] == "X":
            return True

        # if board[x][y] == "O":
        #     mark[x][y]=False
        else:

            if mark[x][y]:
                mark[x][y] = True  # todo 这种 不好回溯啊
                up = self.dfs(board, x - 1, y, mark)
                down = self.dfs(board, x + 1, y, mark)
                left = self.dfs(board, x, y - 1, mark)
                mark[x][y] = False
                right = self.dfs(board, x, y + 1, mark)
            else:
                return True

            return up and down and left and right


s = Solution()
print(s.surroundedRegions([['X', 'X', 'X', 'X'],
                           ['X', 'O', 'O', 'X'],
                           ['X', 'O', 'O', 'X'],
                           ['X', 'X', 'X', 'X']]))
