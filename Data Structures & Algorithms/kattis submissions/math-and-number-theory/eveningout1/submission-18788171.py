A, B = map(int, input().split())
r = A % B

if r <= B / 2:
    print(r)
else:
    print(B-r)