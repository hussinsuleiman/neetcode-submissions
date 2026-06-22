from collections import defaultdict

N = int(input())
strs = [input() for i in range(N)]
pos = {c:i for i,c in enumerate(strs[0])}

def inv(s):
    arr = [pos[c] for c in s]
    inv = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if arr[i] > arr[j]:
                inv += 1
    
    return inv%2

left, right = [], []

for s in strs:
    if inv(s) == 0:
        left.append(s)
    else:
        right.append(s)

def check_one_swap(s,t):
    diff = []
    
    for i in range(len(s)):
        if s[i] != t[i]:
            diff.append(i)
            
            if len(diff) > 2:
                break
    
    if len(diff) != 2:
        return False
    
    i,j = diff[0], diff[1]
    return s[i] == t[j] and s[j] == t[i]

graph = defaultdict(list)

for l in left:
    for r in right:
        if check_one_swap(l,r):
            graph[l].append(r)

match = {}

def dfs(u, seen):
    for v in graph[u]:
        if v in seen:
            continue
        
        seen.add(v)
        
        if v not in match or dfs(match[v], seen):
            match[v] = u
            return True
    
    return False
    
matching = 0

for l in left:
    if dfs(l, set()):
        matching += 1
    
print(N-matching)