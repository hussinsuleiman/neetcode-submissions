X,Y,N = map(int, input().split())
board = []

for _ in range(X):
    row = input().split()
    board.append(row)

for i in range(X):
    for j in range(Y-N+1):
        cur = board[i][j]
        
        if cur == 'O':
            continue
        
        found = True
        
        for k in range(N):
            if board[i][j+k] != cur:
                found = False
                break
        
        if found:
            if cur == 'B':
                print("BLUE WINS")
            else:
                print("RED WINS")
            exit()

for j in range(Y):
    for i in range(X-N+1):
        cur = board[i][j]
        
        if cur == 'O':
            continue
        
        found = True
        
        for k in range(N):
            if board[i+k][j] != cur:
                found = False
                break
        
        if found:
            if cur == 'B':
                print("BLUE WINS")
            else:
                print("RED WINS")
            exit()

for i in range(X-N+1):
    for j in range(Y-N+1):
        cur = board[i][j]
        
        if cur == 'O':
            continue
        
        found = True
        
        for k in range(N):
            if board[i+k][j+k] != cur:
                found = False
                break
        
        if found:
            if cur == 'B':
                print("BLUE WINS")
            else:
                print("RED WINS")
            exit()

for i in range(X-N+1):
    for j in range(N-1, Y):
        cur = board[i][j]
        
        if cur == 'O':
            continue
        
        found = True
        
        for k in range(N):
            if board[i+k][j-k] != cur:
                found = False
                break
        
        if found:
            if cur == 'B':
                print("BLUE WINS")
            else:
                print("RED WINS")
            exit()

print("NONE")