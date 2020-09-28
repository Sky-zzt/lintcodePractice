class Solution:
    """
    @param nums:
    @return: Find the maxmum range value. A range value is defined as the minimum value times the sum of all values in a range.

  给定一个非负数的整数数组，需要选出一个区间, 使得该区间是所有区间中值最大的一个，我们定义一个区间的值为：区间中的最小数 * 区间所有数的和。
    """

    # todo  吐血了 ，花了一个小时写了一个枚举区间长度为1,2,3的长须，差点每写出来，你能信
    def maxRange1(self, nums):
        # write your code here
        res = []

        for l in range(1, len(nums) + 1):
            i, j = 0, 0
            j = i + l

            while j <= len(nums):
                ans = []
                for k in range(i, j):
                    ans.append(nums[k])
                i += 1
                j += 1
                res.append(ans)
        return res

    def maxRange2(self, nums):  # 区间dp的求每个区间的方法，呵呵
        l = len(nums)
        for length in range(l):
            for i in range(l - length + 1):
                j = i + length - 1

    def maxRange(self, nums):
        pass


s = Solution()
print(s.maxRange1([6, 2, 1]))
