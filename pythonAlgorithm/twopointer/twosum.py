class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here

        numbers = sorted(numbers)
        i, j = 0, len(numbers) - 1
        while i < j:
            if target == numbers[i] + numbers[j]:
                return [i, j]
            if target > numbers[i] + numbers[j]:
                i += 1
            if target < numbers[i] + numbers[j]:
                j -= 1
        return -1


s = Solution()
print(s.twoSum([1, 0, -1], 1))
