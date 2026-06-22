N = int(input())
tot = 0

for _ in range(N):
    typ, d, nb = input().split()
    nb = int(nb)
    
    if d == "IN":
        tot += nb
    else:
        tot -= nb

if tot == 0:
    print("NO STRAGGLERS")
else:
    print(tot)