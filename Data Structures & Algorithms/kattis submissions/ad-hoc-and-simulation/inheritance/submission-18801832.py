P = int(input())
l = len(str(P))
nbs = [[0]]

for i in range(l):
    new = []
    
    for nb in nbs[-1]:
        new.append(nb*10+2)
        new.append(nb*10+4)
    
    nbs.append(new)

output = []

for i in range(1, l+1):
    for nb in nbs[i]:
        if P % nb == 0:
            output.append(str(nb))

print("\n".join(output))
