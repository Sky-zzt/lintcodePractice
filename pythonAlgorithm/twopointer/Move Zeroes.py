class Solution:
    """
    @param nums: an integer array
    @return: nothing
    给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

Example
例1:

输入: nums = [0, 1, 0, 3, 12],
输出: [1, 3, 12, 0, 0].
    """
        # 双指针。思想很简单
    '''
               i
    [-1,2,-3,4,0,1,0,-2,0,0,1]
                 j
    '''
    def moveZeroes(self, nums):
        # write your code here
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            if nums[i] == 0 and nums[j] != 0 and j > i: #
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            if  i<len(nums) and nums[i] != 0:# todo i<len(nums)  这个数组判越界 很重要啊
                i += 1
            if j < len(nums) and nums[j] == 0:
                j += 1
            if i > j:  # todo  这个主要是防止下面这种，j不动了就 ，23 行又进不去，然后死循环
                j += 1

s=Solution()
s.moveZeroes([-1,2,-3,4,0,1,0,-2,0,0,1])