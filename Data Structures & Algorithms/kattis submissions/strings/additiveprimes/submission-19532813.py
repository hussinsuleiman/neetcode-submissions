n = int(input())

def isPrime(k):
    for i in range(2, int(k**0.5)+1):
        if k%i == 0:
            return False
    return True

if not isPrime(n):
    print("COMPOSITE")
    exit()

sDigits = 0

while n != 0:
    sDigits += n%10
    n //= 10

if isPrime(sDigits):
    print("ADDITIVE PRIME")
else:
    print("PRIME, BUT NOT ADDITIVE")