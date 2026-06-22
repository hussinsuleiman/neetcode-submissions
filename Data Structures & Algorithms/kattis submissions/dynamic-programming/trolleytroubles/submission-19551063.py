N,L = map(int, input().split())
K = int(input()) - 1
board = []

for i in range(N):
    line = input()
    row = [line[k] for k in range(L)]
    board.append(row)

dp = [[-1]*N for i in range(L+1)]
pointers = [[-1]*(L+1) for i in range(N)]

for t in range(N):
    dp[0][t] = 0
    pointers[t][0] = t

for i in range(1, L+1):
    for k in range(N):
        if dp[i][k] != -1:
            continue
        
        if board[k][L-i] == '=':
            dp[i][k] = dp[i-1][k]
            pointers[k][L-i] = k
        
        elif board[k][L-i] == 'H':
            dp[i][k] = dp[i-1][k] + 1
            pointers[k][L-i] = k
        
        elif board[k][L-i] == 'v':
            end = k
            
            while board[end][L-i] == 'v':
                end += 1
            
            m = dp[i-1][end]
            
            if board[end][L-i] == 'H':
                dp[i][end] = dp[i-1][end] + 1
                pointers[end][L-i] = end
                m += 1
            
            for t in range(end-1, k-1, -1):
                m = min(m, dp[i-1][t])
                
                if m == dp[i-1][t]:
                    pointers[t][L-i] = t
                else:
                    pointers[t][L-i] = t+1
                
                dp[i][t] = m
            
        elif board[k][L-i] == '^':
            end = k
            
            while board[end][L-i] == '^':
                end -= 1
            
            m = dp[i-1][end]
            
            if board[end][L-i] == 'H':
                dp[i][end] = dp[i-1][end] + 1
                pointers[end][L-i] = end
                m += 1
            
            for t in range(end+1, k+1):
                m = min(m, dp[i-1][t])
                
                if m == dp[i-1][t]:
                    pointers[t][L-i] = t
                else:
                    pointers[t][L-i] = t-1
                    
                dp[i][t] = m

print(dp[L][K])
cur = K

for i in range(L):
    while pointers[cur][i] != cur:
        if pointers[cur][i] == cur+1:
            print(str(i+1) + 'd')
            cur += 1
        else:
            print(str(i+1) + 'u')
            cur -= 1     