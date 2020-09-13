from linklist.list_node import ListNode


class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """

    def removeElements(self, head, val):
        # write your code here
        if head == None: return None
        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode
        # if head.val == val: return dummyNode.next.next
        while head is not None:
            if head.val == val:
                pre.next = head.next
                head = head.next
                continue
            pre = pre.next
            head = head.next
        return dummyNode.next





