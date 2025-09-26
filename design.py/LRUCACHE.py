class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.cur_capacity = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def insertEnd(self, key: int, val: int):
        curLastNode = self.tail.prev

        newNode = Node(key, val)
        curLastNode.next = newNode

        newNode.prev = curLastNode
        newNode.next = self.tail

        self.tail.prev = newNode

        
        return newNode

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.cache[key] = self.insertEnd(key, val)
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            self.cur_capacity += 1
            self.cache[key] = self.insertEnd(key, value)

            if self.cur_capacity > self.capacity:
                leastNode = self.head.next
                self.remove(leastNode)
                self.cache.pop(leastNode.key)
                self.cur_capacity -= 1

        else:
            self.remove(self.cache[key])
            self.cache[key] = self.insertEnd(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)