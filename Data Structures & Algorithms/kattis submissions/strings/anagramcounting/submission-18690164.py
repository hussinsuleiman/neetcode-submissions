import sys
input = sys.stdin.readline

def factorial(n):
    f = 1
    
    for i in range(1, n+1):
        f *= i
    
    return f

for line in sys.stdin:
    line = line.strip()
    occ = dict()
    l = len(line)
    
    for letter in line:
        if letter in occ.keys():
            occ[letter] += 1
        else:
            occ[letter] = 1
    
    fact = factorial(l)
    
    for elt in occ.keys():
        fact //= factorial(occ[elt])
    
    print(fact)
    
    