class MyCircularQueue:

    def __init__(self, k: int):
        self.head = ListNode(0)
        self.tail = self.head
        self.tail.next = self.head
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        node = ListNode(value)
        self.tail.next = node
        # node.next = self.head
        self.tail = self.tail.next
        self.size += 1
        
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            self.tail = self.head
            return False
        temp = self.head.next
        self.head.next = temp.next
        # temp.next = None
        self.size -= 1
        if self.size == 0:
            self.tail = self.head
            
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.head.next.val

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()