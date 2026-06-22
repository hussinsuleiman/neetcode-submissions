N = int(input())

for i in range(N):
    message = input()
    l = len(message)
    m = int(l ** 0.5)
    
    if m*m < l:
        m += 1
    
    board = []
    index = 0
    
    for j in range(m):
        line = []
        
        for k in range(m):
            if index < l:
                line.append(message[index])
                index += 1
            else:
                line.append('*')
        
        board.append(line)
    
    output = []
    
    for j in range(m):
        for k in range(m-1, -1, -1):
            if board[k][j] != '*':
                output.append(board[k][j])
    
    print(''.join(output))
    
    