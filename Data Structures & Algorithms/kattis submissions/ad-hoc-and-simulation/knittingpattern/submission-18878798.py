N, P = map(int, input().split())
a = ((N - P) // 2) % P

if P%2 == 0 and a == P // 2:
    print(0)
else:
    print(2*a)