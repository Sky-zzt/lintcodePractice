class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """

    # 这个题 之所以跑的慢 是因为没有优化，导致慢，在有大量“O”的情况下，至少是 3^n 级别的复杂度 ，十分恐怖
    def surroundedRegions(self, board):
        # write your code here
        res = []
        hash = [[-1] * len(board[0]) for _ in range(len(board))]
        mark = [[True] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    if self.dfs(board, i, j, res, mark, hash):
                        print((i, j))
                        board[i][j] = 'X'
                    # if self.bfs(board, i, j, hash): board[i][j] = 'X'
                    # print(res)
                    res.clear()  # TODO  每次递归前先清空 因为我的思路是 上下左右都为true的时候，才更新
        return board

    def dfs(self, board, x, y, res, mark, hash):
        directionX = [-1, 1, 0, 0]
        directionY = [0, 0, -1, 1]
        if (x <= 0 or y <= 0 or x >= len(board) - 1 or y >= len(board[0]) - 1) and board[x][y] == 'O': return False
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]): return False
        if board[x][y] == 'X': return True
        # if board[x][y] == 'O': mark[x][y] = False
        if hash[x][y] != -1:
            return hash[x][y]  # 一招记忆化 时间复杂度从 3^n 到 m*n
        if mark[x][y]:
            for i in range(4):
                if board[x][y] == 'O': mark[x][y] = False
                isok = self.dfs(board, directionX[i] + x, directionY[i] + y, res, mark, hash)
                if board[x][y] == 'O': mark[x][y] = True
                res.append(isok)  # TODO 标记了已访问导致其他的递归不能进去，那就在这个递归结束后回去掉标记  好
        hash[x][y] = False not in res
        return hash[x][y]
        # else:
        #     return True  # 如下图在（1,1）这一轮递归中，他已经访问过（1,1）点了，然后他在（2,1）点又想访问（1,1），那么我们不让他访问，让他直接return true，return None也行，就是不能return fasle
        # 做标记主要是房主重复访问导致的死循环

    def bfs(self, grid, x, y, hash):

        from queue import Queue
        if hash[x][y] != -1:
            return hash[x][y]  # 一招记忆化 时间复杂度从 3^n 到 m*n

        directionX = [-1, 1, 0, 0]
        directionY = [0, 0, -1, 1]
        q = Queue()
        q.put(Coordinate(x, y))
        s = set()
        res = set()  # todo  很妙的方法 dfs 也可以参考这么做
        while q.qsize() != 0:
            coor = q.get()

            for i in range(4):
                adj = Coordinate(coor.x + directionX[i],
                                 coor.y + directionY[i])
                if self.isBound(grid, adj):
                    res.add(False)
                    continue
                if hash[adj.x][adj.y] != -1:
                    return hash[x][y]  # 一招记忆化 时间复杂度从 3^n 到 m*n
                if grid[adj.x][adj.y] == 'O' and (adj.x, adj.y) not in s:
                    s.add((adj.x, adj.y))
                    q.put(adj)
                else:
                    res.add(True)
        hash[x][y] = False not in res
        return hash[x][y]

    def isBound(self, grid, coor):
        if coor.x < 0 or coor.x >= len(grid): return True
        if coor.y < 0 or coor.y >= len(grid[0]): return True
        return False


s = Solution()
ss = s.surroundedRegions([['X', 'X', 'X', 'X', 'X'],
                          ['X', 'X', 'X', 'X', 'X'],
                          ['X', 'X', 'O', 'O', 'X'],
                          ['X', 'X', 'O', 'X', 'X'],
                          ['X', 'X', 'O', 'X', 'X'],
                          ])
for i in ss:
    print(i)

'''
["XOOXXXOXXOOOOOOOOOOO","XOOXXOOXOOOXOXOXOOXO","OOOXXXXOXOXXOOOOXOXO","OOOXXOOXOOOXXXOOXOOX","OOOOOOOXXXOOOOOOOOOO","XOOOOXOXOXXOOOOOOXOX","OOOXOOOXOXOXOXOXOXOX","OOOXOXOOXXOXOXXOXXXO","OOOOXOOXXOOOOXOOOXOX","OOXOOXOOOOOXOOXOOOXO","XOOXOOOOOOOXOOXOXOXO","OXOOOXOXOXXOXXXOXXOO","XXOXOOOOXOOOOOOXOOOX","OXOOXXXOOOXXXXXOXOOO","OOXXXOOOXXOOOXOXOOOO","XOOXOXOOOOXOOOXOXOXX","XOXOOOOOOXOOOXOXOOOO","OXXOOOXXXOXOXOXXXXOO","OXOOOOXXOOXOXOOXOOXX","OOOOOOXXXXOXOOOXXOOO"]

'''
a = ["XOOXXXOXXOOOOOOOOOOO", "XOOXXOOXOOOXOXOXOOXO", "OOOXXXXOXOXXOOOOXOXO", "OOOXXOOXOOOXXXOOXOOX",
     "OOOOOOOXXXOOOOOOOOOO", "XOOOOXOXOXXOOOOOOXOX", "OOOXOOOXOXOXOXOXOXOX", "OOOXOXOOXXOXOXXOXXXO",
     "OOOOXOOXXOOOOXOOOXOX", "OOXOOXOOOOOXOOXOOOXO", "XOOXOOOOOOOXOOXOXOXO", "OXOOOXOXOXXOXXXOXXOO",
     "XXOXOOOOXOOOOOOXOOOX", "OXOOXXXOOOXXXXXOXOOO", "OOXXXOOOXXOOOXOXOOOO", "XOOXOXOOOOXOOOXOXOXX",
     "XOXOOOOOOXOOOXOXOOOO", "OXXOOOXXXOXOXOXXXXOO", "OXOOOOXXOOXOXOOXOOXX", "OOOOOOXXXXOXOOOXXOOO"]
res = []
ans = []


def f(arr):
    for i in range(len(arr)):
        ans = []
        for j in arr[i]:
            ans.append(j)
        res.append(ans)
        # ans.clear()


f(a)
for i in res:
    print(i)
print("*********")
ss = s.surroundedRegions(res)

for i in ss:
    print(i)
