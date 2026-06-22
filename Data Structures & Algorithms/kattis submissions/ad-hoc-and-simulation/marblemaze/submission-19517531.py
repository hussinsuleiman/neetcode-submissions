W,H,N = map(int, input().split())
X0,Y0 = map(int, input().split())
grid = []
alternating = {}

for i in range(H):
    row = []
    line = input()
    
    for j in range(W):
        row.append(line[j])
        
        if line[j] in {'-', '|'}:
            alternating[(i,j)] = 0
    
    grid.append(row)

for i in range(N):
    x,y = X0,Y0
    
    while True:
        if x == W or x == -1 or y == H or y == -1 or grid[y][x] == '.':
            print(str(x) + ' ' + str(y))
            break
        
        elif grid[y][x] == '-':
            prev = alternating[(y,x)]
            alternating[(y,x)] += 1
            
            if prev%2 == 0:
                x -= 1
            else:
                x += 1
            
        elif grid[y][x] == '|':
            prev = alternating[(y,x)]
            alternating[(y,x)] += 1
            
            if alternating[(y,x)]%2 == 0:
                y += 1
            else:
                y -= 1
        
        elif grid[y][x] == '>':
            x += 1
        
        elif grid[y][x] == '<':
            x -= 1
        
        elif grid[y][x] == '^':
            y -= 1
        
        elif grid[y][x] == 'v':
            y += 1