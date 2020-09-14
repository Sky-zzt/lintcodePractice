class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers(self, A):
        # write your code here

        if not A: return
        # for i in range(len(A)):
        self.heapInsert(A)
        print(A)
        size = len(A)
        while size > 0:
            size -= 1
            self.swap(A, 0, size)
            self.heapfiy(A, 0, size)

    def heapInsert(self, A):
        if not A: return
        for i in range(len(A)):  # todo Very important py -1//2==-1, java -1/2=0  so in sum case  use round(num) instead
            while A[round((i - 1) / 2)] < A[i]:
                self.swap(A, i, round((i - 1) / 2))
                i = round((i - 1) / 2)
                # print(i)

    # todo remeber it
    def heapfiy(self, arr, index, heapsize):
        left = index * 2 + 1
        while left < heapsize:
            largetst = left + 1 if left + 1 < heapsize and arr[left + 1] > arr[left] else left
            largetst = largetst if arr[largetst] > arr[index] else index
            if largetst == index: break
            self.swap(arr, largetst, index)
            index = largetst
            left = index * 2 + 1

    # TODO 有问题，A,0,0 交换有问题
    def swap(self, arr, i, j):
        arr[i] = arr[i] ^ arr[j]
        arr[j] = arr[i] ^ arr[j]
        arr[i] = arr[i] ^ arr[j]


s = Solution()
a = [4, 1]
s.sortIntegers(a)
# s.heapInsert(a)
print(a)
# print("dddddd")
# print(round((0-1)/2))
# import math
