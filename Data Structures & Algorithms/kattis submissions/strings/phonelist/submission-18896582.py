t = int(input())

for i in range(t):
    n = int(input())
    nbs = []
    
    for j in range(n):
        nbs.append(input())
    
    nbs.sort()
    done = False
    
    for j in range(1, n):
        if nbs[j-1] == nbs[j][:len(nbs[j-1])]:
            print("NO")
            done = True
            break
    
    if not done:
        print("YES")