def is_prime(n):
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return n == p

    d = n - 1
    s = 0
    
    while d % 2 == 0:
        d //= 2
        s += 1

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Deterministic bases for 64-bit integers
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            return True
        if not check(a):
            return False

    return True


N = int(input())
print("YES" if is_prime(N) else "NO")
