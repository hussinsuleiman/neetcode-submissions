c = int(input())

for i in range(c):
    d,n = map(int, input().split())
    nbs = list(map(int, input().split()))
    
    pre = [0]
    count = [0] * (d+1)
    count[0] = 1
    res = 0
    
    for nb in nbs:
        pre.append((nb + pre[-1])%d)
        res += count[pre[-1]]
        count[pre[-1]] += 1
    
    print(res)