class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer

    给一整数数组, 找到数组中有多少组 不同的元素对 有相同的和, 且和为给出的 target 值, 返回对数.


    这个题  不能先去重 
    """

    def twosum(self, numbers, target):
        res = ()
        s = set()

        hashmap = {}
        for i in range(len(numbers)):
            if target - numbers[i] in hashmap:
                if (numbers[i], target - numbers[i]) not in s: s.add((target - numbers[i], numbers[i]))
            hashmap.update({numbers[i]: i})
        return len(s)


s = Solution()
print(s.twosum(numbers=[107, 0, 107, 0, 107, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 107, 107, 106, 1, 1, 9, 98, 9, 97,
                        11, 1001, 2001, -91, 201, 203, 201, 999, 345, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4,
                        5, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 101, 1, 1, 1, 1, 1, 1, 1, 1], target=107))
