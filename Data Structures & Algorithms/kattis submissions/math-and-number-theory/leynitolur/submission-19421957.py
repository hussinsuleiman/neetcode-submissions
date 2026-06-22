MOD = 1 << 64
A = 230309227
B = 68431307
Ainv = pow(A, -1, MOD)

for _ in range(100):
    y = int(input())
    x = ((y - B) * Ainv) % MOD
    print(x)