class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {i : i for i in range(n)}
        nbComp = n
        rank = [1] * n

        def find(n1):
            res = n1

            while par[res] != res:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
                rank[p1] = 0

            return 1
        
        for i,j in edges:
            nbComp -= union(i,j)
        
        return nbComp
        
            
            

        
