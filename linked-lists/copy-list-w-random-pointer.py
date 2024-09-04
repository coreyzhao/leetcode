"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        visited = {}

        
        def get_cloned_node(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val)
                    return visited[node]
            return None

        current = head
        while current:
            
            if current not in visited:
                visited[current] = Node(current.val)
            
            
            visited[current].next = get_cloned_node(current.next)
            
           
            visited[current].random = get_cloned_node(current.random)
            
            current = current.next

        
        return visited[head]
        
       