N,K = map(int, input().split())
nbs = list(map(int, input().split()))
ans = []

for k in nbs:
    if k <= (N+1)//2:
        ans.append('1')
    else:
        ans.append(str(N))

print(' '.join(ans))