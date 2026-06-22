N = int(input())
M = int(input())
res = 0
nbs = set([N])

while 0 not in nbs:
    new = set()
    
    for nb in nbs:
        if nb%M != 0:
            new.add(nb - nb%M)
        else:
            new.add(nb//M)
        new.add(nb - M + 1)
    
    res += 1
    nbs = new

print(res)