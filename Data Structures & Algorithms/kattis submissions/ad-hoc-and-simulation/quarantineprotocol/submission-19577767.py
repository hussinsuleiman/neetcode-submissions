n,m = map(int, input().split())
board = []
res = 0

for _ in range(n):
    line = input().split()
    board.append(line)

for j in range(m):
    clean = True
    index = 0
    
    for i in range(n):
        if board[i][j] == 'X':
            clean = False
        
        elif board[i][j] == '#':
            if clean:
                res += i+1 - index
            else:
                res += 1
                
            index = i+1
            clean = True
    
    if clean:
        res += n - index

print(res)