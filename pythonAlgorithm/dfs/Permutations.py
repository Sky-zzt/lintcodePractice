class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        # write your code here
        if not nums: return [[]]
        s = set()
        res = []
        self.helper(res, nums, s, [])
        return res

    def helper(self, res, nums, s, part):
        if len(part) == len(nums):
            res.append(list(part))
            return
        for i in range(len(nums)):
            if nums[i] in s: continue
            s.add(nums[i])
            part.append(nums[i])
            self.helper(res, nums, s, part)
            part.pop()
            s.remove(nums[i])

s=Solution()
s.permute([1,2,3])