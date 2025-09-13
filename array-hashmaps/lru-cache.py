class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key, Node

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left
    
    # remove any node in the ls
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # insert any node to the right of cache (making it the most recent one)
    def insert(self, node):
        cur_right = self.right.prev

        cur_right.next = node
        node.prev = cur_right

        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(Node(key, value))
        else:
            self.insert(Node(key, value))
        self.cache[key] = self.right.prev

        if len(self.cache) > self.capacity:
            head = self.left.next
            self.remove(head)
            del self.cache[head.key]


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)