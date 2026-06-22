A,B = map(int, input().split())

while A%2 == 0 and B%2 == 0:
    A //= 2
    B //= 2

if A%2 == 1 and B%2 == 1:
    print("B")
else:
    print("A")