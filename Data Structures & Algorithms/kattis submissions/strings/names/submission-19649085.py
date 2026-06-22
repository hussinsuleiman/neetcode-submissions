s = input()
n = len(s)
res = n

for i in range(n):
    j,k = i,n-1
    tot = 0
    
    while j < k:
        if s[j] != s[k]:
            tot += 1
        
        j += 1
        k -= 1
    
    res = min(res, tot + i)

print(res)