class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DiListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev



class MyLinkedListv1:

    def __init__(self):
        self.length = 0
        self.dumy_head = ListNode()  
        

    def get(self, index: int) -> int:
        if not (index >= 0 and index < self.length):
            return -1
        node = self.dumy_head.next
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, next=self.dumy_head.next)
        self.dumy_head.next = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        curr = self.dumy_head
        for i in range(self.length):
            curr = curr.next
        curr.next = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not (index >= 0 and index <= self.length):
            return
        curr = self.dumy_head
        for i in range(index):
            curr = curr.next
        newNode = ListNode(val,next=curr.next)
        curr.next = newNode
        self.length += 1 
        
    def deleteAtIndex(self, index: int) -> None:
        if not (index >= 0 and index < self.length):
            return
        curr = self.dumy_head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.length -= 1

        


class MyLinkedList:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if not (index >= 0 and index < self.length):
            return -1
        mid = self.length // 2
        if index <= mid:
            curr = self.head
            for i in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.length - 1 - index):
                curr = curr.prev
        return curr.val
    
    def addAtHead(self, val: int) -> None:
        newNode = DiListNode(val, next=self.head)
        if self.head:
            self.head.prev = newNode
        else:
            self.tail = newNode
        self.head = newNode
        self.length += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = DiListNode(val, prev=self.tail)
        if self.tail:
            self.tail.next = newNode
        else:
            self.head = newNode
        self.tail = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if not (index >= 0 and index <= self.length):
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            mid = self.length // 2
            if index <= mid:
                curr = self.head
                for i in range(index):
                    curr = curr.next
            else:
                curr = self.tail
                for i in range(self.length - 1 - index):
                    curr = curr.prev
            newNode = DiListNode(val, next=curr, prev=curr.prev)
            curr.prev.next = newNode
            curr.prev = newNode
            self.length += 1 
        
    def deleteAtIndex(self, index: int) -> None:
        if not (index >= 0 and index < self.length):
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            
        elif index == self.length - 1: 
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            mid = self.length // 2
            if index <= mid:
                curr = self.head
                for i in range(index):
                    curr = curr.next
            else:
                curr = self.tail
                for i in range(self.length - 1 - index):
                    curr = curr.prev
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.length -= 1



        





# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)