N = int(input())

for _ in range(N):
    M = int(input())
    dist = list(map(int, input().split()))
    dp = dict()
    dp[0] = ([], 0)

    for i in range(M):
        new = dict()
        
        for key in dp:
            m = max(dp[key][1], key + dist[i])
            
            if key + dist[i] not in new or m < new[key + dist[i]][1]:
                new[key + dist[i]] = (dp[key][0] + ['U'], m)
            
            if key >= dist[i]:
                if key - dist[i] not in new or dp[key][1] < new[key - dist[i]][1]:
                    new[key-dist[i]] = (dp[key][0] + ['D'], dp[key][1])
            
        dp = new
    
    if 0 not in dp:
        print("IMPOSSIBLE")
        continue
    
    print(''.join(dp[0][0]))