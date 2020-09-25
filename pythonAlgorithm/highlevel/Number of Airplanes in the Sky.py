"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


# todo 还可以用前缀和做
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        room = []
        # 加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i.start, 1))
            room.append((i.end, -1))
        tmp = 0
        ans = 0
        # 排序
        room = sorted(room)
        # 扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans, tmp)
        return ans

    # class Test:
    #     def __init__(self, x, y):
    #         self.x = x
    #         self.y = y
    #
    # t1=Test(1,2)
    # t2=Test(1,3)
    # t3=Test(1,0)
    #
    # res=[t1,t2,t3]
    # print(res[0].y)
    # a=sorted(res,key=lambda t:(t.x,t.y))
    #
    # print(a[0].y)

    def maxAirPlane(self, airplanes):
        container = []
        for i in airplanes:
            container.append(Point(i[0], 1))
            container.append(Point(i[1], 0))
        container = sorted(container, key=lambda p: (p.time, p.flag))

        count = 0
        ans = 1
        for i in container:
            if i.flag == 1:
                count += 1
            else:
                count -= 1
            ans = max(ans, count)
        return ans


class Point:
    def __init__(self, time, flag):
        self.time = time
        self.flag = flag


s = Solution()
print(s.maxAirPlane([(1, 5), (2, 3), (3, 4)]))
