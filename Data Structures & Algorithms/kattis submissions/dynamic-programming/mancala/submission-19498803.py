P = int(input())
B = [0] * 80
cur = 0
memo = {}

while cur < 2001:
    s = 0
    l = 0
    
    for i in range(80):
        if B[i] != 0:
            s += B[i]
        else:
            s += 1
            B[i] = i+1
            
            for j in range(i-1, -1, -1):
                B[j] -= 1
            
            l = i
            break
    
    cur += 1
    l += 1
    
    while s < cur:
        s += B[l]
        l += 1
    
    memo[cur] = (l, tuple(B[:l]))
    
for i in range(P):
    K,N = map(int, input().split())
    l,B = memo[N]
    ans = [str(B[i]) for i in range(l)]
    t = 0
    print(str(K) + ' ' + str(l))
    
    while t + 10 <= l:
        print(' '.join(ans[t:t+10]))
        t += 10
    
    print(' '.join(ans[t:]))