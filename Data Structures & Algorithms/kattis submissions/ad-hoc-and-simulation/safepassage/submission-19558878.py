nbs = list(map(int, input().split()))
N = nbs[0]
times = sorted(nbs[1:])
ans = 0
i = N - 1

while i >= 3:
    ans += min(times[0] + 2 * times[1] + times[i], 2 * times[0] + times[i - 1] + times[i])
    i -= 2

if i == 2:
    ans += sum(times[:3])
else:
    ans += times[i]

print(ans)