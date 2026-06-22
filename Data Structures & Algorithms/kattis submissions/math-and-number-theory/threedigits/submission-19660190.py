n = int(input())
res = [1]
MOD = 10**12

for i in range(1, n+1):
    nb = res[-1]*i
    
    while nb%10 == 0:
        nb //= 10
    
    res.append(nb%MOD)

s = str(res[n]%1000)

if len(s) < 3 and n >= 7:
    s = '0'*(3-len(s)) + s
    
print(s)