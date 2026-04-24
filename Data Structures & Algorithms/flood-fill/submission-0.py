class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        seen = set([(sr, sc)])
        m,n = len(image), len(image[0])

        while stack:
            r,c = stack.pop()

            if r > 0 and image[r-1][c] == image[r][c] and (r-1,c) not in seen:
                stack.append((r-1, c))
                seen.add((r-1, c))
            
            if r < m-1 and image[r+1][c] == image[r][c] and (r+1,c) not in seen:
                stack.append((r+1, c))
                seen.add((r+1, c))
            
            if c > 0 and image[r][c-1] == image[r][c] and (r,c-1) not in seen:
                stack.append((r, c-1))
                seen.add((r, c-1))
            
            if c < n-1 and image[r][c+1] == image[r][c] and (r,c+1) not in seen:
                stack.append((r, c+1))
                seen.add((r, c+1))
        
        for i in range(m):
            for j in range(n):
                if (i,j) in seen:
                    image[i][j] = color
        
        return image
        