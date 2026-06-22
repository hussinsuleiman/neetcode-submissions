import sys
import math
input = sys.stdin.readline

n = int(input())

for i in range(n):
    x = int(input())
    right, left = [], []
    
    while x != 0:
        exp = int(math.log(abs(x)) / math.log(3))
        s = (3 ** (exp+1) - 1) // 2
        
        if abs(x) > s:
            exp += 1
            
        # put right
        if x > 0:
            right.append(str(3 ** exp))
            x -= 3 ** exp
        
        # put left
        else:
            left.append(str(3 ** exp))
            x += 3 ** exp
    
    print("left pan: " + " ".join(left))
    print("right pan: " + " ".join(right))
    print()
    