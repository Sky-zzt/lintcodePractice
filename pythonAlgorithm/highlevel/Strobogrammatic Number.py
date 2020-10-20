class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    一个镜像数字是指一个数字旋转180度以后和原来一样(倒着看)。例如，数字"69"，"88"，和"818"都是镜像数字。
写下一个函数来判断是否这个数字是镜像的。数字用字符串来表示。

Example
样例1:

输入 : "69"
输出 : true
样例 2:

输入 : "68"
输出 : false
    """

    # todo 将倒过来能看成数字的数字哈希一下，就能进行转换判断了。
    def isStrobogrammatic(self, num):
        # write your code here
        map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}  # 镜像数字要么是左右对称的 要么就是69这种，所以用相向双指针
        i, j = 0, len(num) - 1
        while i <= j:
            if not num[i] in map or map[num[i]] != num[j]:
                return False
            i, j = i + 1, j - 1
        return True


s = '122'
