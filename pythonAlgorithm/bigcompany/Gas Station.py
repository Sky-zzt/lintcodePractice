
'''
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第_i_个加油站前往第_i_+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。

Example
样例 1:

输入:gas[i]=[1,1,3,1],cost[i]=[2,2,1,1]
输出:2
样例 2:

输入:gas[i]=[1,1,3,1],cost[i]=[2,2,10,1]
输出:-1
Challenge
O(n)时间和O(1)额外空间

Notice
数据保证答案唯一。
'''
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    https://www.bilibili.com/video/BV13k4y1o7SU?from=search&seid=5073604284006055839

    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        sum=0
        spend=0
        for i in range(len(gas)):

            sum+=gas[i]
            sum-=cost[0]
            if sum>=0:
                continue
            sum=0
