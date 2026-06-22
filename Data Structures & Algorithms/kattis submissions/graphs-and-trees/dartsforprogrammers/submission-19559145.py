N = int(input())
a = [20, 1, 18, 4, 13, 6, 10, 15, 2, 17, 3, 19, 7, 16, 8, 11, 14, 9, 12, 5]
d = {a[i]:i+1 for i in range(20)}
pre = [0, 20]

for i in range(1, 20):
    pre.append(pre[-1] + a[i])

for _ in range(N):
    w1,w2,w3 = map(int, input().split())
    arr = [d[w1], d[w2], d[w3]]
    arr.sort()
    
    if w1 == w2 and w2 == w3:
        print(w1)
        continue
    
    s1, s2 = pre[arr[1]] - pre[arr[0]-1], pre[arr[2]] - pre[arr[1]-1]
    s = max(s1,s2)
    s = max(s, 210 - s1 - s2 + w1+w2+w3)
    print(s)