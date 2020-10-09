class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing

    给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

Example
样例 1

输入 : [1, 0, 1, 2]
输出 : [0, 1, 1, 2]
解释 : 原地排序。
    """

    def sortColors(self, nums):
        # write your code here
        self.partition(nums)

    def partition(self, nums, k=1):
        less = -1
        more = len(nums)
        cur = 0
        while cur < more:
            if nums[cur] < k:
                less += 1
                self.swap(nums, less, cur)
                cur += 1
            elif nums[cur] > k:
                more -= 1
                self.swap(nums, more, cur)
            else:
                cur += 1

    def swap(self, arr, start, end):
        arr[start], arr[end] = arr[end], arr[start]
