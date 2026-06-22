A,B = input().split()
A,B = int(A[::-1]), int(B[::-1])

if A > B:
    print(A)
else:
    print(B)