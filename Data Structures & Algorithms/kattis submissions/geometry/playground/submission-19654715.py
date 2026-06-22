K = int(input())

while K != 0:
    a = list(map(float, input().split()))
    nbs = [int(a[i]*1000) for i in range(K)]
    nbs.sort()
    sums = nbs[0]
    done = False
    
    for i in range(1, K):
        if sums >= nbs[i]:
            print('YES')
            done = True
            break
        sums += nbs[i]
    
    if not done:
        print('NO')
    
    K = int(input())