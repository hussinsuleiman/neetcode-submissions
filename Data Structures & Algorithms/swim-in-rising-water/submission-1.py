class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        l,r = max(grid[0][0], grid[-1][-1]), 2500
        
        def dfs(k):
            stack = [(0,0)]
            seen = set()

            while stack:
                i,j = stack.pop()
                seen.add((i,j))
                neighbors = {(i+1, j), (i-1, j), (i, j+1), (i, j-1)}

                for x,y in neighbors:
                    if x >= 0 and x < n and y >= 0 and y < n and (x,y) not in seen and max(grid[x][y], grid[i][j]) <= k:
                        stack.append((x,y))
                
            return (n-1, n-1) in seen

        while l < r:
            mid = (l+r) // 2

            if dfs(mid):
                r = mid
            else:
                l = mid+1
            
        return l