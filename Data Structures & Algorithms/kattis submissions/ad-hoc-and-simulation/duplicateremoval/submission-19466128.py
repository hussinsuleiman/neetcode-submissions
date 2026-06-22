import sys

for line in sys.stdin:
    nbs = list(map(int, line.split()))
    
    if nbs[0] == 0:
        break
    
    res = []

    for i in range(1, len(nbs)):
        if res and str(nbs[i]) == res[-1]:
            continue
        
        res.append(str(nbs[i]))
    
    res.append('$')
    print(' '.join(res))