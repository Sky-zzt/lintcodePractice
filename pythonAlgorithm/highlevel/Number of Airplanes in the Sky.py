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
        room=[]
        #加入开始时间和结束时间，1是房间+1，-1是房间-1
        for i in airplanes:
            room.append((i.start,1))
            room.append((i.end,-1))
        tmp = 0
        ans = 0
        #排序
        room=sorted(room)
        #扫描一遍
        for idx, cost in room:
            tmp += cost
            ans = max(ans,tmp)
        return ans