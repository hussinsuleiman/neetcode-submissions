N = int(input())
res = 0

while N != 1:
    if N%2 == 0:
        N //= 2
    else:
        N = N*3+1
    res += 1

print(res)