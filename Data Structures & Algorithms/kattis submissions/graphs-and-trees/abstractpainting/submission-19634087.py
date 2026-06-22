T = int(input())
MOD = 10**9+7

for _ in range(T):
    R,C = map(int, input().split())
    print((18 * pow(6, R+C-2, MOD) * pow(2, (R-1)*(C-1), MOD)) % MOD)