N = int(input())
nbs = []

for i in range(N):
    nbs.append(int(input(), 2))

nbs.sort()
i = 0

while i < N and i == nbs[i]:
    i += 1

x = bin(i)[2:]
r = '0' * (N-len(x))
print(r + x)