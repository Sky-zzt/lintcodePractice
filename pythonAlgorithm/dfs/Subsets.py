class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # write your code here
        if not nums: return [[]]
        nums = sorted(nums)
        res = []
        self.helper(res, [], nums, 0)
        return res

    def helper(self, res, part, nums, pos):
        res.append(list(part))
        for i in range(pos, len(nums)):
            part.append(nums[i])
            self.helper(res, part, nums, i + 1)
            part.pop()

s=Solution()

print(s.subsets([1]))
