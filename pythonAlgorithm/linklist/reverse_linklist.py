class Node:
    def __init__(self, val=0):
        self.value = val
        self.next = None


class LinkList:
    c = 10

    def __init__(self, *args):
        self.val = (*args,)
        self.head = self.__constructLinklist()
        #self.printLinklist(self.head)
        # self.pre = self.revserlinklist()
        # self.printLinklist(self.pre)

    def printLinklist(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def __constructLinklist(self):
        dummyNode = Node()
        head = Node(self.val[0])
        dummyNode.next = head
        for i in range(1, len(self.val)):
            next = Node(self.val[i])
            head.next = next
            head = next
        return dummyNode.next

    def revserlinklist(self):
        pre = None
        while self.head is not None:
            next = self.head.next
            self.head.next = pre
            pre = self.head
            self.head = next
        return pre

    def revserFromM2N(self, m, n):
        #if m<0 or n<0 or n>self.linklength():return None
        head2=self.head
        head3=self.head
        head2.next.next.next=None
        self.printLinklist(self.head)



    def linklength(self):
        length = 0
        while self.head is not None:
            self.head = self.head.next
            length += 1
        return length


a = LinkList(1, 2, 3, 4, 5)

a.revserFromM2N(2,3)
