T = int(input())

for _ in range(T):
    input()
    N = int(input())
    nbs = list(map(int, input().split()))
    cnt = {0: 1}
    cur = 0
    tot = 0
    
    for i in range(N):
        cur += nbs[i]
        
        if cur-47 in cnt:
            tot += cnt[cur-47]
        
        if cur in cnt:
            cnt[cur] += 1
        else:
            cnt[cur] = 1
    
    print(tot)