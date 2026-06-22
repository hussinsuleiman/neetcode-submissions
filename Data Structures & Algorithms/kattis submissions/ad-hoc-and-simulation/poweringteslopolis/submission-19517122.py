N = int(input())
M = int(input())
board = []

for i in range(N):
    line = input()
    row = []
    
    for c in line:
        row.append(c)
    
    board.append(row)

lit = set()
neighbors = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)}

for i in range(N):
    for j in range(M):
        if board[i][j] == 'T':
            lit.add((i,j))
        else:
            for x,y in neighbors:
                if i+x < 0 or i+x >= N or j+y < 0 or j+y >= M:
                    continue
                
                if board[i+x][j+y] == 'T':
                    lit.add((i,j))
                    break

ans = []

for i in range(N):
    for j in range(M):
        if (i,j) not in lit:
            ans.append(str(i) + ' ' + str(j))

if ans:
    print("False")
    print('\n'.join(ans))
else:
    print("True")