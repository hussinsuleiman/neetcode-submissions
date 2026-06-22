n,m = map(int, input().split())
MOD = 10**9+7
print((pow(3,m,MOD) * pow(2,n-2*m,MOD) - 1)%MOD)