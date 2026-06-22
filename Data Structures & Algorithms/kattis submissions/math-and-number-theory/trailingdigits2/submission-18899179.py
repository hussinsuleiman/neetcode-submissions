MOD = 10**10
n = int(input())
t = 0

for i in range(1, n + 1):
    t = (t + pow(i, i, MOD)) % MOD

print(t)