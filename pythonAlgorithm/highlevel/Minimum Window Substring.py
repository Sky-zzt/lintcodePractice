class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string

    给定两个字符串 source 和 target. 求 source 中最短的包含 target 中每一个字符的子串.

Example
样例 1:

输入: source = "abc", target = "ac"
输出: "abc"
样例 2:

输入: source = "adobecodebanc", target = "abc"
输出: "banc"
解释: "banc" 是 source 的包含 target 的每一个字符的最短的子串.
样例 3:

输入: source = "abc", target = "aa"
输出: ""
解释: 没有子串包含两个 'a'.
Challenge
O(n) 时间复杂度

Notice
如果没有答案, 返回 "".
保证答案是唯一的.
target 可能包含重复的字符, 而你的答案需要包含至少相同数量的该字符.
    """

    def minWindow(self, source, target):
        # write your code here

        m = len(source)
        j = 0
        ans = 0x7fffffff
        for i in range(m):
            while j < m and target not in source[i:j]:
                j += 1
            ans = min(ans, j - i)

        if ans == 0x7fffffff:
            ans = ''
        return ans

    def isContain(self):
        pass
