import sys
input = sys.stdin.readline

def gcd(a, b):
    while b > 0:
        a %= b
        a, b = b, a
    
    return a

def compare(s0, s1, r0, r1):
    if (s0, s1) == (1, 2) or (s0, s1) == (2, 1):
        if (r0, r1) == (1, 2) or (r0, r1) == (2, 1):
            return 0
        return 1
    
    elif (r0, r1) == (1, 2) or (r0, r1) == (2, 1):
        return 2
    
    elif s0 == s1:
        if r0 == r1:
            if r0 > s0:
                return 2 
            elif r0 < s0:
                return 1
            else:
                return 0
        
        else:
            return 1
    
    elif r0 == r1:
        return 2 
    
    if s0 < s1:
        s0, s1 = s1, s0
    
    if r0 < r1:
        r0, r1 = r1, r0
    
    if s0 > r0:
        return 1
    
    elif s0 < r0:
        return 2
    
    elif s1 > r1:
        return 1
    
    elif s1 < r1:
        return 2
    
    else:
        return 0


s0, s1, r0, r1 = input().strip().split()

while (s0, s1, r0, r1) != ('0', '0', '0', '0'):
    total = 1
    
    if s0 != '*':
        s0 = int(s0)
    else:
        total *= 6
        
    if s1 != '*':
        s1 = int(s1)
    else:
        total *= 6
    
    if r0 != '*':
        r0 = int(r0)
    else:
        total *= 6
    
    if r1 != '*':
        r1 = int(r1)
    else:
        total *= 6
    
    nbWin = 0
    
    if total == 1296:
        for i in range(1, 7):
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(i, j, k, l) == 1:
                            nbWin += 1
    
    elif total == 216:
        if s0 != '*':
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(s0, j, k, l) == 1:
                            nbWin += 1
        
        elif s1 != '*':
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(j, s1, k, l) == 1:
                            nbWin += 1
        
        elif r0 != '*':
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(j, k, r0, l) == 1:
                            nbWin += 1
        
        elif r1 != '*':
            for j in range(1, 7):
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(j, k, l, r1) == 1:
                            nbWin += 1
    elif total == 36:
        if s0 != '*':
            if s1 != '*':
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(s0, s1, k, l) == 1:
                            nbWin += 1
            
            elif r0 != '*':
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(s0, k, r0, l) == 1:
                            nbWin += 1
                
            else:
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(s0, k, l, r1) == 1:
                            nbWin += 1
        
        elif s1 != '*':
            if r0 != '*':
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(k, s1, r0, l) == 1:
                            nbWin += 1
            
            else:
                for k in range(1, 7):
                    for l in range(1, 7):
                        if compare(k, s1, l, r1) == 1:
                            nbWin += 1
        
        else:
            for k in range(1, 7):
                for l in range(1, 7):
                    if compare(k, l, r0, r1) == 1:
                        nbWin += 1
    
    elif total == 6:
        if s0 == '*':
            for l in range(1, 7):
                if compare(l, s1, r0, r1) == 1:
                    nbWin += 1
        
        elif s1 == '*':
            for l in range(1, 7):
                if compare(s0, l, r0, r1) == 1:
                    nbWin += 1
        
        elif r0 == '*':
            for l in range(1, 7):
                if compare(s0, s1, l, r1) == 1:
                    nbWin += 1
        
        else:
            for l in range(1, 7):
                if compare(s0, s1, r0, l) == 1:
                    nbWin += 1
        
    else:
        if compare(s0, s1, r0, r1) == 1:
            nbWin += 1
    
    if nbWin == 0:
        print(0)
        
    elif nbWin == total:
        print(1)
    
    else:
        g = gcd(nbWin, total)
        print(str(nbWin // g) + "/" + str(total // g))
                    
    s0, s1, r0, r1 = input().strip().split()
