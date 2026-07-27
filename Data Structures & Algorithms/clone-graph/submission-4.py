"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = dict()
        res = self.addNode(node, old_to_new)
        return res

    def addNode(self, node, old_to_new):
        if node in old_to_new:
            return old_to_new[node]
        
        new = Node(node.val)
        old_to_new[node] = new

        for nei in node.neighbors:
            new.neighbors.append(self.addNode(nei, old_to_new))
        
        return new