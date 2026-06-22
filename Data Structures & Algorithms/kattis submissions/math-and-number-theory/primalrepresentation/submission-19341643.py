import sys

for line in sys.stdin:
    x = int(line)
    res = []
    
    if x < 0:
        res.append("-1")
        x = -x
    
    i = 2
    
    while i*i <= x:
        exp = 0
        
        while x%i == 0:
            x //= i
            exp += 1
        
        if exp > 1:
            res.append(str(i) + '^' + str(exp))
        
        elif exp == 1:
            res.append(str(i))
        
        i += 1
    
    if x > 1:
        res.append(str(x))
    
    print(' '.join(res))