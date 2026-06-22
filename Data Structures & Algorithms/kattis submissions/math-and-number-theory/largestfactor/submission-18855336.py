n = int(input())
prime = 0

for i in range(2, int(n ** 0.5) + 1):
    while n % i == 0:
        n //= i
        prime = i

print(max(n, prime))
    
    