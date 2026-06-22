import math

P = int(input())

def sumExponents(P):
    total = 0
    i = 2
    
    while P > 1 and i < int(math.sqrt(P))+1:
        while P % i == 0:
            total += 1
            P = P // i
                
        i += 1
    
    if P != 1:
        total += 1
    
    return total

print(sumExponents(P)+1)