class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        l = len(word)
        starts = []
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append((i,j))
        
        def dfs(a,b,i,visited):
            if i >= l:
                return True

            if a < 0 or a >= m or b < 0 or b >= n or (a,b) in visited or board[a][b] != word[i]:
                return False
            
            visited.add((a,b))
            
            left = dfs(a+1,b,i+1,visited.copy())
            right = dfs(a-1,b,i+1,visited.copy())
            down = dfs(a,b+1,i+1,visited.copy())
            up = dfs(a,b-1,i+1,visited.copy())

            return left or right or down or up
        
        for a,b in starts:
            visited = set()
            if dfs(a,b,0,visited):
                return True
        
        return False
        

        
