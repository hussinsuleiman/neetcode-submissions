import sys
input = sys.stdin.readline

N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    print(7)

elif t == 2:
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
    
elif t == 3:
    nbs = [A[0], A[1], A[2]]
    nbs.sort()
    print(nbs[1])
    
elif t == 4:
    print(sum(A))
    
elif t == 5:
    s = 0
    
    for elt in A:
        if elt%2 == 0:
            s += elt
    
    print(s)
    
elif t == 6:
    output = []
    
    for elt in A:
        output.append(chr(elt%26 + ord('a')))
    
    print("".join(output))
    
else:
    i = 0
    visited = set([0])
    done = False
    
    while 0 <= A[i] and A[i] < N:
        if i == N-1:
            print("Done")
            done = True
            break
        
        if A[i] in visited:
            print("Cyclic")
            done = True
            break
        
        visited.add(A[i])
        i = A[i]
    
    if not done:
        print("Out")