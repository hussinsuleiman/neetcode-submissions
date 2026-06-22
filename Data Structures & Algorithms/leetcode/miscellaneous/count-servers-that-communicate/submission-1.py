class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        t = 0
        m,n = len(grid), len(grid[0])
        seen = set()

        for i in range(m):
            nbOnes = 0
            elts = set()

            for j in range(n):
                if grid[i][j] == 1:
                    nbOnes += 1
                    elts.add((i,j))
                
            if nbOnes > 1:
                t += nbOnes
                
                for elt in elts:
                    seen.add(elt)
        
        for j in range(n):
            nbOnes = 0
            s = 0

            for i in range(m):
                if grid[i][j] == 1:
                    nbOnes += 1

                    if (i,j) not in seen:
                        seen.add((i,j))
                    else:
                        s += 1
                
            if nbOnes > 1:
                t += nbOnes - s
        
        return t