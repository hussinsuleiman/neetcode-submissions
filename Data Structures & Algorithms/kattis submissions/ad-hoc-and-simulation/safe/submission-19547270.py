from collections import deque

board = []

for i in range(3):
    row = list(map(int, input().split()))
    for k in row:
        board.append(k)

def encode(board):
    code = 0
    power = 1
    
    for i in range(9):
        code += board[i] * power
        power *= 4
    
    return code

def decode(code):
    board = []
    
    for i in range(9):
        board.append(code%4)
        code //= 4
    
    return board
    
def make_move(code, move_index):
    board = decode(code)
    
    for k in moves[move_index]:
        board[k] = (board[k]-1)%4
    
    return encode(board)

moves = []

for r in range(3):
    for c in range(3):
        affected = set()
        
        for j in range(3):
            affected.add(3*r+j)
        
        for i in range(3):
            affected.add(3*i+c)
        
        moves.append(affected)

dist = [-1] * (4**9)
dist[0] = 0
queue = deque()
queue.append(0)

while queue:
    t = queue.popleft()
    
    for move in range(9):
        nei = make_move(t, move)
        
        if dist[nei] == -1:
            dist[nei] = dist[t]+1
            queue.append(nei)
    
code = encode(board)
print(dist[code])