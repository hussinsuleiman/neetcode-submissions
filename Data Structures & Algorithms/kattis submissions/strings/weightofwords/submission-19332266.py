l,w = map(int, input().split())
q,r = w//l, w%l
res = []

if w > 26*l or w < l:
    print("impossible")
    exit()

for i in range(r):
    res.append(chr(ord('a') + q))

for i in range(r, l):
    res.append(chr(ord('a') + q-1))

print(''.join(res))