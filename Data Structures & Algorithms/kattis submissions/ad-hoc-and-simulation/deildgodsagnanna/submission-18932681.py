n = int(input())
MOD = 10**9+7
p = n

for i in range(1,20):
    p = p*(n-i)

print((p//8)%MOD)