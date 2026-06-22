t = int(input())

for _ in range(t):
    n = int(input())
    res = ['1']
    exp = 1
    
    while n%(2*exp) != exp:
        exp *= 2
        res.append(str(exp))
    
    print(len(res))
    print(' '.join(res))