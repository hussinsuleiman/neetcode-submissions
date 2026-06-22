import sys
input = sys.stdin.readline

n = int(input())
s = []
s.append(int(input()))
t = 0

for i in range(1, n):
    s.append(int(input()))
    t += max(s[i-1], s[i])

print(t)
    

