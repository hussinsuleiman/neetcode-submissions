nbs = list(map(int, input().split()))
n = nbs[0]
a = nbs[1:]

pref_max = [0] * n
suff_min = [0] * n
pref_max[0] = a[0]

for i in range(1, n):
    pref_max[i] = max(pref_max[i-1], a[i])

suff_min[-1] = a[-1]

for i in range(n-2, -1, -1):
    suff_min[i] = min(suff_min[i+1], a[i])

res = []

for i in range(n):
    if (i == 0 or pref_max[i-1] < a[i]) and \
       (i == n-1 or a[i] < suff_min[i+1]):
        res.append(str(a[i]))

print(len(res), " ".join(res[:100]))