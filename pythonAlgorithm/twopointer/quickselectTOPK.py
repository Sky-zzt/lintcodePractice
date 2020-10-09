class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        pass

    def quickselect(self, nums, l, r, n):
        import random
        p = self.partition(nums, l, r, nums[l + int(random.random() * (l - r + 1))])
        if l + n < p[0]:
            self.quickselect(nums, l, p[0], n)
        elif l + n > p[1]:
            self.quickselect(nums, p[1], r, n - p[0] + l)
        return nums[p[0] + 1]

    def partition(self, arr, left, right, target):
        less = left - 1
        more = right + 1
        while left < more:
            if arr[left] < target:
                less += 1
                swap(arr, left, less)
                left += 1
            elif arr[left] > target:
                more -= 1
                swap(arr, left, more)
            else:
                left += 1
        return less + 1, more - 1


def swap(arr, start, end):
    arr[start], arr[end] = arr[end], arr[start]
