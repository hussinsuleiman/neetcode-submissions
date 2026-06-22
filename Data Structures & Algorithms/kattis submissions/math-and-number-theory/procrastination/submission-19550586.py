N,M = map(int, input().split())
tasks = []

for _ in range(N):
    T,G = map(int, input().split())
    tasks.append((T,-G))

tasks.sort()
grade = 0

for i in range(N):
    if M < tasks[i][0]:
        print(grade)
        exit()
    
    M -= tasks[i][0]
    grade -= tasks[i][1]

print(grade)