N = int(input())
stack = []
area = 0

for i in range(N):
    H,W = map(int, input().split())
    width = W
    
    while stack and stack[-1][0] >= H:
        h,w = stack.pop()
        area = max(area, h*w)
        width += w
    
    stack.append((H,width))

width = 0

while stack:
    h,w = stack.pop()
    width += w
    area = max(area, h*width)

print(area*50)