r,d = map(int, input().split())

if r == 1:
    print(2*d-2)
elif d == 1:
    print(2*r-2)
elif r%2 == 0 or d%2 == 0:
    print(r*d)
else:
    print(r*d+1)