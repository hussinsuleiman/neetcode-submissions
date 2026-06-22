cost = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}

dp = [""] * 101
dp[2] = "1"
dp[3] = "7"
dp[4] = "4"
dp[5] = "2"
dp[6] = "6"
dp[7] = "8"

for i in range(8, 101):
    best = None
    for d in range(10):
        c = cost[d]
        if i - c >= 2 and dp[i - c] != "":
            if d == 0:  # zero cannot be leading
                candidate = dp[i - c][0] + "0" + dp[i - c][1:]
            else:
                candidate = str(d) + dp[i - c]
            
            if best is None:
                best = candidate
            else:
                if len(candidate) < len(best) or \
                   (len(candidate) == len(best) and candidate < best):
                    best = candidate
    dp[i] = best

T = int(input())

for i in range(T):
    n = int(input())
    m = n//2
    maxi = '1' * m
    
    if n%2 == 1:
        maxi = '7' + '1' * (m-1)
    
    print(dp[n] + ' ' + maxi)