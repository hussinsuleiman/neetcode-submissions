n = int(input())
s = [int(input()) for i in range(n)]
s.sort()
s = s[::-1]
res = [1]
T = 0
past = s[0]
ans = 1

for i in range(1, n):
    if T + s[i] < past:
        res.append(0)
        T += s[i]
    else:
        res.append(1)
        past += T+s[i]
        T = 0
        ans = i+1
        
print(ans)