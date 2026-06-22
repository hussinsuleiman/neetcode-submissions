n = int(input())
p = list(map(int, input().split()))
done = False

for i in range(1, n):
    if p[i] <= p[0]:
        print(i)
        done = True
        break

if not done:
    print("infinity")