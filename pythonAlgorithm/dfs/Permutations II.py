class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if not nums: return [[]]
        nums=sorted(nums)
        s = set()
        res = []
        visited=[0]*len(nums)
        self.helper(res, nums, s, [],visited)
        return res

    def helper(self, res, nums, s, part,visited):
        if len(part) == len(nums):
            res.append(list(part))
            return
        for i in range(len(nums)):
            if  nums[i] in s:continue
            if i>0 and visited[i-1]==0 and nums[i-1]==nums[i]: continue # todo   nums[i] in s 不应该以and的形式放在这里，因为前后不似乎同一个逻辑
            visited[i]=1
            s.add(nums[i])
            part.append(nums[i])
            self.helper(res, nums, s, part,visited)
            part.pop()
            s.remove(nums[i])
            visited[i]=0

s=Solution()

print(s.permuteUnique([1, 1]))

class Solution1:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique(self, nums):
        res = []
        used = [False] * len(nums)
        path = []
        # 排序
        nums = sorted(nums)
        # dfs
        self.dfs(nums, used, path, res)
        return res
    def dfs(self, nums, used, path, res):
        # 叶子节点
        if len(path) == len(nums):
            res.append(path[:])
            return
        # 非叶节点
        for i in range(len(nums)):
            # 元素已访问过 或者 是重复元素
            if used[i] or (i > 0 and nums[i] == nums[i-1] and used[i-1]==False):
                continue
            # 在路径添加该节点，递归
            used[i] = True
            self.dfs(nums, used, path + [nums[i]], res)
            # 回溯
            used[i] = False

s=Solution1()

print(s.permuteUnique([1, 1]))