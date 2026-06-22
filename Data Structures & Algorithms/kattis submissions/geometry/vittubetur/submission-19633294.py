import sys

nbs = []
m = 0

for line in sys.stdin:
    n = int(line)
    nbs.append(n)
    m = max(m, n)

spf = list(range(m + 1))

for i in range(2, int(m ** 0.5) + 1):
    if spf[i] == i:  
        for j in range(i * i, m + 1, i):
            if spf[j] == j:
                spf[j] = i

omega = [0] * (m + 1)

for n in range(2, m + 1):
    omega[n] = omega[n // spf[n]] + 1

vals = [0]

for n in range(1, m + 1):
    vals.append(vals[-1] + omega[n])

for n in nbs:
    print(vals[n])