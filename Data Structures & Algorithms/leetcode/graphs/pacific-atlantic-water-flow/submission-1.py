class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(ocean):
            queue = deque(ocean)

            while queue:
                x,y = queue.popleft()

                if x > 0 and (x-1,y) not in ocean and heights[x-1][y] >= heights[x][y]:
                    queue.append((x-1,y))
                    ocean.add((x-1,y))

                if y > 0 and (x,y-1) not in ocean and heights[x][y-1] >= heights[x][y]:
                    queue.append((x,y-1))
                    ocean.add((x,y-1))
                
                if x < n-1 and (x+1,y) not in ocean and heights[x+1][y] >= heights[x][y]:
                    queue.append((x+1,y))
                    ocean.add((x+1,y))
                
                if y < m-1 and (x,y+1) not in ocean and heights[x][y+1] >= heights[x][y]:
                    queue.append((x,y+1))
                    ocean.add((x,y+1))
            
            return ocean

        pacific = set()
        atlantic = set()
        n, m = len(heights), len(heights[0])

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:   
                    pacific.add((i,j))
                if i == n-1 or j == m-1:
                    atlantic.add((i,j))
        
        pacific = bfs(pacific)
        atlantic = bfs(atlantic)
        output = []

        for i in range(n):
            for j in range(m):
                if (i,j) in pacific and (i,j) in atlantic:
                    output.append([i,j])
        
        return output