# this is a ver that If the length is even, it will fall to the right
def middlemode(head):
    # write your code here
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


from linklist.list_node import ListNode


# ods and even divide to deal
def findmid(head):
    if not head:
        return None
    if head.next is None: return head
    if head.next.next is None: return head
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    cur = head
    while head is not None and head.next is not None:
        head = head.next.next
        cur = cur.next
        pre = pre.next
    if head is None: return pre  # enev case
    return cur  # ods case
