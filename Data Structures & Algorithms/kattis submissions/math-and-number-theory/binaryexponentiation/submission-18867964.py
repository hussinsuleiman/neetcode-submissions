a, e, m = map(int, input().split())

def binExp(a, e, m):
    if e == 0:
        return 1
    
    return ((a ** (e % 2)) * binExp(a, e // 2, m) ** 2) % m

print(binExp(a, e, m))

