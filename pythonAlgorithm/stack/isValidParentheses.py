'''

给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]" 则是无效的括号。

样例
样例 1：

输入："([)]"
输出：False
样例 2：

输入："()[]{}"
输出：True
'''
class Solution(object):
    '''
    题意：输入一个只包含括号的字符串，判断括号是否匹配
    模拟堆栈，读到左括号压栈，读到右括号判断栈顶括号是否匹配
    '''
    def isValidParentheses(self, s):
        stack = []
        for ch in s:
            # 压栈
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            else:
                # 栈需非空
                if not stack:
                    return False
                # 判断栈顶是否匹配
                if ch == ']' and stack[-1] != '[' or ch == ')' and stack[-1] != '(' or ch == '}' and stack[-1] != '{':
                    return False
                # 弹栈
                stack.pop()
        return not stack