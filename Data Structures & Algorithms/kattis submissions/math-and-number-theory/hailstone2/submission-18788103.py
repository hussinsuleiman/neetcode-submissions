import sys
input = sys.stdin.readline

n = int(input())
total = 1

while n != 1:
    if n % 2 == 0:
        n = n//2
    else:
        n = n*3+1
    
    total += 1

print(total)