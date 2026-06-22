board = []

for i in range(3):
    line = input()
    row = []
    
    for c in line:
        row.append(c)
    
    board.append(row)

for i in range(3):
    if board[i][0] == 'E':
        continue
    
    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
        if board[i][0] == 'O':
            print("O")
        else:
            print("X")
        exit()

for i in range(3):
    if board[0][i] == 'E':
        continue
    
    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
        if board[0][i] == 'O':
            print("O")
        else:
            print("X")
        exit()

if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != 'E':
    if board[0][0] == 'O':
        print("O")
    else:
        print("X")
    exit()

if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != 'E':
    if board[0][2] == 'O':
        print("O")
    else:
        print("X")
    exit()

print("N")