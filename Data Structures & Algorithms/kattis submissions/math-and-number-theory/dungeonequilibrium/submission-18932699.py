from collections import defaultdict

n = int(input())
nbs = list(map(int, input().split()))
occ = defaultdict(int)
total = 0

for elt in nbs:
    occ[elt] += 1

for elt in occ.keys():
    if occ[elt] > elt:
        total += occ[elt]-elt
    elif occ[elt] < elt:
        total += occ[elt]

print(total)