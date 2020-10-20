"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.

    给出一个无重叠的按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

Example
样例 1：

输入:
(2, 5) into [(1,2), (5,9)]
输出:
[(1,9)]
样例 2：

输入:
(3, 4) into [(1,2), (5,9)]
输出:
[(1,2), (3,4), (5,9)]
    """

    # todo 插入进去 调一下 merge interval
    # 间类问题总结
    # 区间类问题总结
    # • 把区间在数轴上画出来 （脑海中 or 纸上）
    # • 往往会将区间按照左端点从小到大排个序
    def insert(self, intervals, newInterval):
        # write your code here
        pass
