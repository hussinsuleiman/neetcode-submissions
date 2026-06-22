def min_height(rects, C):
    n = len(rects)
    INF = 10**18
    dp = [INF] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        width = 0
        row_h = 0
 
        for j in range(i, 0, -1):
            w, h = rects[j - 1]
            width += w
            
            if width > C:
                break
            
            row_h = max(row_h, h)
            dp[i] = min(dp[i], dp[j - 1] + row_h)

    return dp[n]

N,C = map(int, input().split())
rects = []

for i in range(N):
    w,h = map(int, input().split())
    rects.append((w,h))
    
print(min_height(rects, C))