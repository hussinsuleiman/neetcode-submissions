n = int(input())
single = [i for i in range(21)] 
nbs = set(single)

for nb in single:
    nbs.add(2*nb)
    nbs.add(3*nb)

nbs = list(nbs)
l = len(nbs)

for i in range(l):
    for j in range(i, l):
        for k in range(j, l):
            if n == nbs[i] + nbs[j] + nbs[k]:
                for t in [i, j, k]:
                    if nbs[t] == 0:
                        continue
                    
                    if nbs[t]%3 == 0:
                        print("triple " + str(nbs[t]//3))
                    
                    elif nbs[t]%2 == 0:
                        print("double " + str(nbs[t]//2))
                    
                    else:
                        print("single " + str(nbs[t]))
                
                exit()

print("impossible")