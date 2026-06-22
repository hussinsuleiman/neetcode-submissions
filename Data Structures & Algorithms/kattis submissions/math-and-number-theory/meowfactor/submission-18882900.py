n = int(input())
res = 1

for i in range(2, 129):
    if n%(i**9) == 0:
        res = i

print(res)