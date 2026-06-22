N = int(input())
d = list(map(int,input().split()))
s = sum(d)
ans = set()

for i in range(N):
    ans.add(s-d[i])

res = list(ans)
res.sort()

for i in range(len(res)):
    res[i] = str(res[i])

print(len(res))
print(" ".join(res))