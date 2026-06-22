N = int(input())

for _ in range(N):
    nbs = input().split()
    vals = []
    d = dict()
    
    for x in nbs:
        v = int(x[0])*10 + int(x[-1])
        
        if v in d:
            d[v] += 1
        else:
            d[v] = 1
            vals.append(v)
    
    vals.sort()
    res = []
    
    for v in vals:
        res.append(str(d[v]))
    
    print(' '.join(res))