class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(u, parent):
            while -1 != parent[u]:
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

        parent = [-1]*n
        size = [1]*n
        comp = n

        for a,b in edges:
            if union(a, b, parent, size):
                comp -= 1

        return comp