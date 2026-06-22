MOD = 10**9 + 7
n = int(input())

ans = (pow(6, n, MOD) - pow(MOD - 2, n, MOD)) % MOD
ans = ans * pow(8, MOD - 2, MOD) % MOD

print(ans)