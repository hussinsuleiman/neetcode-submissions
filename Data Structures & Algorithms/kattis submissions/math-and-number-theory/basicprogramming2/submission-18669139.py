import sys
input = sys.stdin.readline

N,t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    A.sort()
    i, j = 0, N-1
    done = False
    
    while i < j and A[i] < A[j]:
        s = A[i] + A[j]
        
        if s < 7777:
            i += 1
        elif s > 7777:
            j -= 1
        else:
            print("Yes")
            done = True
            break
    
    if not done:
        print("No")
    
elif t == 2:
    s = set(A)
    
    if len(s) != N:
        print("Contains duplicate")
    else:
        print("Unique")
    
elif t == 3:
    occ = dict()
    
    for nb in A:
        if nb not in occ:
            occ[nb] = 1
        else:
            occ[nb] += 1
    
    found = False
    
    for elt in occ.keys():
        if occ[elt] > N/2:
            print(elt)
            found = True
    
    if not found:
        print(-1)
            
elif t == 4:
    A.sort()
    
    if N%2 == 0:
        output = [str(A[(N-1) // 2]), str(A[N // 2])]
        print(" ".join(output))
    else:
        print(A[N // 2])

elif t == 5:
    output = []
    
    for i in range(N):
        if A[i] >= 100 and A[i] <= 999:
            output.append(str(A[i]))
    
    output.sort()
    print(" ".join(output))