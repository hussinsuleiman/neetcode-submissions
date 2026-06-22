import math

N, M = map(int, input().split())
total = 0

for i in range(1, int(math.sqrt(M)) + 1):
    if M // i <= N and M % i == 0:
        total += 1
        
        if math.sqrt(M) != i:
            total += 1

print(total)



