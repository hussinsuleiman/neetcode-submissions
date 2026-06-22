a,b,k = map(int, input().split())

if a < b:
    a,b = b,a

def gcd(a,b,k):
    while a**2 > k:
        a,b = b,a%b
    return a,b

a,b = gcd(a,b,k)
print(a,b)