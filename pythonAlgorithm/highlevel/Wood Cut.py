'''
有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

Example
样例 1

输入:
L = [232, 124, 456]
k = 7
输出: 114
Explanation: 我们可以把它分成114cm的7段，而115cm不可以
样例 2

输入:
L = [1, 2, 3]
k = 7
输出: 0
说明:很显然我们不能按照题目要求完成。
Challenge
O(n log Len), Len为 n 段原木中最大的长度

Notice
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。
'''


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces



    算法：二分
题目意思是说给出 n 段木材L[i], 将这 n 段木材切分为至少 k 段，这 k 段等长，

若直接枚举每段木材的长度则时间复杂度高达 O(n*maxL), 我们可以使用二分答案来优化枚举木材长度的过程

设left=0,即木材长度最小为0，设right=max_L 即所有木材中最长的长度，因为结果是不可能大于这个长度的，mid = left + right/2
若长度为mid时不能完成，说明太长了，那么我们往区间[left,mid]搜，
若可以完成，说明也许可以更长，那么我们往[mid,right]搜,
在check函数中，我们判断用所有木头除当前mid的值的和是否大于等于k，若小于则说明该mid不可行, 若大于等于则说明mid可行
由于判断条件是left + 1 < right,最后结果就是left的值
复杂度分析
时间复杂度O(nlog（L）)
二分查找的复杂度
空间复杂度O(size(L))
只有数组L
    """

    # todo 九章算法强化班中讲过的基于值的二分法。 ：   类似的还有robot jumping
    def woodCut(self, L, k):
        # write your code here
        len_L = len(L)
        if len_L == 0:
            return 0
        max_L = 0
        for i in range(len_L):
            max_L = max(max_L, L[i])
        left, right = 0, max_L

        def check(mid):
            cou = 0
            # 计算当前长度下能分成几段
            for i in range(len_L):
                cou += (int)(L[i] / mid)
            # 如果还能分更长的，返回true
            if cou >= k:
                return True
            # 如果不能分更长的，返回false
            return False

        while left + 1 < right:
            mid = (int)(left + (right - left) / 2)
            if check(mid):  # 如果还能分更长的，则往[mid,right]走
                left = mid
            else:  # 如果不能分更长的，则往[left,mid]走
                right = mid
        if check(right):
            return right
        return left
