import sys
input = sys.stdin.readline

n = int(input())
scores = []

for i in range(n):
    command, s, c, g = input().strip().split()
    s = int(s)
    c = int(c)
    g = int(g)
    
    if command == 'CAUGHT':
        scores.append((s, c, g))
    else:
        scores.append((s, -c, -g))

scores.sort()
k = int(input())
index = 0
output = [0, 0]

while index < n and scores[index][0] < k:
    output[0] += scores[index][1]
    output[1] += scores[index][2]
    index += 1

print(str(output[0]) + " " + str(output[1]))