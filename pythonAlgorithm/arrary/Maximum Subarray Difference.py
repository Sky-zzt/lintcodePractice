class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings

    给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。
    """

    # TODO dp。 维护四个数组，当前位置左边的最大子数组和，最小子数组和。当前位置右边的最大子数组和，最小子数组和。 然后枚举分割线，扫描一下即可
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums: return 0
        import sys
        leftmax, minsum, sum = -sys.maxsize, 0, 0
        leftmaxlist = []

        for i in range(len(nums)):
            sum += nums[i]
            leftmax = max(leftmax, sum - minsum)
            leftmaxlist.append(leftmax)
            minsum = min(minsum, sum)

        print(leftmaxlist)
        rightmax, minsum, sum = -sys.maxsize, 0, 0
        rightmaxlist = []

        for i in range(len(nums) - 1, -1, -1):
            sum += nums[i]
            rightmax = max(rightmax, sum - minsum)
            rightmaxlist.append(rightmax)
            minsum = min(minsum, sum)

        print(rightmaxlist)
        globalmax = -sys.maxsize
        rightmaxlist = rightmaxlist[::-1]  # todo 这个题trick 比较多，比如这里应该翻转一下，
        for i in range(0, len(
                nums) - 1):  # 遍历分割线（为了应对[5,4]这种情况，不要从分割的角度看，要割也是从每个数的头上割）  range应该从 0 开始比较好  [5,4] 这种情况只有 从0开始才行
            globalmax = max(globalmax, leftmaxlist[i] + rightmaxlist[i + 1])
        return globalmax
