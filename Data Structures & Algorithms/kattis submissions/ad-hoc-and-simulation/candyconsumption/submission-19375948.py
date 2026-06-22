N = int(input())
MOD = 10**9+7
res = 0
cur = N

for i in range(2, N+2):
    res = (res + (i-1)*i*cur) % MOD
    cur = (cur*(N+1-i)) % MOD

print(res)