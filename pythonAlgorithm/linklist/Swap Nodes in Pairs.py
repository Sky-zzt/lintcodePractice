from linklist.list_node import ListNode, head_with_6ele_repeat4end

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a ListNode
    @return: a ListNode

        right

    """
    '''
    def swapPairs(self, head):
        if not head or head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next is not None and head.next.next is not None:
            n1 = head.next
            n2 = head.next.next
            head.next = n2
            n1.next = n2.next
            n2.next = n1
            head = n1
        return dummy.next
    '''

    def swapPairs(self, head):
        # write your code here
        if not head or head.next is None: return head
        dummyNode = ListNode(0)
        dummyNode.next = head
        while head.next is not None:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head
            head = head.next
        return dummyNode.next


s = Solution()
s.swapPairs(head_with_6ele_repeat4end)
ListNode.printLinklist(head_with_6ele_repeat4end)
