class Solution:
    """
    @param Points: a list of [x, y]
    @return: return a list of points
    给定一个坐标点列表 Points，其中Points 中 Point[i][0] 表示横轴坐标，Points[i][1] 表示纵轴坐标。
当存在点 p 满足 Points 中任意点都不在 p 的右上方区域内（横纵坐标都大于p），则称其为最大点。
返回所有最大点，列表中的最大点按照 X 轴从小到大的方式排序。


   todo  首先对于所有的点进行x坐标从大到小排序。 然后用一个变量 max_y 来存储目前最大的y。 当你遍历这个排好序的数组的时候，只要该点的 y 大于 max_y 就证明是最大点。
   todo 如上是两个变量的通用手法
    """

    def MaximumPointsSet(self, Points):
        # write your code here
        n, max_y = len(Points), -1
        vis, result = [0] * n, []

        nums = sorted(Points, key=lambda x: -x[0])

        for i in range(n):
            if nums[i][1] > max_y:
                vis[i] = 1
            max_y = max(nums[i][1], max_y)

        for i in range(n - 1, -1, -1):
            if vis[i] == 1:
                result.append([nums[i][0], nums[i][1]])

        return result