import heapq

n,m = map(int, input().split())
songs = []

for i in range(n):
    f,s = input().split()
    f = int(f)
    songs.append((f,s))

topHits = [(1,0)]
INF = float('inf')

for i in range(1, n):
    quality = songs[i][0]*(i+1) / songs[0][0] if songs[0][0] > 0 else INF if songs[i][0] > 0 else 0
    
    if len(topHits) < m:
        heapq.heappush(topHits, (quality, -i))
    
    elif quality > topHits[0][0] and len(topHits) == m:
        heapq.heappop(topHits)
        heapq.heappush(topHits, (quality, -i))

res = []

while topHits:
    res.append(songs[-topHits[0][1]][1])
    heapq.heappop(topHits)

print('\n'.join(res[::-1]))