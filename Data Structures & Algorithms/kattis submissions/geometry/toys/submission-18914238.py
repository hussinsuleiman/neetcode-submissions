T, K = map(int, input().split())
pos = 0

for i in range(2, T + 1):
    pos = (pos + K) % i

print(pos)