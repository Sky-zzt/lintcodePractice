class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """

    PEOPLE = 0
    ZOMBIE = 1
    WALL = 2

    def zombie(self, grid):
        # write your code here
        if not grid: return 0
        from queue import Queue
        directionX = [-1, 1, 0, 0]
        directionY = [0, 0, -1, 1]
        q = Queue()
        people = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.PEOPLE:
                    people += 1
                elif grid[i][j] == self.ZOMBIE:
                    q.put(Coordinate(i, j))
        if people == 0: return 0
        day = 0
        while q.qsize() == 0:
            size = q.qsize()
            day += 1
            coor = q.get()
            for i in range(size):
                for j in range(4):
                    adj = Coordinate(coor.x + directionX[j], coor.y + directionY[j])
                    if grid[adj.x][adj.y] == self.PEOPLE:
                        grid[adj.x][adj.y] = self.ZOMBIE
                        q.put(adj)
                        people -= 1
                    if people == 0:
                        return day
                    if grid[adj.x][adj.y] == self.WALL:
                        continue

        return -1
'''

class Coordinate {
    int x, y;
    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Solution {
    public int PEOPLE = 0;
    public int ZOMBIE = 1;
    public int WALL = 2;
    
    public int[] deltaX = {1, 0, 0, -1};
    public int[] deltaY = {0, 1, -1, 0};
     
    /**
     * @param grid a 2D integer grid
     * @return an integer
     */
    public int zombie(int[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int n = grid.length;
        int m = grid[0].length;
        
        // initialize the queue & count people
        int people = 0;
        Queue<Coordinate> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == PEOPLE) {
                    people++;
                } else if (grid[i][j] == ZOMBIE) {
                    queue.offer(new Coordinate(i, j));
                }
            }
        }
        
        // corner case
        if (people == 0) {
            return 0;
        }
        
        // bfs
        int days = 0;
        while (!queue.isEmpty()) {
            days++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Coordinate zb = queue.poll();
                for (int direction = 0; direction < 4; direction++) {
                    Coordinate adj = new Coordinate(
                        zb.x + deltaX[direction],
                        zb.y + deltaY[direction]
                    );
                    
                    if (!isPeople(adj, grid)) {
                        continue;
                    }
                    
                    grid[adj.x][adj.y] = ZOMBIE;
                    people--;
                    if (people == 0) {
                        return days;
                    }
                    queue.offer(adj);
                }
            }
        }
        
        return -1;
    }
'''