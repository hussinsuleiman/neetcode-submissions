n = int(input())
d = [int(input()) for i in range(n)]
stack = [d[0]]
res = 0

for i in range(1, n):
    while stack and stack[-1] < d[i]:
        stack.pop()
        res += 1
    
    if stack:
        res += 1
    
    stack.append(d[i])

print(res)