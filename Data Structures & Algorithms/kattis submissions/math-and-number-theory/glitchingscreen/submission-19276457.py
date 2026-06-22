h,w,n = map(int, input().split())
board = []

for i in range(n):
    train = []
    
    for j in range(h):
        train.append(input())
    
    board.append(train)

cur = []
found = False
done = False

for i in range(h):
    cur.append(input())

for train in board:
    valid = True
    
    for i in range(h):
        for j in range(w):
            if train[i][j] == '.' and cur[i][j] == 'x':
                valid = False
                break
        
        if not valid:
            break
    
    if valid:
        if found:
            print("no")
            done = True
            break
        found = True
    
    if done:
        break

if not done:
    print("yes")