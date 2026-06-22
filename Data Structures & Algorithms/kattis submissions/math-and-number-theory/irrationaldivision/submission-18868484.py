p,q = map(int, input().split())

if p%2 == 0:
    print(0)
elif q%2 == 1:
    print(1)
elif q > p:
    print(2)
else:
    print(0)