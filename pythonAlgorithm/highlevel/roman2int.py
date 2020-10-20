class Solution:
    """
    @param s: Roman representation
    @return: an integer

    思路很简单，就是指针从左往右移动。 遇到5 = IV这样的，我们可以理解为左边i比右边i+1小的，i那一位为负数。
    也就是IV = -1 + 5 = 4， IX = -1 + 10 = 9 令hash为罗马字到数字的map： 整个s 从左往右读取，
    if hash si < hash si+1, ans -= hash si. else ans += hash si

当i 到最后了， i+1 越界了，这里我们可以给s加一个零的尾巴。这样无论s最后是啥字母，肯定比0都大。
    """

    def romanToInt(self, s):

        convert = {'0': 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        s += '0'
        ans = 0
        for i in range(len(s) - 1):
            if convert[s[i]] < convert[s[i + 1]]:
                ans -= convert[s[i]]
            else:
                ans += convert[s[i]]

        return ans
