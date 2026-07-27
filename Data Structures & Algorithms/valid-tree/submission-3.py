class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        def find(u, parent):
            while parent[u] != -1:
                u = parent[u]
            return u
        
        def union(u, v, parent, size):
            p,q = find(u, parent), find(v, parent)
            
            if p == q:
                return False
            
            if size[p] < size[q]:
                p,q = q,p
            
            parent[q] = p
            size[p] += size[q]
            return True

        parent = [-1] * n
        size = [1] * n

        for a,b in edges:
            if not union(a, b, parent, size):
                return False
        
        return True