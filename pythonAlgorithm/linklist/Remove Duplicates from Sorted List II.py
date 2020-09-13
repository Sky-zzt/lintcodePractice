"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from linklist.list_node import ListNode, head_with_6ele_repeat4end, head_with_1ele, head_with_2ele_diff


class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """

    # todo try again
    def deleteDuplicates(self, head):
        # write your code here
        if head == None: return None
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        while head != None:
            if head.next != None and head.val == head.next.val:
                value = head.val  # todo important
                while head != None and head.val == value:
                    head = head.next  # todo also
                pre.next = head
            else:
                pre = head
                head = head.next
        return dummyNode.next

    # todo recomond 
    def deleteDuplicates2(self, head):
        if head == None: return None
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        while head != None:
            if head.next != None and head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
                head=head.next
            else:
                pre = pre.next# or pre=head
                head = head.next
        return dummyNode.next


s = Solution()
a = s.deleteDuplicates2(head_with_6ele_repeat4end)
head_with_2ele_diff.printLinklist(a)
