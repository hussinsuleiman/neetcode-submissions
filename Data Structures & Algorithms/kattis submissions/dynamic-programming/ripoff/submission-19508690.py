N,S,T = map(int, input().split())
board = [0]

while True:
    line = input().strip()
    
    if line == '0':
        break
    
    line = list(map(int, line.split()))
    
    for nb in line:
        board.append(nb)

board.append(0)
INF = float('inf')
dp = [[-INF]*(T+1) for i in range(N+2)]
dp[0][0] = 0

for i in range(1, N+2):
    for k in range(T, 0, -1):
        for j in range(1, min(S+1,i+1)):
            dp[i][k] = max(dp[i][k], dp[i-j][k-1] + board[i])

print(max(dp[N+1]))