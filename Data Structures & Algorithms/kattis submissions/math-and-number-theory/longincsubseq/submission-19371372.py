import sys
from bisect import bisect_left

for line in sys.stdin:
    n = int(line)
    nbs = list(map(int, sys.stdin.readline().split()))
    tails = []
    indices = []
    prev = ['-1']*n
    
    for i in range(n):
        pos = bisect_left(tails, nbs[i])
        
        if pos > 0:
            prev[i] = indices[pos-1] 
        
        if pos == len(tails):
            tails.append(nbs[i])
            indices.append(str(i))
        else:
            tails[pos] = nbs[i]
            indices[pos] = str(i)
    
    print(len(tails))
    res = []
    cur = indices[-1]
    
    while cur != '-1':
        res.append(cur)
        cur = prev[int(cur)]
    
    res.reverse()
    print(' '.join(res)) 