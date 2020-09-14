class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        # write your code here

        if not A: return
        self.mergesort(A, 0, len(A) - 1)

    def mergesort(self, arr, left, right):
        mid = (left + right) // 2
        if left < right:
            self.mergesort(arr, left, mid)
            self.mergesort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        helper = []
        l = left
        r = mid + 1
        while l <= mid and r <= right:
            if arr[l] > arr[r]:
                helper.append(arr[r])
                r += 1
            else:
                helper.append(arr[l])
                l += 1
        while l <= mid:  # todo is <=
            helper.append(arr[l])
            l += 1
        while r <= right:
            helper.append(arr[r])
            r += 1
        for i in range(len(helper)):
            arr[left + i] = helper[i]  # todo is left+i not l+i


s = Solution()
a = [2, 4, 1, 7, 1, 9, 0, 4]
c = [7, 8, 9, 1, 2, 3, 10]
s.merge(c, 0, 2, 6)
print(c)
print(s.sortIntegers(a))
print(a)
