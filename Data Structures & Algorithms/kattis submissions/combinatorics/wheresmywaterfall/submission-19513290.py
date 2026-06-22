n,m,k = map(int, input().split())
p = list(map(int, input().split()))
board = []
positions = [(0,pos) for pos in p]

for i in range(n):
    line = input()
    row = []
    
    for c in line:
        row.append(c)
    
    board.append(row)
    
while positions:
    posX, posY = positions.pop()
    
    for i in range(posX, n):
        if board[i][posY] == 'O':
            board[i][posY] = '~'
        
        elif board[i][posY] == '~':
            break
        
        else:
            j = posY-1
            
            while j > -1 and board[i][j] in {'#', '?'} and board[i-1][j] == 'O':
                board[i-1][j] = '~'
                j -= 1
            
            if j > -1 and board[i-1][j] == 'O':
                positions.append((i-1,j))
                
            j = posY+1
            
            while j < m and board[i][j] in {'#', '?'} and board[i-1][j] == 'O':
                board[i-1][j] = '~'
                j += 1
            
            if j < m and board[i-1][j] == 'O':
                positions.append((i-1, j))
                
            break
        
for row in board:
    print(''.join(row))