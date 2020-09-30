class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    # todo 这个跑不过去啊，超时了
    def winSum(self, nums, k):  # todo 这不是On, 是On^2 的,求最值也是On^2 的。而sliding win max 用的deque，是On的
        # write your code here
        i = 0
        j = i + k - 1  # TODO 记住这个写法  很好的
        sum = 0
        res = []
        while j < len(nums):
            for k in range(i, j + 1):
                sum += nums[k]
            res.append(sum)
            sum = 0
            i += 1
            j += 1
        return res


a = []
s = Solution()
print(s.winSum(a, 9007))
