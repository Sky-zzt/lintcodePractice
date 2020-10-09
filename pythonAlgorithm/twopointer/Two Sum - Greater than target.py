class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer

    给一组整数，问能找出多少对整数，他们的和大于一个给定的目标值。

Example
样例 1:

输入: [2, 7, 11, 15], target = 24
输出: 1
解释: 11 + 15 是唯一的一对

样例 2:

输入: [1, 1, 1, 1], target = 1
输出: 6

Challenge
O(1) 额外空间以及 O(nlogn) 时间复杂度
    """

    def twoSum2(self, nums, target):
        # write your code here
        nums = sorted(nums)
        l = 0
        count = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] <= target:
                l += 1
            else:
                count += len(nums) - r
                r -= 1
        return count


s = Solution()
print(s.twoSum2([2, 7, 11, 15], 24))
print(s.twoSum2([1, 1, 1, 1], 1))
