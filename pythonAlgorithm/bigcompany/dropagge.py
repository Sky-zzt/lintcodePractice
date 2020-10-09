class Solution:
    """
    @param n: An integer
    @return: An integer
    描述
楼有 n 层高，鸡蛋若从 k 层或以上扔，就会碎。从 k 层以下扔，就不会碎。

现在给两个鸡蛋，用最少的扔的次数找到 k。返回最坏情况下次数。

样例
样例 1：

输入：100
输出：14
样例 2：

输入：10
输出：4
说明
对于 n = 10， 一种找 k 的初级方法是从 1、2 ... k 层不断找。但最坏情况下要扔 10 次。

注意有两个鸡蛋可以使用，所以可以从 4、7、9 层扔。这样最坏就只需要 4 次 (例如 k = 9 时)。
https://www.jiuzhang.com/solution/drop-eggs/
    """

    def dropEggs(self, n):
        # write your code here
        pass