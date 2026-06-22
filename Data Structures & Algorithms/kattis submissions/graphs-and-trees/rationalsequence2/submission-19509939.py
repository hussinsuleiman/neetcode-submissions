P = int(input())

for i in range(P):
    K,frac = input().split()
    a,b = map(int, frac.split('/'))
    cur = 1
    ops = []
    
    while (a,b) != (1,1):
        if a > b:
            ops.append(2)
            a -= b
        else:
            ops.append(1)
            b -= a
        
    for i in range(len(ops)-1, -1, -1):
        if ops[i] == 1:
            cur *= 2
        else:
            cur = cur * 2 + 1
    
    print(K + ' ' + str(cur))