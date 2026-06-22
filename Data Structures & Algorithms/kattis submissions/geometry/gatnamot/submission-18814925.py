import math

r = int(input())
total = 2*r+1

for k in range(1, r+1):
    total += (2 * int(math.sqrt(r ** 2 - k ** 2)) + 1) * 2

print(total)