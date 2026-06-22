import sys
import math
import random
sys.setrecursionlimit(10**7)

def is_prime(n):
    if n < 2:
        return False
    small = [2,3,5,7,11,13,17,19,23,29]
    for p in small:
        if n % p == 0:
            return n == p

    d = n-1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    test_bases = [2,325,9375,28178,450775,9780504,1795265022]
    for a in test_bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            continue
        for _ in range(s-1):
            x = (x*x) % n
            if x == n-1:
                break
        else:
            return False
    return True

def pollard(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n

    while True:
        x = random.randrange(2, n-1)
        y = x
        c = random.randrange(1, n-1)

        def f(v):
            return (v*v + c) % n

        d = 1
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x-y), n)

        if d != n:
            return d

def largest_factor(n):
    if n == 1:
        return 1
    if is_prime(n):
        return n

    d = pollard(n)
    return max(largest_factor(d), largest_factor(n//d))


m = int(sys.stdin.readline()) - 1
print(largest_factor(m))