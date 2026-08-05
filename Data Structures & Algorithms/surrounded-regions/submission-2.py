class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board), len(board[0])
        seen = set()

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == 'X' or (i,j) in seen:
                return
            
            seen.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            if board[i][0] == 'O' and (i,0) not in seen:
                dfs(i,0)
            
            if board[i][n-1] == 'O' and (i,n-1) not in seen:
                dfs(i,n-1)
        
        for j in range(n):
            if board[0][j] == 'O' and (0,j) not in seen:
                dfs(0,j)
            
            if board[m-1][j] == 'O' and (m-1,j) not in seen:
                dfs(m-1,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in seen:
                    board[i][j] = 'X'