N = int(input())
t = 0
r = 0

for i in range(N):
    a,k = input().split()
    k = int(k)
    
    if a == 'T':
        t += k
    else:
        r = max(t,r)
        t -= k

print(max(r,t))