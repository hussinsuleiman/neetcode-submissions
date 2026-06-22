T = int(input())

for i in range(T):
    d = int(input())
    print((8 * pow(9, d-1, 10**9+7)) % (10**9+7))