s = input()
MOD = 10**9+7
k = 0

for c in s:
    if c == '?':
        k += 1

res = 0
prevQ = 0
prev1 = 0
l = len(s)

for i in range(l):
    if s[i] == '0':
        res += (pow(2, max(0,k-1), MOD) * prevQ + pow(2, k, MOD) * prev1) % MOD
        
    elif s[i] == '?':
        prevQ += 1
    
    else:
        prev1 += 1
        res += (pow(2, max(0,k-1), MOD) * (k-prevQ)) % MOD

val = 0

for i in range(2, k+1):
    val = (val*2 + pow(2, i-2, MOD) * (i-1)) % MOD

print((res + val)%MOD)