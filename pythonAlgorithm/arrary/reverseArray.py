class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """

    def reverseArray(self, nums):
        # write your code here
        end = len(nums)
        start = 0
        self.reverse(nums, start, end - 1)
        return nums

    def reverse(self, nums, start, end):
        # write your code here
        # todo 这里是 if 不是 while start<end:
        if start < end:
            self.swap(nums, start, end)
            self.reverse(nums, start + 1, end - 1)
        return nums

    def swap(self, arr, start, end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

    def reverseArray2(self, nums):
        # write your code here
        end = len(nums) - 1
        start = 0
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
        return nums


s = Solution()
print(s.reverseArray([1, 2, 3]))
