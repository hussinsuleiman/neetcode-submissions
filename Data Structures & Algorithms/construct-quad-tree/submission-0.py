"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(a,b,c,d):
            leaf = True

            for i in range(a,c+1):
                for j in range(b,d+1):
                    if grid[i][j] != grid[a][b]:
                        leaf = False
                        break

            if leaf:
                node = Node(grid[a][b], True)
                return node
            
            node = Node(1, False)
            node.topLeft = build(a, b, (a+c+1)//2-1, (b+d+1)//2-1)
            node.topRight = build(a, (b+d+1)//2, (a+c+1)//2-1, d)
            node.bottomLeft = build((a+c+1)//2, b, c, (b+d+1)//2-1)
            node.bottomRight = build((a+c+1)//2, (b+d+1)//2, c, d)
            return node

        n = len(grid)
        return build(0, 0, n-1, n-1)