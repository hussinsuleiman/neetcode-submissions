import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n,s = sys.stdin.readline().split()
    n = int(n)
    elts = len(s)
    front = True
    lo, hi = 0, len(s)-1
    
    while n > 0:
        n -= 1
        q = elts//4
        elts -= q
        
        if q == 0:
            break
        
        if front:
            lo += q
        else:
            hi -= q
        
        front = not front
    
    print(s[lo:hi+1])