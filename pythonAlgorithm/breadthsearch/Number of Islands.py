class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.markByBfs(grid, i, j)
                    count += 1
        return count

    def markByBfs(self, grid, x, y):

        from queue import Queue
        directionX = [-1, 1, 0, 0]
        directionY = [0, 0, -1, 1]
        q = Queue()
        q.put(Coordinate(x, y))
        grid[x][y] = 0
        while q.qsize()!=0:
            coor = q.get()
            for i in range(4):
                adj = Coordinate(coor.x + directionX[i],
                                 coor.y + directionY[i])
                if self.isBound(grid, adj):  continue
                if grid[adj.x][adj.y] == 1:
                    grid[adj.x][adj.y] = 0
                    q.put(adj)

    def isBound(self, grid, coor):
        if coor.x < 0 or coor.x >= len(grid): return True
        if coor.y < 0 or coor.y >= len(grid[0]): return True
        return False


s = Solution()
print(s.numIslands([[1, 1, 0, 0, 0]]))



