import sys
input = sys.stdin.readline

n = int(input())
curr = 0
maxCapacity = 0

for i in range(n):
    a,b = map(int, input().split())
    curr += b-a
    maxCapacity = max(maxCapacity, curr)
    
print(maxCapacity)
    
    