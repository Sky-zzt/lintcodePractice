class Solution:
    def MonotonousStack(self, heights):
        stack = []
        leftmin = [-1] * len(heights)
        rightmin = [-1] * len(heights)
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                rightmin[idx] = i
                if len(stack) > 0: leftmin[idx] = stack[-1]
            stack.append(i)
        while len(stack) > 0:
            idx = stack.pop()
            if len(stack) > 0: leftmin[idx] = stack[-1]
        print(leftmin)
        print(rightmin)
        return leftmin, rightmin


s = Solution()
s.MonotonousStack([0, 2, 1, 5, 6, 2, 3, 0])
#  0  1  2  3  4  5  6  7
