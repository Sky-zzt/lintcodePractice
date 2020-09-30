class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays

            //分割线左向有扫描一遍 右向左扫描一遍  不重叠意味着有分割线
        //给定一个整数数组，找出两个 不重叠 子数组使得它们的和最大。
        //每个子数组的数字在数组中的位置应该是连续的。
        //返回最大的和
    """

    def maxTwoSubArrays(self, nums):
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


s = Solution()

print(s.maxTwoSubArrays([1, 3, -1, 2, -1, 2]))
