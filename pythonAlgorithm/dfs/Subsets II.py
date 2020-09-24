class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """

    def subsetsWithDup(self, nums):
        # write your code here
        if not nums: return [[]]
        nums = sorted(nums)
        res = []
        self.helper(res, [], nums, 0)
        return res

    def helper(self, res, part, nums, pos):
        res.append(list(part))
        for i in range(pos, len(nums)):
            # todo
            if i != pos and nums[i] == nums[i - 1]: continue
            part.append(nums[i])
            self.helper(res, part, nums, i + 1)
            part.pop()


    def subsetsWithDup(self, nums):
        # write your code here
        if not nums: return [[]]
        nums = sorted(nums)
        res = []
        visited=[0]*len(nums)
        self.helper(res, [], nums, 0,visited)
        return res

    def helper(self, res, part, nums, pos,visited):
        res.append(list(part))
        for i in range(pos, len(nums)):
            # todo
            if i>0 and visited[i - 1] == 0 and nums[i] == nums[i - 1]: continue
            visited[i] = 1
            part.append(nums[i])
            self.helper(res, part, nums, i + 1,visited)
            part.pop()
            visited[i]=0
s=Solution()
s.subsetsWithDup([])