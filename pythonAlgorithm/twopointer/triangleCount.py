class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        S = sorted(S)
        #  小--->大   a,b,c   a+b>c <=> a.b,c 可以组成三角形
        l = 0
        r = len(S) - 2
        count = 0
        while r >= 1:
            if l < r and S[l] + S[r] > S[r + 1]:
                count += 1
                l += 1
            else:
                l = 0
                r -= 1
        return count

    # TODO 这个答案很好  我上面那个 荣誉计算太多，而且 没法对付 [4,4,4,4]这种case  do it again
    def triangleCOunt2(self, S):
        res = 0
        # 先对S进行排序
        S = sorted(S)
        # 最大边从右向左遍历
        for i in range(len(S) - 1, 1, -1):
            # 建立双指针
            left = 0
            right = i - 1
            while (left < right):
                # 可以构成三角形
                if S[left] + S[right] > S[i]:
                    res += right - left  # 这步 很妙啊
                    right -= 1
                # 不能构成三角形
                else:
                    left += 1
        return res


s = Solution()
print(s.triangleCOunt2([4, 4, 4, 4]))
for i in range(5, 1, -1):
    print(i)
