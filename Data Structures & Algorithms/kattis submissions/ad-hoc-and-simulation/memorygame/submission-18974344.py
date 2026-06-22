N,K = map(int, input().split())
nbs = set()
elts = list(map(int, input().split()))
t = 0

for nb in elts:
    if nb in nbs:
        t += 1
        nbs.remove(nb)
    else:
        nbs.add(nb)

if 2*N-K == 1 or (2*N-K == 2 and not nbs):
    t += 1

print(t)