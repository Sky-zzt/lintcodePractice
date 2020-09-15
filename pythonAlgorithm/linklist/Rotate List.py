"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from linklist.list_node import ListNode, head_with_2ele_diff,head_with_6ele_repeat4end


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    # todo 快慢指针
    def rotateRight(self, head, k):
        # write your code here
        if not head: return None
        if head.next is None: return head
        cur = head
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        j = 0
        for i in range(1, k + 1):
            if head.next is not None:
                j += 1
                head = head.next
        if j <= k: return pre
        while head.next is not None:
            head = head.next
            cur = cur.next
            # pre = pre.next
        cur.next = None
        head.next = pre
        return head


s = Solution()
s.rotateRight(head_with_6ele_repeat4end, 1)
