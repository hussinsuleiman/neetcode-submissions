from collections import defaultdict

N = int(input())

if N == 0:
    print('0 0')
    exit()

nbs = []

for _ in range(N):
    line = input()
    
    if line == 'just me':
        nbs.append(0)
    else:
        m = int(line.split()[0])
        nbs.append(m)

occ = defaultdict(int)

for i in range(N):
    occ[nbs[i]] += 1
    
    if occ[nbs[i]+1] > 0:
        occ[nbs[i]+1] -= 1

res = 0

for c in occ:
    res += occ[c]
    
print(str(res) + ' ' + str(N))