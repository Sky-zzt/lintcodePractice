'''

给定两个字符串 S 和 T, 判断T是否可以通过对S做刚好一次编辑得到。
每次编辑可以选择以下任意一个操作：

在S的任意位置插入一个字符
删除S中的任意一个字符
将S中的任意字符替换成其他字符


算法：模拟

根据题意，我们只能对字符串操作一次

那么我们根据情况可以分为三种情况：

两个字符串的长度之差 大于1
 直接返回false
长度之差等于1， 判断长的字符串删掉不一样的字符，剩余的字符串是否相同
长度之差等于0
，判断不相同的字符个数，若超过一个返回false。
复杂度分析

时间复杂度O(n)
n为两个字符串中较长的串
空间复杂度O(1)
无需额外空间
'''


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """

    def isOneEditDistance(self, s, t):
        if len(s) > len(t):  # 保证t比s长
            tmp = s
            s = t
            t = tmp
        diff = len(t) - len(s)
        if diff == 1:  # 长度差一个的情况
            for i in range(0, len(s)):
                if t[i] != s[i]:
                    # t去掉索引为i的字符之后剩余的子串和s是否相同
                    return s[i:] == t[i + 1:]
            return True
        if diff == 0:  # 长度相同的情况
            cnt = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
            return cnt == 1
        return False
