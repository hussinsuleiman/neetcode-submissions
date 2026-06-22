import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
unread = [("Jane Eyre", k)]
offered = []
indexOffered = 0
time = 0

for i in range(n):
    line = input().strip()
    s = ""
    j = 1
    
    while line[j] != '"':
        s += line[j]
        j += 1
    
    line = line.split()
    k = int(line[-1])
    
    if s < "Jane Eyre":
        heapq.heappush(unread, (s, k))
        
for i in range(m):
    line = input().strip()
    s = ""
    j = 1
    
    while line[j] != '"':
        j += 1
    
    j += 1
    
    while line[j] != '"':
        s += line[j]
        j += 1
    
    line = line.split()  
    t = int(line[0])
    k = int(line[-1])
    offered.append((t,s,k))

offered.sort()

while indexOffered < m and offered[indexOffered][0] <= time:
    if offered[indexOffered][1] < "Jane Eyre":
        heapq.heappush(unread, (offered[indexOffered][1], offered[indexOffered][2]))
        
    indexOffered += 1

s, k = heapq.heappop(unread)
    
while s != "Jane Eyre":
    time += k
    
    while indexOffered < m and offered[indexOffered][0] <= time:
        if offered[indexOffered][1] < "Jane Eyre":
            heapq.heappush(unread, (offered[indexOffered][1], offered[indexOffered][2]))
            
        indexOffered += 1
    
    s, k = heapq.heappop(unread)

print(time + k)
    