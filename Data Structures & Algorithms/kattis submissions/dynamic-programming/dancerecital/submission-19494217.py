R = int(input())
routines = [input() for i in range(R)]
masks = []
costs = [[0]*R for i in range(R)]

for r in routines:
    m = 0
    
    for c in r:
        m |= 1 << (ord(c)-ord('A'))
    
    masks.append(m)

for i in range(R):
    for j in range(R):
        costs[i][j] = bin(masks[i] & masks[j]).count('1')
    
INF = float('inf')
dp = [[INF]*R for i in range(1 << R)]

for i in range(R):
    dp[1 << i][i] = 0

for mask in range(1 << R):
    for i in range(R):
        if not (mask & (1 << i)):
            continue
        
        for j in range(R):
            if (mask & (1 << j)):
                continue
            
            new_mask = mask | (1 << j)
            dp[new_mask][j] = min(dp[new_mask][j], dp[mask][i] + costs[i][j])

print(min(dp[(1 << R)-1]))