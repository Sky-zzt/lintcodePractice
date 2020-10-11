class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer

    给出一个都是正整数的数组 nums，其中没有重复的数。从中找出所有的和为 target 的组合个数。

        Example
        样例1

        输入: nums = [1, 2, 4] 和 target = 4
        输出: 6
        解释:
        可能的所有组合有：
        [1, 1, 1, 1]
        [1, 1, 2]
        [1, 2, 1]
        [2, 1, 1]
        [2, 2]
        [4]
    """

    # 如何求出一种具体方案呢
    def backPackVI(self, nums, target):
        # write your code here
        l = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for j in range(l):
                if i>=nums[j]:
                    f[i] += f[i - nums[j]]
        return f[target]
s=Solution()
print(s.backPackVI([1, 2, 4], 4))
