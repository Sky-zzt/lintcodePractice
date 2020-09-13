class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        # write your code here
        if not A and A is not None:
            self.mergesort(A, 0, len(A) - 1)

    def mergesort(self, arr, left, right):
        mid = (left + right) // 2
        if True:
            self.mergesort(arr, left, mid)
            self.mergesort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        helper = []
        l = left
        r = mid
        while l <= mid and r <= right:
            if arr[l] > arr[r]:
                helper.append(arr[r])
                r += 1
            else:
                helper.append(arr[l])
                l += 1
        while l < mid:
            l += 1
            helper.append(arr[l])
        while r < right:
            r += 1
            helper.append(arr[r])

        for i in range(len(arr)):
            arr[i] = helper[i]
a=[1,3]

