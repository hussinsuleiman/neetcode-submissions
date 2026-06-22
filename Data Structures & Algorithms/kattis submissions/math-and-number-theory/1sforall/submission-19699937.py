import math

n = int(input())
res = [0, 1]

for i in range(2, n+1):
    res.append(res[-1] + 1)
    
    for a in range(2, (i+1)//2):
        res[-1] = min(res[-1], res[a] + res[i-a])
    
    nb = str(i)
    
    for ind in range(1, len(nb)):
        if nb[ind] != '0':
            res[-1] = min(res[-1], res[int(nb[:ind])] + res[int(nb[ind:])])
    
    for k in range(2, int(math.sqrt(i)) + 1):
        if i%k == 0:
            res[-1] = min(res[-1], res[k] + res[i//k])
    
print(res[n])