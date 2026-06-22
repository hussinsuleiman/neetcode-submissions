import sys

MOD = 998244353
G = 3

def ntt(a, invert):
    n = len(a)

    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        wlen = pow(G, (MOD - 1) // length, MOD)
        
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)

        for i in range(0, n, length):
            w = 1
            half = length >> 1
            
            for j in range(i, i + half):
                u = a[j]
                v = a[j + half] * w % MOD
                a[j] = (u + v) % MOD
                a[j + half] = (u - v) % MOD
                w = w * wlen % MOD

        length <<= 1

    if invert:
        n_inv = pow(n, MOD - 2, MOD)
        
        for i in range(n):
            a[i] = a[i] * n_inv % MOD

def convolution(a, b):
    n = 1
    need = len(a) + len(b) - 1
    
    while n < need:
        n <<= 1

    fa = a[:] + [0] * (n - len(a))
    fb = b[:] + [0] * (n - len(b))

    ntt(fa, False)
    ntt(fb, False)

    for i in range(n):
        fa[i] = fa[i] * fb[i] % MOD

    ntt(fa, True)
    return fa[:need]

def solve():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    b = [1 if c == 'B' else 0 for c in s]
    a = [1 if c == 'A' else 0 for c in s][::-1]
    
    conv = convolution(b, a)
    out = []
    
    for k in range(1, n):
        out.append(str(conv[n - 1 - k]))
        
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()