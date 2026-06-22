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
            
        oldToNew = dict()
        node = head

        while node:
            oldToNew[node] = Node(node.val)
            node = node.next
        
        node = head

        while node and node.next:
            oldToNew[node].next = oldToNew[node.next]

            if node.random:
                oldToNew[node].random = oldToNew[node.random]
            
            node = node.next
        
        if node.random:
            oldToNew[node].random = oldToNew[node.random]

        return oldToNew[head]

        