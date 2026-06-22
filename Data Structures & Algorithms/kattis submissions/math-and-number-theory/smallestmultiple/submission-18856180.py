import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    
    while b != 0:
        temp = a%b
        a = b
        b = temp
    
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def smallestMult(nbs):
    if len(nbs) == 1:
        return nbs[0]
    
    a = nbs.pop()
    return lcm(smallestMult(nbs), a)

for line in sys.stdin:
    nbs = list(map(int, line.strip().split()))
    print(smallestMult(nbs))
