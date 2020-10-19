class Solution:
    """
    @param str: The string before proofreading.
    @return: Return the string after proofreading.
    有一些单词中有拼写错误，请编写一个程序，能够自动校对单词的拼写，并且返回正确值。
校对的规则如下：

如果有三个相同的字符连在一起，一定是拼写错误，去掉其中一个，如：ooops -> oopsooops−>oops。
如果有两对一样的字符(AABB的形式)连在一起,，一定是拼写错误，去掉第二对中的一个字符，如：helloo -> hellohelloo−>hello。
以上两条规则要优先从左往右处理，如：aabbccaabbcc 中 aabbaabb 和 bbccbbcc 都是拼写错误，应该优先考虑修复aabbaabb，结果是aabccaabcc。
Example
样例输入 1:
str = "helloo"

样例输出 1:
"hello"

"lloo" 拼写错误，去掉一个'o'。

样例输入 2:
str = "woooow"

样例输出 2:
"woow"

"oooo"拼写错误，先删去一个'o'，"ooo"还是拼写错误，再删去一个'o'。
Notice
输入字符串的长度为 nn，1 <= n <= 10^51<=n<=10
​5
​​ 。
字符串均由小写字符组成。
https://www.jiuzhang.com/solution/automatic-proofreading-program/
    """
    # todo stack
    def automaticProofreadingProgram(self, str):
        # Write your code here.
        pass