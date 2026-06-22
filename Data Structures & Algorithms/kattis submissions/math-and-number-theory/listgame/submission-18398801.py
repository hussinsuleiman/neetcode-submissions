import math

X = int(input())
total = 0

for nb in range(2, math.floor(math.sqrt(X))+1):
    while X%nb == 0:
        X = X // nb
        total += 1

if X != 1:
    total += 1

print(total)