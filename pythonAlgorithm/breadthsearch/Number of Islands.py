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
        while q:
            ele = q.get()
            for i in range(4):
                coor = Coordinate(ele.x + directionX[i], ele.y + directionY[i])
                if not self.isBound(grid, coor):  continue
                if grid[coor.x][coor.y] == 1:
                    grid[coor.x][coor.y] = 0
                    q.put(coor)

    def isBound(self, grid, coor):
        if coor.x < 0 or coor.x >= len(grid): return False
        if coor.y < 0 or coor.y >= len(grid[0]): return False
        return True


s = Solution()
print(s.numIslands([[1, 1, 0, 0, 0]]))
