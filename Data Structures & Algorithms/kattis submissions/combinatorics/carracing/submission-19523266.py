n = int(input())
p = [0]*5
cnt = [0]*5

for i in range(n):
    car, pos = map(int, input().split())
    cnt[car-1] += 1
    p[car-1] += pos

index = 0

for i in range(1,5):
    if p[i]//cnt[i] < p[index]//cnt[index]:
        index = i

print(index+1)
print(p[index]//cnt[index])