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

    def wallsAndGates(self, rooms):
        # write your code here
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==2^31-1:
                    self.bfs(rooms,i,j)
    # def bfs(self,rooms,x,y):
    #     q=[]
    #     directionX=[-1,1,0,0]
    #     directionY=[0,0,-1,1]
    #     q.append(rooms[x][y])
    #     cnt=0
    #     while not q:
    #         poll = q.pop()
    #         m=len(q)
    #         cnt+=1
    #         for i in range(m):
    #             poll.x=12
    #             new=poll.y=15
    #             if rooms[new]==-1:
    #             #     mark[x]y=cnt
    #             # if new is valid:
    #             #     q.append(new)

