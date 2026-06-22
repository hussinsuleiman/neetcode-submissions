from collections import defaultdict

N = int(input())
loc = defaultdict(list)
items = defaultdict(set)

for _ in range(N):
    item = input().split()
    
    if item[0] == 'PUT':
        items[item[1]].add(item[2])
        loc[item[2]].append(item[1])
    
    elif item[0] == "TAKE":
        elt = loc[item[1]][0]
        loc[item[1]].pop()
        items[elt].remove(item[1])
    
    else:
        ans = list(items[item[1]])
        
        if not ans:
            print("NOT FOUND")
        else:
            ans.sort()
            print(' '.join(ans))      