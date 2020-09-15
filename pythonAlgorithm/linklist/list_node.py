class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        # self.head = self.constructLinklist()
    @classmethod
    def printLinklist(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    # def constructLinklist(self):
    #     dummyNode = ListNode(0)
    #     head = ListNode(self.val[0])
    #     dummyNode.next = head
    #     for i in range(1, len(self.val)):
    #         next = ListNode(self.val[i])
    #         head.next = next
    #         head = next
    #     return dummyNode.next


head_with_6ele_repeat4end = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(1
              )
n6 = ListNode(3)
n7 = ListNode(3)
n8 = ListNode(3)
n9 = ListNode(6)
n10 = ListNode(6)

head_with_6ele_repeat4end.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# n5.next=n6
# n2.next=n7
# n7.next=n8
# n8.next=n9
# n9.next=n10


head_with_1ele = ListNode(1)

head_with_2ele_diff = ListNode(1)
n2 = ListNode(2)

head_with_2ele_diff.next = n2
