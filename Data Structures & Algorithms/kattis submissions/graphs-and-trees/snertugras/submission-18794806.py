import sys
from collections import deque
input = sys.stdin.readline

def bfs(board, i, j, h, w):
    queue = deque()
    queue.append((i, j))
    level = 0
    visited = set([(i,j)])
    
    while queue:
        l = len(queue)
        
        for k in range(l):
            currI, currJ = queue.popleft()
            
            if board[currI][currJ] == 'G':
                return level
            
            board[currI][currJ] = level
            
            if currI > 0 and (currI-1, currJ) not in visited and board[currI-1][currJ] != '#':
                queue.append((currI-1, currJ))
                visited.add((currI-1, currJ))
            
            if currI < h-1 and (currI+1, currJ) not in visited and board[currI+1][currJ] != '#':
                queue.append((currI+1, currJ))
                visited.add((currI+1, currJ))
            
            if currJ > 0 and (currI, currJ-1) not in visited and board[currI][currJ-1] != '#':
                queue.append((currI, currJ-1))
                visited.add((currI, currJ-1))
            
            if currJ < w-1 and (currI, currJ+1) not in visited and board[currI][currJ+1] != '#':
                queue.append((currI, currJ+1))
                visited.add((currI, currJ+1))
            
        level += 1
    
    return "thralatlega nettengdur"
    
h, w = map(int, input().split())
board = []
startX, startY = 0, 0

for i in range(h):
    line = input().strip()
    row = []
    
    for j in range(w):
        row.append(line[j])
        
        if line[j] == 'S':
            startX, startY = i, j
        
    board.append(row)

print(bfs(board, startX, startY, h, w))

