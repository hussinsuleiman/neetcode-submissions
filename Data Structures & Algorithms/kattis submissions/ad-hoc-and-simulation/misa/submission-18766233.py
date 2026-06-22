import sys
input = sys.stdin.readline

def findNeighbors(board, i, j, R, S):
    res = 0
    
    if i > 0:
        if board[i-1][j] == 'o':
            res += 1
        
        if j > 0 and board[i-1][j-1] == 'o':
            res += 1
        
        if j < S-1 and board[i-1][j+1] == 'o':
            res += 1
    
    if j > 0 and board[i][j-1] == 'o':
        res += 1
    
    if j < S-1 and board[i][j+1] == 'o':
        res += 1 
    
    if i < R-1:
        if board[i+1][j] == 'o':
            res += 1
        
        if j > 0 and board[i+1][j-1] == 'o':
            res += 1
        
        if j < S-1 and board[i+1][j+1] == 'o':
            res += 1
    
    return res
    

R, S = map(int, input().split())
board = []

for i in range(R):
    line = input().strip()
    board.append(line)

maxNei = 0
total = 0

for i in range(R):
    for j in range(S):
        nei = findNeighbors(board, i, j, R, S)
        
        if board[i][j] == '.':
            maxNei = max(maxNei, nei)
        else:
            total += nei

total = total // 2 + maxNei
print(total)
        