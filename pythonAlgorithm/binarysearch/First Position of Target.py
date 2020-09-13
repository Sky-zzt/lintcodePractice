class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if not nums:return -1
        l=len(nums)
        start=0
        # todo need to l-1  or line 35 will be wrong
        end=l-1
        while start+1<end:
            mid=(start+end)//2
            if nums[mid]==target:end=mid
            elif nums[mid]<target:start=mid
            elif nums[mid]>target:end=mid
        if nums[start]==target:
            return start
        if nums[end]==target:
            return end
        return -1
