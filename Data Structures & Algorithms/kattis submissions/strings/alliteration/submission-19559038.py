from collections import defaultdict

n = int(input())

for _ in range(n):
    words = input().split()
    cnt = defaultdict(int)
    
    for w in words:
        cnt[w[0]] += 1
    
    c = ''
    
    for key in cnt:
        if c == '' or cnt[key] > cnt[c] or (cnt[key] == cnt[c] and key < c):
            c = key
    
    print(c)