class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
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
