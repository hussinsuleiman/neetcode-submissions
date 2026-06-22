from collections import defaultdict

N = int(input())
cnt = defaultdict(int)
names = []
once = set()

for i in range(N):
    s = input()
    parts = s.split()
    cnt[parts[0]] += 1
    names.append(s)

for name in names:
    parts = name.split()
    
    if cnt[parts[0]] == 1:
        once.add(name)

cnt = defaultdict(int)

for i in range(N):
    parts = names[i].split()
    
    if names[i] in once:
        print(names[i])
    else:
        cnt[parts[0]] += 1
        print(parts[0] + ' ' + str(cnt[parts[0]]) + '.' + ' ' + ' '.join(parts[1:]))