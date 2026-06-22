d,s,e = map(int, input().split())
x = d-s-e

if x >= s:
    print((1-s/d)*s/x)
else:
    print((s+e)/d)