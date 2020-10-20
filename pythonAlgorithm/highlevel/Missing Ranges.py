class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    给定一个排序整数数组，其中元素的取值范围为[lower，upper] (包括边界)，返回其缺少的范围。

Example
样例1

输入：
nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
输出：
["2", "4->49", "51->74", "76->99"]
解释：
在区间[0,99]中，缺失的区间有：[2,2]，[4,49]，[51,74]和[76,99]
样例2

输入：
nums = [0, 1, 2, 3, 7], lower = 0 and upper = 7
输出：
["4->6"]
解释：
在区间[0,7]中，缺失的区间有：[4,6]
    """

    # todo 从头到尾遍历一下  如果前一个比后一个大1   区间就  [前+1，后-1]
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        pass
