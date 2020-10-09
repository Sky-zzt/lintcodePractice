class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    给出一个含有正整数和负整数的数组，重新排列成一个正负数交错的数组。

Example
样例 1

输入 : [-1, -2, -3, 4, 5, 6]
输出 : [-1, 5, -2, 4, -3, 6]
解释 : 或者仍和满足条件的答案

先partition 分成前面为负数，后面为正数
然后两根指针，首先判断正数多还是负数多，并把多的那一部分移到后半部分，最后两根指针分别递增二交换即可
    """

    def rerange(self, A):
        # write your code here
        pass

    index = 1
    index += 2
