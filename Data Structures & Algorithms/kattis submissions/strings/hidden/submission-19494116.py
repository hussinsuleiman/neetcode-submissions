from collections import defaultdict

P,S = input().split()
occ = defaultdict(int)

for c in P:
    occ[c] += 1

i = 0
nbLeft = len(P)

for c in S:
    if c in occ and occ[c] > 0:
        if c != P[i]:
            print("FAIL")
            exit()
        else:
            i += 1
            occ[c] -= 1
            nbLeft -= 1

if nbLeft == 0:
    print("PASS")
else:
    print("FAIL")