class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {i : i for i in range(1, n+1)}
        rank = [1] * (n+1)

        def find(n1):
            res = n1

            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0

            return False
        
        for i,j in edges:
            if union(i,j):
                return [i,j]