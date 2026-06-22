import sys, random, math

b, d = map(int, sys.stdin.readline().split())


if d == 2:
    print("yes" if (b & 1) else "no")
    sys.exit()

x = b % d
if x == 0:
    print("no")
    sys.exit()


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small = (2,3,5,7,11,13,17,19,23,29,31,37)
    for p in small:
        if n % p == 0:
            return n == p
    s = 0
    d0 = n - 1
    while d0 % 2 == 0:
        s += 1
        d0 //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        v = pow(a, d0, n)
        if v == 1 or v == n - 1:
            continue
        for _ in range(s - 1):
            v = (v * v) % n
            if v == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    while True:
        c = random.randrange(1, n)
        f = lambda t: (t * t + c) % n
        x = random.randrange(0, n)
        y = x
        g = 1
        while g == 1:
            x = f(x)
            y = f(f(y))
            g = math.gcd(abs(x - y), n)
        if g != n:
            return g

def factorize(n: int, out: list):
    if n == 1:
        return
    if is_prime(n):
        out.append(n)
        return
    g = pollard_rho(n)
    factorize(g, out)
    factorize(n // g, out)


fac = []
factorize(d - 1, fac)
r = d - 1

for p in set(fac):
    while r % p == 0 and pow(x, r // p, d) == 1:
        r //= p

print("yes" if (r % 2 == 0 and pow(x, r // 2, d) == d - 1) else "no")