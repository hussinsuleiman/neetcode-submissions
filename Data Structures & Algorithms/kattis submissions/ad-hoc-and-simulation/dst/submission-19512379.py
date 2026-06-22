N = int(input())

for i in range(N):
    c,D,H,M = input().split()
    D,H,M = int(D), int(H), int(M)
    
    if c == 'F':
        M += D
        
        while M >= 60:
            M -= 60
            H += 1
        
        if H >= 24:
            H -= 24
    
    else:
        M -= D
        
        while M < 0:
            M += 60
            H -= 1
        
        if H < 0:
            H += 24
    
    print(str(H) + ' ' + str(M))