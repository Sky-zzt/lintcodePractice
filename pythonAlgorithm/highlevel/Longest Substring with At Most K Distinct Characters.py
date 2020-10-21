class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer

    给定字符串S，找到最多有k个不同字符的最长子串T。

Example
样例 1:

输入: S = "eceba" 并且 k = 3
输出: 4
解释: T = "eceb"
样例 2:

输入: S = "WORLD" 并且 k = 4
输出: 4
解释: T = "WORL" 或 "ORLD"
Challenge
O(n) 时间复杂度


 窗口类
• Remove Nth Node From End of List
• minimum-size-subarray-sum
• Minimum Window Substring
• Longest Substring with At Most K Distinct Characters
• Longest Substring Without Repeating Characters
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        m = len(s)
        j = 0
        diff = 0
        arr = set()
        ans = 0
        for i in range(m):
            while j < m and diff < k:
                arr.add(s[j])
                diff = len(arr)
                j += 1
            ans = max(ans, j - i)
            arr.discard(s[i])
        return ans


s = Solution()
print(s.lengthOfLongestSubstringKDistinct("WORLD", 4))
