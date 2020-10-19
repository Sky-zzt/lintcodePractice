class Solution:
    """
    @param height: the Building height
    @return: The minimum unit of initial energy required to complete the game

    机器人正在玩一个古老的基于DOS的游戏。游戏中有N+1座建筑——从0到N编号，从左到右排列。编号为0的建筑高度为0个单位，编号为i的建筑的高度为H(i)个单位。
起初， 机器人在编号为0的建筑处。每一步，它跳到下一个（右边）建筑。假设机器人在第k个建筑，且它现在的能量值是E, 下一步它将跳到第个k+1建筑。它将会得到或者失去正比于与H(k+1)与E之差的能量。如果 H(k+1) > E 那么机器人就失去 H(k+1) - E 的能量值，否则它将得到 E - H(k+1) 的能量值。
游戏目标是到达第个N建筑，在这个过程中，能量值不能为负数个单位。现在的问题是机器人以多少能量值开始游戏，才可以保证成功完成游戏？

Example
例 1:

输入:
height:[3,4,3,2,4]
输出: 4
解释:
初始能量为4才能从0走到4
Notice
1 \leq height.size() \leq 10^51≤height.size()≤10
​5
​​
1 \leq height[i] \leq 10^51≤height[i]≤10
​5
​​
1。数学推导 Ek=2EK-1 -Hk
2.二分法
    """

    class Solution:
        """
        @param height: the Building height
        @return: The minimum unit of initial energy required to complete the game
        二分 由于在check中的判断会轻易的超出longlong的范围，故不建议用java，c++做
        每次我们对mid作为E0 遍历数组，判断在能量加减过程中会不会出现小于0的情况，由此判断区间的左右减小
        """

        def LeastEnergy(self, height):
            left, right = 0, max(height)
            while left < right:
                mid = int(left + (right - left) / 2)
                print(self.check(mid, height))
                if self.check(mid, height):
                    right = mid
                else:
                    left = mid + 1
            return left

        def check(self, power, height):
            for i in range(len(height)):
                if power > height[i]:
                    power += power - height[i]
                else:
                    power -= height[i] - power
                if power < 0:
                    return False
            return True