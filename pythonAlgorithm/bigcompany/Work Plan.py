class Solution:
    """
    @param low: the simple task
    @param high: the complex task
    @return: the most value
    小美是团队的负责人，需要为团队制定工作的计划，来帮助团队产生最大的价值。每周团队都会有两项候选的任务,其中一项为简单任务,一项为复杂任务,两项任务都能在一周内完成。在第i周,团队完成简单任务的价值为low_ilow
​i
​​ ,完成复杂任务的价值为high_ihigh
​i
​​ 。由于复杂任务本身的技术难度较高，团队如果在第i周选择执行复杂任务的话,需要在i-1周不做任何任务来专心准备。如果团队在第i周选择执行简单任务的话,不需要提前做任何准备。现在小美的团队收到了未来n周的候选任务列表,请帮助小美确定每周的工作安排使得团队的工作价值最大。

Example
例1:

输入:low=[4,2,3,7],hard=[3,5,6,9]
输出:17
解释:在第一周的时候挑选简单任务，价值=4
在第二周做准备，第三周挑选复杂任务，价值=4+6=10
在第四周挑选简单任务，价值=10+7=17
例2:

输入:low=[1,3,5,9],high=[3,5,7,9]
输出:19
Notice
1 \leq |low|,|high| \leq 100001≤∣low∣,∣high∣≤10000
1 \leq low[i],high[i] \leq 100001≤low[i],high[i]≤10000

    """
    # todo dp
    def workPlan(self, low, high):
        # Write your code here.
            pass