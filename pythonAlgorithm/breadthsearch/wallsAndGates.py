class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing


    您将获得一个使用这三个可能值初始化的 m×n 2D 网格。
-1 - 墙壁或障碍物。
0 - 门。
INF - Infinity是一个空房间。我们使用值 2 ^ 31 - 1 = 2147483647 来表示INF，您可以假设到门的距离小于 2147483647。
在代表每个空房间的网格中填入到距离最近门的距离。如果不可能到达门口，则应填入 INF。

Example
样例1

输入：
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
输出：
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
解释：
2D网络为：
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
答案为：
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
样例2

输入：
[[0,-1],[2147483647,2147483647]]
输出：
[[0,-1],[1,2]]

    """

    # todo bfs 对于这种多源点 多终点能用类似于number of islands方法做，但是就是慢 呵呵时间复杂度 为
    def wallsAndGates(self, grid):
        # write your code here
        if not grid: return 0
        mark = grid.copy()
        # flag = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2147483647:
                    flag = [[False] * len(grid[0]) for _ in range(len(grid))]
                    self.markByBfs(grid, i, j, mark, flag)
                    # count += 1
        return mark

    def markByBfs(self, grid, x, y, mark, flag):

        from queue import Queue
        directionX = [1, -1, 0, 0]
        directionY = [0, 0, -1, 1]
        q = Queue()
        q.put(Coordinate(x, y))
        flag[x][y] = True
        cnt = 0
        while q.qsize() != 0:
            m = q.qsize()
            cnt += 1
            for _ in range(m):  # 最短路和分层一定要有外层 这个for
                coor = q.get()  # todo 这个是放这里 千万别放外面 呵呵坑逼
                for i in range(4):
                    adj = Coordinate(coor.x + directionX[i],
                                     coor.y + directionY[i])
                    if self.isBound(grid, adj):  continue
                    if grid[adj.x][adj.y] == 0:
                        mark[x][y] = min(cnt, mark[x][y])
                        break
                    if flag[adj.x][adj.y] is False and grid[adj.x][adj.y] != -1:
                        q.put(adj)
                        flag[adj.x][adj.y] = True

    def isBound(self, grid, coor):
        if coor.x < 0 or coor.x >= len(grid): return True
        if coor.y < 0 or coor.y >= len(grid[0]): return True
        return False


s = Solution()
print(s.wallsAndGates(
    [[2147483647, -1, 0, 2147483647],
     [2147483647, 2147483647, 2147483647, -1],
     [2147483647, -1, 2147483647, -1],
     [0, -1, 2147483647, 2147483647]]))
