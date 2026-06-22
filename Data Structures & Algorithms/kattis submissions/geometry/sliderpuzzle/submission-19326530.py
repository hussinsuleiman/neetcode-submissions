from collections import deque

T = int(input())

for i in range(T):
    nbs = list(map(int, input().split()))
    visited = set([0])
    queue = deque([0])
    L = len(nbs)
    
    while queue:
        index = queue.popleft()
        nb = nbs[index]
        
        if index >= nb and index-nb not in visited:
            visited.add(index-nb)
            queue.append(index-nb)
        
        if index + nb < L and index+nb not in visited:
            visited.add(index + nb)
            queue.append(index + nb)
    
    if L-1 in visited:
        print("Puzzle " + str(i+1) + ' is solvable.')
    else:
        print("Puzzle " + str(i+1) + ' is not solvable.')