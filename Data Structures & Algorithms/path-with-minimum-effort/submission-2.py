class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(k):
            stack = [(0,0)]
            seen = set()
            seen.add((0,0))

            while stack:
                x,y = stack.pop()

                for dx,dy in dirs:
                    if x+dx >= 0 and x+dx < row and y+dy >= 0 and y+dy < col and (x+dx,y+dy) not in seen and abs(heights[x+dx][y+dy] - heights[x][y]) <= k:
                        stack.append((x+dx, y+dy))
                        seen.add((x+dx,y+dy))

            return (row-1, col-1) in seen

        row, col = len(heights), len(heights[0])
        maxes = [max(heights[i]) for i in range(row)]
        l,r = 0, max(maxes)
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]

        while l < r:
            mid = (l+r)//2

            if not valid(mid):
                l = mid+1
            else:
                r = mid
            
        return l