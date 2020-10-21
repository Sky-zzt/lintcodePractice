class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    给出一个数组 nums 包含 n + 1 个整数，每个整数是从 1 到 n (包括边界)，保证至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

Example
样例 1:

输入:
[5,5,4,3,2,1]
输出:
5
样例 2:

输入:
[5,4,4,3,2,1]
输出:
4
Notice
1.不能修改数组(假设数组只能读)
2.只能用额外的O(1)的空间
3.时间复杂度小于O(n^2)
4.数组中只有一个重复的数，但可能重复超过一次
    """

    def findDuplicate(self, nums):
        # write your code here
        nums = sorted(nums)
        # todo 方法一 ：枚举每一个数 二分枚举 用二分的 first position 和last postion 看位置是否相等 ，nlogn
        # todo 排序 重复的数就扎堆了，遍历一遍 不就得出了
        '''
        使用九章算法班&九章算法强化版里讲过的快慢指针的方法。 要做这个题你首先需要去做一下 Linked List Cycle 这个题。
         如果把数据看做一个 LinkedList，第 i 个位置上的值代表第 i 个点的下一个点是什么的话，
        我们就能画出一个从 0 出发的，一共有 n + 1 个点的 Linked List。 
        可以证明的一件事情是，这个 Linked List 一定存在环。因为无环的 Linked List 里 非空next 的数目和节点的数目关系是差一个（节点多，非空next少）

那么，我们证明了这是一个带环链表。而我们要找的重复的数，也就是两个点都指向了同一个点作为 next 的那个点。也就是环的入口。

因此完全套用 Linked List Cycle 这个题快慢指针的方法即可。

什么是快慢指针算法？ 从起点出发，慢指针走一步，快指针走两步。因为有环，所以一定会相遇。 相遇之后，把其中一根指针拉回起点，重新走，这回快慢指针都各走一步。他们仍然会再次相遇，且相遇点为环的入口。

时间复杂度是多少？ 时间复杂度是 On
        '''
