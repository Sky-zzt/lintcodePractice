class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        return self.binarySearch(nums, target, 0, len(nums))

    def binarySearch(self, nums, target, start, end):
        mid = (start + end) // 2
        while start+1<end: #todo <=才行
            if nums[mid] == target: return mid
            if nums[mid] < target:
                return  self.binarySearch(nums, target, mid + 1, end)  #todo 必须加1 ，不然，死循环 你输入一个[2],4试试
            if nums[mid] > target:
                return  self.binarySearch(nums, target, start, mid - 1)
        return -1
    def bs(self,nums, target):
        # write your code here
        if not nums:return -1
        l=len(nums)
        start=0
        # todo need to l-1  or line 35 will be wrong
        end=l-1
        while start+1<end:
            mid=(start+end)//2
            if nums[mid]==target:return mid
            elif nums[mid]<target:start=mid
            elif nums[mid]>target:end=mid
        if nums[start]==target:
            return start
        if nums[end]==target:
            return end
        return -1



