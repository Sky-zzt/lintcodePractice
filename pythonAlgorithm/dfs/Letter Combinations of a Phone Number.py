class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations

    给一个不包含0和1的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。

下图的手机按键图，就表示了每个数字可以代表的字母。
输入: "23"
输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
解释:
'2' 可以是 'a', 'b' 或 'c'
'3' 可以是 'd', 'e' 或 'f'
    """
    PHONE = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        # write your code here
        pass

    def dfs(self, digits, count, res, ans):
        if len(ans) == len(digits):
            res.extend(ans)
            return
        for i in range(len(digits)):
            if digits[i] in self.PHONE:
                ans=ans+digits
                self.dfs(digits,count,res,ans)
                ans.pop()



s="sdsds"
s=s+"111"
# s.
# print(s)