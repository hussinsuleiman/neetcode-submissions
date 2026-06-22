import sys
input = sys.stdin.readline

M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
words = []

for i in range(M):
    word = input().strip()
    words.append(word)

board = []

for i in range(M + U + D):
    line = []
    
    for j in range(N + L + R):
        if (i+j) % 2 == 0:
            line.append('#')
        else:
            line.append('.')
    
    board.append(line)

for i in range(U, M + U):
    for j in range(L, L + N):
        board[i][j] = words[i-U][j-L]

output = []

for line in board:
    output.append(''.join(line))

print('\n'.join(output))
