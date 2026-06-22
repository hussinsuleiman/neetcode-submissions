n = int(input())
a = list(map(int, input().split()))
stack = []

for nb in a:
    if not stack or nb < stack[-1]:
        stack.append(nb)
        
    else:
        while stack and stack[-1] < nb:
            stack.pop()

        while stack and nb == stack[-1]:
            nb = stack.pop()*2
        stack.append(nb)

print(max(stack))