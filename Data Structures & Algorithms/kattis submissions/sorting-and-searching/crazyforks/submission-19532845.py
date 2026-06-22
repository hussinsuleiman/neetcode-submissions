import sys
lines = []
L = []
indMax = 0
i = 0

for line in sys.stdin:
    line = line[:-1]
    lines.append(line)
    l = len(line)
    L.append(l)
    
    if l > L[indMax]:
        indMax = i
        
    i += 1

print(indMax)
tines = [0] * L[indMax]

for k in range(indMax+1, i):
    for j in range(L[k]):
        if lines[k][j] == '#':
            tines[j] += 1

res = []

for t in tines:
    if t > 0:
        res.append(str(t))

print(' '.join(res))