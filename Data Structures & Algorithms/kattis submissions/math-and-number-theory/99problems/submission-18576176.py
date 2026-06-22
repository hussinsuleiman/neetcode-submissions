n = int(input())
r = n%100
q = n // 100

if r >= 49 or q == 0:
    print(100*(q+1) - 1)
else:
    print(100*q-1)