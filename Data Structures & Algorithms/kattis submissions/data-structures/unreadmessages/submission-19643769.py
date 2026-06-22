n,m = map(int, input().split())
res = 0
messages = []

for k in range(m):
    s = int(input())
    res += n-1
    done = False
    
    for i in range(k-1, -1, -1):
        if messages[i] == s:
            res -= (k-i-1)
            done = True
            break
    
    if not done:
        res -= k
    
    messages.append(s)
    print(res)