N = int(input())
total = 0

for i in range(N):
    nb = input()
    base, exp = int(nb[:-1]), int(nb[-1])
    total += base ** exp

print(total)