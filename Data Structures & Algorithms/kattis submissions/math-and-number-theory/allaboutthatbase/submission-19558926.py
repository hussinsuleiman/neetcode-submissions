N = int(input())

for _ in range(N):
    X,op,Y,eq,Z = input().split()
    ans = []
    start = 1
    hasZero = False
    
    for c in X:
        if '0' <= c and c <= '9':
            start = max(start, ord(c)-ord('0')+1)
            if c == '0':
                hasZero = True
        else:
            start = max(start, ord(c)-ord('a')+11)
    
    for c in Y:
        if '0' <= c and c <= '9':
            start = max(start, ord(c)-ord('0')+1)
            if c == '0':
                hasZero = True
        else:
            start = max(start, ord(c)-ord('a')+11)
    
    for c in Z:
        if '0' <= c and c <= '9':
            start = max(start, ord(c)-ord('0')+1)
            if c == '0':
                hasZero = True
        else:
            start = max(start, ord(c)-ord('a')+11)
    
    if start == 2 and not hasZero:
        start = 1
    
    for B in range(start, 37):
        base = str(B)
        
        if B >= 10 and B < 36:
            base = chr(ord('a')+B-10)
        elif B == 36:
            base = '0'
        
        x,y,z = 0,0,0    
        
        for exp in range(len(X)):
            c = X[-exp-1]
            
            if '0' <= c and c <= '9':
                x += int(c) * B**exp
            else:
                x += (ord(c)-ord('a')+10) * B**exp
                
        for exp in range(len(Y)):
            c = Y[-exp-1]
            
            if '0' <= c and c <= '9':
                y += int(c) * B**exp
            else:
                y += (ord(c)-ord('a')+10) * B**exp
        
        for exp in range(len(Z)):
            c = Z[-exp-1]
            
            if '0' <= c and c <= '9':
                z += int(c) * B**exp
            else:
                z += (ord(c)-ord('a')+10) * B**exp
        
        if op == '+':
            if x+y == z:
                ans.append(base)
        
        elif op == '*':
            if x*y == z:
                ans.append(base)
        
        elif op == '-':
            if x-y == z:
                ans.append(base)
        
        else:
            if x/y == z:
                ans.append(base)
         
    if not ans:
        print("invalid")
    else:
        print(''.join(ans))