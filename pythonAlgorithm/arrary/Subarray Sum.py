class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    给定一个整数数组，找到和为 0 的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置
    """

    def subarraySum(self, nums):
        # write your code here
        import sys
        res = []
        map = {0: -1}  # TODO 这种情况 你画一下  图就只到为啥  需要map = {0: -1}  前缀和的应用，如果两个位置的前缀和相等，那么
        globalMax, sum, minSum = -sys.maxsize, 0, 0
        for i in range(len(nums)):
            sum += nums[i]
            # globalMax = max(globalMax, sum - minSum)
            if sum in map:
                res.append(map.get(sum) + 1)
                res.append(i)
                return res
            minSum = min(minSum, sum)
            map.update({sum: i})
            print(map)
        return -1


s = Solution()

print(s.subarraySum([-3, 1, -4, 2, -3, 4]))
