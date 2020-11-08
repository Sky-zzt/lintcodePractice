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

暴力解法时间复杂度较高，会达到 On3
，故而采取滑动窗口的方法降低时间复杂度。

我们使用两个指针表示字符串中的某个子串的左右边界。每步操作中，右指针向右移动一位，然后不断移动左指针，直到这两个指针对应的子串中没有重复的字符。在移动结束后，这个子串就对应着以右指针结束的，不包含重复字符的最长子串。我们记录下这个子串的长度。

在枚举结束后，我们找到的最长的子串的长度即为答案。
    """

    def lengthOfLongestSubstring(self, s):
        # write your code here
        pass
