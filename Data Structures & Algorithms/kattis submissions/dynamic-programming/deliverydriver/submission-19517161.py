costs = list(map(int, input().split()))
N = int(input())
board = []

for i in range(3):
    board.append(list(map(int, input().split())))

dp = [[0,0,0] for i in range(N+1)] 

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0], max(dp[i-1][1] - costs[0], dp[i-1][2] - costs[1])) + board[0][i-1]
    dp[i][1] = max(dp[i-1][1], max(dp[i-1][0] - costs[0], dp[i-1][2] - costs[2])) + board[1][i-1]
    dp[i][2] = max(dp[i-1][2], max(dp[i-1][0] - costs[1], dp[i-1][1] - costs[2])) + board[2][i-1]

print(max(dp[-1]))