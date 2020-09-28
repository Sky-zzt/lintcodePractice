class Solution:
    """
    @param height: A list of integer
    @return: The area of largest rectangle in the histogram

    )。维护一个单调递增栈，逐个将元素 push 到栈里。push 进去之前先把 >= 自己的元素 pop 出来。
    每次从栈中 pop 出一个数的时候，就找到了往左数比它小的第一个数（当前栈顶）和往右数比它小的第一个数（即将入栈的数），
    从而可以计算出这两个数中间的部分宽度 * 被pop出的数，就是以这个被pop出来的数为最低的那个直方向两边展开的最大矩阵面积。
    因为要计算两个数中间的宽度，因此放在 stack 里的是每个数的下标。
    """

    # 找出左右两边离他最近的最小值，每个位置i能形成的最大的矩形=heights(i) * ((i-leftnearminIndex)+(rightnearmin-i))
    # todo 和Trapping rain water 对比看
    # todo 下次想不起来就重写一遍吧  呵呵
    def largestRectangleArea(self, heights):
        # todo 左边和右边的离他最近的最大最小值  Monotonous stack
        leftmin, rightmin = self.MonotonousStack(heights + [0])  # todo 右边加个 0 好处理
        maxArea = 0
        ans = 0
        for i in range(len(heights)):
            ans = 0
            # if rightmin[i]==-1:
            #     ans+=heights[i]*(len(heights)-i)
            # if leftmin[i]==-1:
            #     ans+=heights[i]*(i+1)
            ans = heights[i] * ((i - leftmin[i]) + (rightmin[i] - i))  ## todo 这不就是 rightmin[i]-leftmin[i] 呵呵
            maxArea = max(maxArea, ans)

    # 不能处理相等的情况，想等的话，stack.append([3,3]) 这样做
    def MonotonousStack(self, heights):
        stack = []
        leftmin = [0] * len(heights)
        rightmin = [0] * len(heights)
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                rightmin[idx] = i
                if len(stack) > 0: leftmin[idx] = stack[-1]
            stack.append(i)
        while len(stack) > 0:
            idx = stack.pop()
            if len(stack) > 0: leftmin[idx] = stack[-1]
        # print(leftmin)
        # print(rightmin)
        return leftmin, rightmin

    def MonotonousStack1(self, heights):  # todo heights右边加个  0 或者其他好处理
        stack = []
        heights.append(-1)
        leftmin = [-1] * len(heights)
        rightmin = [1] * len(heights)
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                idx = stack.pop()
                rightmin[idx] = heights[i]
                if len(stack) > 0: leftmin[idx] = heights[stack[-1]]
            stack.append(i)
        print(leftmin)
        print(rightmin)
        return leftmin, rightmin


s = Solution()

s.MonotonousStack1([1, 2, 4])
