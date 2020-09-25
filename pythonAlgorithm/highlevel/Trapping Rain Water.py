class Solution:
    """
    @param heights: a list of integers
    @return: a integer


    每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度

从左到右扫描一边数组，获得每个位置往左这一段的最大值，再从右到左扫描一次获得每个位置向右的最大值。 然后最后再扫描一次数组，计算每个位置上的盛水数目。

时间复杂度 On 空间复杂度 On

    """

    # [0,1,0,2,1,0,1,3,2,1,2,1]
    # todo 如果是二维数组的话，和这个思路相仿，求出每个位置上下左右的最大最小值，可以用我的这个方法，也可以把周围元素全部放进heap里
    def trapRainWater(self, heights):
        # write your code here
        left = [0] * len(heights)
        right = [0] * len(heights)
        res = 0
        maxsimum = 0
        for i in range(len(heights)):
            if i > 0: maxsimum = max(heights[i - 1], maxsimum)
            left[i] = maxsimum
        maxsimum = 0
        for i in range(len(heights) - 1, -1, -1):
            if i < len(heights) - 1: maxsimum = max(heights[i + 1], maxsimum)
            right[i] = maxsimum
        print(left)
        print(right)
        for i in range(len(heights)):
            minimum = min(left[i], right[i]) - heights[i]
            if minimum > 0:  # todo  勿忘
                res += minimum
        return res

    # 双指针 同时求左边和右边最大值
    def trapRainWater2(self, heights):
        i = 0
        j = len(heights) - 1
        left = [0] * len(heights)
        right = [0] * len(heights)
        maxLeft = 0
        maxRight = 0
        while i < len(heights) or j >= 0:
            if i > 0: maxLeft = max(heights[i - 1], maxLeft)
            left[i] = maxLeft
            i += 1
            if j < len(heights) - 1: maxRight = max(heights[j + 1], maxRight)
            right[j] = maxRight
            j -= 1
        print(left)
        print(right)


s = Solution()
print(s.trapRainWater2([1, 3, 2, 0, 4]))
print(s.trapRainWater([1, 3, 2, 0, 4]))
