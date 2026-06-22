board = []

for k in range(9):
    row = input().split()
    
    if len(set(row)) != 9:
        print("INVALID!")
        exit()
    
    board.append(row)

for j in range(9):
    col = set()
    
    for i in range(9):
        if board[i][j] in col:
            print("INVALID!")
            exit()
        
        col.add(board[i][j])

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        cells = set()
        
        for k1 in range(3):
            for k2 in range(3):
                if board[i+k1][j+k2] in cells:
                    print("INVALID!")
                    exit()
                
                cells.add(board[i+k1][j+k2])

print("VALID")