n = int(input())
nbs = [int(input()) for i in range(n)]
res = 1
inc = -1

for i in range(1, n):
    if nbs[i] == nbs[i-1]:
        continue
    
    if nbs[i] > nbs[i-1] and inc != 1:
        inc = 1
        res += 1
    
    elif nbs[i] < nbs[i-1] and inc != 0:
        inc = 0
        res += 1

print(res)