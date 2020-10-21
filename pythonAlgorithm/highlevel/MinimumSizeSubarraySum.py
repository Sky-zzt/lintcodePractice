class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    给定一个由 n 个正整数组成的数组和一个正整数 s ，请找出该数组中满足其和 ≥ s 的最小长度子数组。如果无解，则返回 -1。

Example
样例 1:

输入: [2,3,1,2,4,3], s = 7
输出: 2
解释: 子数组 [4,3] 是该条件下的最小长度子数组。
样例 2:

输入: [1, 2, 3, 4, 5], s = 100
输出: -1
Challenge
如果你已经完成了O(nlogn)时间复杂度的编程，请再试试 O(n)时间复杂度。

    """

    # todo 窗口类指针移动模板 本质是找一个窗口 然后这个窗口满足某种条件 都可以这么做 呵呵
    def minimumSize(self, nums, s):
        # write your code here
        m = len(nums)
        sum = 0
        j = 0
        ans = 0x7fffffff
        for i in range(m):
            while j < m and sum < s:
                sum += nums[j]
                j += 1
            if sum >= s:
                ans = min(ans, j - i)
            sum -= nums[i]

        if ans == 0x7fffffff:
            ans = -1
        return ans


s = Solution()
print(s.minimumSize([2, 3, 1, 2, 4, 3], 7))
