rec = []
done = False

for i in range(3):
    a,b = map(int, input().split())
    rec.append((a,b))

if rec[0][0] == rec[1][0] and rec[1][0] == rec[2][0]:
    if rec[0][1] + rec[1][1] + rec[2][1] == rec[0][0]:
        print("YES")
        done = True

if not done and rec[1][0] == rec[2][0]:
    if rec[1][0] + rec[0][1] == rec[0][0] and rec[1][1] + rec[2][1] == rec[0][0]:
        print("YES")
        done = True
        
if not done and rec[1][1] == rec[2][1]:
    if rec[1][0] + rec[2][0] == rec[0][0] and rec[0][1] + rec[1][1] == rec[0][0]:
        print("YES")
        done = True

if not done and rec[1][0] == rec[2][1]:
    if rec[1][1] + rec[2][0] == rec[0][0] and rec[0][1] + rec[1][0] == rec[0][0]:
        print("YES")
        done = True

if not done and rec[1][1] == rec[2][0]:
    if rec[1][0] + rec[2][1] == rec[0][0] and rec[0][1] + rec[1][1] == rec[0][0]:
        print("YES")
        done = True

if not done:
    print("NO")