class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        res = []

        def dfs(i,j,ocean):
            ocean.add((i,j))
            nei = {(i+1,j),(i-1,j),(i,j+1),(i,j-1)}
            
            for x,y in nei:
                if (x,y) not in ocean and x >= 0 and x < m and y >= 0 and y < n and heights[x][y] >= heights[i][j]:
                    dfs(x,y,ocean)

        pacific = set()
        atlantic = set()

        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)
        
        for j in range(n):
            dfs(0,j,pacific)
            dfs(m-1,j,atlantic)

        for i in range(m):
            for j in range(n):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
        
        return res