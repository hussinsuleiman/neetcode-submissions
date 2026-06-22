import sys

for line in sys.stdin:
    n = int(line)
    cur = 1
    i = 0
    
    while cur < n:
        if i == 0:
            cur *= 9
        else:
            cur *= 2
        
        i = (i+1)%2
    
    if i == 1:
        print("Stan wins.")
    else:
        print("Ollie wins.")