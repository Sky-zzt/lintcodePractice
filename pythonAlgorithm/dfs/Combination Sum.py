class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        if not candidates: return [[]]
        nums = sorted(candidates)
        res = []
        visited = [0] * len(nums)
        self.helper(res, [], 0, target, nums, 0, visited)
        return res

    def helper(self, res, part, sum, target, candidates, pos, visited):
        if sum == target:
            res.append(list(part))
            return
        for i in range(pos, len(candidates)):
            sum += candidates[i]
            part.append(candidates[i])
            self.helper(res, part, sum, target, candidates, i, visited)
            part.pop()  # todo 这个的问题就在于没有 sum -= candidates[i]

    def combinationSum(self, candidates, target):
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, 0, [], results,0)
        return results

    def dfs(self, candidates, target, start, combination, results,sum):
        if target < sum: #todo  出口  勿忘
            return
        if target == sum:
            return results.append(list(combination))
        for i in range(start, len(candidates)):
            sum+=candidates[i]
            combination.append(candidates[i])
            self.dfs(candidates, target, i, combination, results,sum)
            combination.pop()
            sum -= candidates[i]


s=Solution()
print(s.combinationSum([1, 2, 3], 5))