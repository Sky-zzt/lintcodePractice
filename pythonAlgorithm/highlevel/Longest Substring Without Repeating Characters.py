class Solution:
    """
    @param s: a string
    @return: an integer
    给定一个字符串，请找出其中无重复字符的最长子字符串。

Example
样例 1:

输入: "abcabcbb"
输出: 3
解释: 最长子串是 "abc".
样例 2:

输入: "bbbbb"
输出: 1
解释: 最长子串是 "b".
Challenge
O(n) 时间复杂度
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        # todo 还是 窗口类指针移动模板 本质是找一个窗口
        m = len(s)
        j = 0
        longest = 0x80000000  # https://www.runoob.com/w3cnote/python-negative-storage.html
        unique_char = set()
        for i in range(m):
            while j < m and s[j] not in unique_char:
                unique_char.add(s[j])
                j += 1
            longest = max(j - i, longest)
            unique_char.discard(s[i])
        return longest


print(0x8000000)
