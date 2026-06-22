n,r,k = map(int,input().split())
m = max(k,r)

if m >= n:
    print(2*m)
elif n-k <= k-r:
    print(2*k)
else:
    print(n+r+(n+r)%2)