class Solution:
    """
    @param nums: the given array
    @param limit: the limit on the absolute difference of the subarray
    @return: Find the number of triplet subarray with the absolute difference less than or equal to limit
    给定一个递增的整数数组nums，和一个表示限制的整数limit，请你返回满足条件的三元子数组的个数，使得该子数组中的任意两个元素之间的绝对差小于或者等于limit。

如果不存在满足条件的子数组，则返回 0 。

Example
样例 1:

输入：[1, 2, 3, 4], 3
输出：4
解释：可选方案有(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)。因此，满足条件的三元组有4个。
样例 2:

输入：[1, 10, 20, 30, 50], 19
输出：1
解释：唯一可行的三元组是(1, 10, 20)，所以答案为1。
Challenge
你可以只用O(n)的时间复杂度解决这个问题吗？

Notice
数据范围：1 ≤ len(nums) ≤ 1e4，1 ≤ limit ≤ 1e6，0 ≤ nums[i] ≤ 1e6
由于答案可能很大，请返回它对99997867取余后的结果。

使用双指针。初始化左指针left为0，右指针right为2。每次右指针移动一位，指向三元组中最后一位元素，
左指针向右移动到满足nums[right]-nums[left]<=limit为止。如果right-left>=2，
说明可以构成三元组，从nums[left, right-1]这个区间中任挑两位作为三元组的前两个元素，有c(n,2)种选择。
直到右指针遍历到最后一个元素为止。由于左右指针都只遍历了一次，所以时间复杂度为O(n)，空间复杂度为O(1)。
    """
    def tripletSubarray(self, nums, limit):
        # write your code here
        left = 0
        res = 0
        mod = 99997867
        for right in range(2, len(nums)):
            while nums[right] - nums[left] > limit:
                left += 1
            if right - left >= 2:
                res += (right - left) * (right - left - 1) // 2
        return res % mod