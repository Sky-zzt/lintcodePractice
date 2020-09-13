class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if matrix[mid][n - 1] < target:
                start = mid
            elif matrix[mid][n - 1] > target:
                end = mid
            elif matrix[mid][n - 1] == target:
                return True
        if matrix[start][n - 1] >= target: # todo 是>= do not forget
            return self.bs(matrix[start], target)
        else:
            return self.bs(matrix[end], target)

    def bs(self, nums, target):
        # write your code here
        if not nums: return False
        l = len(nums)
        start = 0
        # todo need to l-1  or line 35 will be wrong
        end = l - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        return False

s=Solution()
s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],7)
