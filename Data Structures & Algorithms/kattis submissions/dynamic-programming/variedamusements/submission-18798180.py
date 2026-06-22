n, a, b, c = map(int, input().split())
MOD = 10**9+7

dp = [[0, 0, 0], [a, b, c]]

for i in range(2, n+1):
    new = []
    new.append((dp[-1][1] + dp[-1][2]) * a)
    new.append((dp[-1][0] + dp[-1][2]) * b)
    new.append((dp[-1][0] + dp[-1][1]) * c)
    
    dp.append(new)

print((dp[-1][0] + dp[-1][1] + dp[-1][2]) % MOD)