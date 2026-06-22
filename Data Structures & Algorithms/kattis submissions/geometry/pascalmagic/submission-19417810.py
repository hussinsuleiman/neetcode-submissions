n,p = map(int, input().split())
prod = 1
res = n+1

while n != 0:
    prod *= (n%p + 1)
    n //= p

print(res-prod)