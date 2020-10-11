"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
        给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。

        返回一个深拷贝的链表。
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        newhead = RandomListNode(head.label)
        head2 = head
        dummy = RandomListNode(0)
        dummy.next = newhead
        hashmap = {}
        while head2 is not None:
            if head2.random in hashmap: break
            if head2.random is not None: hashmap.update({head2: RandomListNode(head2.random.label)})
            head2 = head2.random
        while head is not None:
            newhead.next = RandomListNode(head.next.label)
            newhead.random = hashmap.get(head.random)
            head = head.next
            newhead = newhead.next
        return dummy.next
