r,c = map(int, input().split())
s = int(input())
board = []
t = 0

for i in range(r):
    nbs = list(map(int, input().split()))
    board.append(nbs)

for i in range(1, r-1):
    for j in range(1, c-1):
        if board[i][j] == s:
            if (board[i-1][j-1] + board[i-1][j+1] + board[i+1][j-1] + board[i+1][j+1]) % s == 0:
                t += 1

print(t)