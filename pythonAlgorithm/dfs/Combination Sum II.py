class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        candidates = sorted(list(candidates))
        results = []
        visited = [0] * len(candidates)
        self.dfs(candidates, target, 0, [], results, 0, visited)
        return results

    def dfs(self, candidates, target, start, combination, results, sum, visited):
        if target < sum:  # todo  出口  勿忘
            return
        if target == sum:
            return results.append(list(combination))
        for i in range(start, len(candidates)):
            if i > 0 and visited[i - 1] == 0 and candidates[i - 1] == candidates[i]: continue
            visited[i] = 1
            sum += candidates[i]
            combination.append(candidates[i])
            self.dfs(candidates, target, i + 1, combination, results, sum, visited)
            combination.pop()
            sum -= candidates[i]
            visited[i] = 0


s = Solution()
print(s.combinationSum2([1, 1, 1], 2))  # [[1,1]]todo how to understand

# todo 理解 深搜树递归图 有益身心
#     关于这个0，1，2
#   todo    1，1，1  ---- 1，2位置上的[1,1]为什么不算一组解，原因还是那个，你在把1 位置上的数0放进去的时候，0 位置上的没有放进去，所以，1，2，不会是解
