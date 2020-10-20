class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    以字符串的形式给出两个非负整数 num1 和 num2，返回 num1 和 num2 的和。

Example
样例 1:

输入 : num1 = "123", num2 = "45"
输出 : "168"
Notice
num1 和 num2 的长度都小于5100。
num1 和 num2 都只包含数字 0-9。
num1 和 num2 都不包含任何前导零。
您不能使用任何内置的BigInteger库内的方法或直接将输入转换为整数。
https://blog.csdn.net/csdnsevenn/article/details/84753109?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.add_param_isCf&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.add_param_isCf
    """

    def addStrings(self, nums1, nums2):
        # write your code here
        max_len = max(len(nums1), len(nums2))
        nums1 = list(nums1)[:: -1]
        nums2 = list(nums2)[:: -1]
        nums3 = [0 for i in range(max_len)]
        # Add
        id_ = 0
        while id_ < max_len:
            num1 = int(nums1[id_]) if id_ < len(nums1) else 0
            num2 = int(nums2[id_]) if id_ < len(nums2) else 0
            nums3[id_] = num1 + num2
            id_ += 1
        # Carry
        for i in range(len(nums3) - 1):
            if nums3[i] > 9:
                nums3[i + 1] += nums3[i] // 10
                nums3[i] %= 10
        # Deal with the last digit
        if nums3[-1] > 9:
            nums3 += [nums3[-1] // 10]
            nums3[-2] %= 10

        return ''.join(str(x) for x in nums3[:: -1])
