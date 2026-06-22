T = int(input())

for i in range(T):
    N = int(input())
    k = 2
    valid = False
    
    while k*(k+1)//2 <= N:
        if (k%2 == 0 and N%k == k//2) or (k%2 == 1 and N%k == 0):
            nbs = [str(N//k-(k-1)//2+i) for i in range(k)]
            res = ' + '.join(nbs)
            print(str(N) + ' = ' + res)
            valid = True
            break
        
        k += 1
    
    if not valid:
        print("IMPOSSIBLE")