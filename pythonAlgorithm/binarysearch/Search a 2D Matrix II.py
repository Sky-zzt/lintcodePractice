class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or len(matrix) == 0: return 0
        if not matrix[0] or len(matrix) == 0: return 0

        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m - 1
        count = 0
        x = 0
        y = n - 1
        while x < m and 0 <= y:
            if target > matrix[x][y]:
                x += 1
            elif target < matrix[x][y]:
                y -= 1
            elif target == matrix[x][y]:
                count += 1
                x += 1
                y -= 1
        return count
