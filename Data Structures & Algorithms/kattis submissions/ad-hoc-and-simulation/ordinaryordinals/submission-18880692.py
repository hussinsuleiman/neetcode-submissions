N, M = map(int, input().split())

def exp(b):
    if b == 0:
        return 1
    return (2**(b%2) * exp(b//2)**2) % M

if N == 0:
    print(2%M)
else:
    print((5 * exp(N-1) - 1)%M)