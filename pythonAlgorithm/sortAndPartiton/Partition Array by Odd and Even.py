class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    分割一个整数数组，使得奇数在前偶数在后。

Example
样例1:

输入: [1,2,3,4]
输出: [1,3,2,4]
    """

    def partitionArray(self, nums):
        # write your code here
        self.partition(nums)
        # [1,2]

    def partition(self, nums, k=1):
        less = -1
        more = len(nums)
        cur = 0
        while cur < more:
            if nums[cur] % 2 == 0:
                less += 1
                self.swap(nums, less, cur)
                cur += 1
            elif nums[cur] % 2 == 1:
                more -= 1
                self.swap(nums, more, cur)
            # else:
            #     cur += 1

    def swap(self, arr, start, end):
        arr[start], arr[end] = arr[end], arr[start]
