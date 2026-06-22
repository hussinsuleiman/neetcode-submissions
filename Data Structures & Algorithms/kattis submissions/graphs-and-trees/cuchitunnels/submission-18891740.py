N = int(input())
D = list(map(int, input().split()))
cur = 0
done = False

for i in range(N-1, 0, -1):
    if D[i] > cur+1:
        done = True
        break
    
    cur += 2-D[i] 

print("YES" if not done and cur == D[0] else "NO")