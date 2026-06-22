from collections import deque

n = int(input())
nbs = list(map(int, input().split()))
queue = deque(nbs)
done = False

while queue and not done:
    done = True
    elt = queue.popleft()
    newQueue = deque()
    
    if not queue:
        newQueue.append(elt)
        
    else:
        while queue: 
            elt2 = queue.popleft()
            
            if (elt + elt2) % 2 == 0:
                done = False
                
                if not queue:
                    break
                
                elt = queue.popleft()
                
                if not queue:
                    newQueue.append(elt)
                    break
            
            else:
                newQueue.append(elt)
                elt = elt2
                
                if not queue:
                    newQueue.append(elt)
                    break
    
    queue = newQueue

print(len(queue))

