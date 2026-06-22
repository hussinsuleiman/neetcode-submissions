n,k = map(int, input().split())
a = list(map(int, input().split()))
s = a.copy()
s.sort()

for i in range(n):
    if (s[i]-a[i])%k != 0:
        print('NO')
        exit()
    
    for j in range(n):
        if a[j] == s[i]:
            a[i], a[j] = a[j], a[i]
            break

print('YES')