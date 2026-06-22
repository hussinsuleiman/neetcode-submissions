import sys
input = sys.stdin.readline

n = int(input())
output = ''
maxVal = -1

for i in range(n):
    name, cont, cool = input().strip().split()
    cont, cool = int(cont), int(cool)
    
    if cont*cool > maxVal or (cont*cool == maxVal and name < output):
        maxVal = cont*cool
        output = name

print(output)
    