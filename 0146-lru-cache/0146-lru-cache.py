class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # HashMap for O(1) lookup
        self.head = Node(0, 0)  # dummy head node
        self.tail = Node(0, 0)  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node = self.cache[key]

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node 

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            node.prev.next = node.next
            node.next.prev = node.prev

            node.next = self.head.next
            node.prev = self.head
            self.head.next.prev = node
            self.head.next = node 

        else:
            if len(self.cache) == self.capacity: #full

                lru = self.tail.prev
                lru.prev.next = self.tail
                self.tail.prev = lru.prev
                del self.cache[lru.key]

                new_node = Node(key,value)
                new_node.val = value

                new_node.next = self.head.next
                new_node.prev = self.head
                self.head.next.prev = new_node
                self.head.next = new_node 
                self.cache[key] = new_node
            else:
                new_node = Node(key,value)
                new_node.val = value

                new_node.next = self.head.next
                new_node.prev = self.head
                self.head.next.prev = new_node
                self.head.next = new_node
                self.cache[key] = new_node 

            

                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)