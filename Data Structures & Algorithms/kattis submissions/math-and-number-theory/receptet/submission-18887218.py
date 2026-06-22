N = int(input())
total = 0

for i in range(N):
    H,B,K = map(int, input().split())
    total += max(0,B-H)*K

print(total)
    