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
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    import sys
    '''
    看似简单，实则很棘手 ，  有三种case需要处理，
    1.   5-》null 2
    2、   1-》2-》3-》6   5
    3、 1-》null   2  
    我只想到了第二种  1，只需要pre 加一个dummy = ListNode(-sys.maxsize)
    3.就是44行if 语句 
    '''
    # todo 写题千万不能大意，要想全面
    def insertNode(self, head, val):
        # write your code here
        if not head: return ListNode(val)
        newNode = ListNode(val)
        import sys
        dummy = ListNode(-sys.maxsize)
        dummy.next = head
        pre = dummy
        while head is not None:
            if head.val >= val and pre.val<=val:
                newNode.next=head
                pre.next = newNode
                #newNode.next = head
                break
            head = head.next
            pre=pre.next
        if pre.val<=val:
            pre.next=newNode
        return dummy.next
s=Solution()
s.insertNode(head_with_6ele_repeat4end,5)

ListNode.printLinklist(head_with_6ele_repeat4end)


