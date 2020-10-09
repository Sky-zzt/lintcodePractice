class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    给定整数数组num，从中找到两个数字使得他们和最接近target，返回两数和与 target 的差的 绝对值。

Example
样例1

输入: nums = [-1, 2, 1, -4] 并且 target = 4
输出: 1
解释:
最小的差距是1，(4 - (2 + 1) = 1).

样例2

输入: nums = [-1, -1, -1, -4] 并且 target = 4
输出: 6
解释:
最小的差距是6，(4 - (- 1 - 1) = 6).

    """

    def twoSumClosest(self, nums, target):
        # write your code here
        l, r = 0, len(nums) - 1
        import sys

        diff = sys.maxsize
        while l < r:
            if nums[l] + nums[r] > target:
                diff = min(abs(target - nums[l] + nums[r]), diff)
                r -= 1
            elif nums[l] + nums[r] < target:
                diff = min(abs(target - nums[l] + nums[r]), diff)
                l += 1
            else:
                l
        return diff
