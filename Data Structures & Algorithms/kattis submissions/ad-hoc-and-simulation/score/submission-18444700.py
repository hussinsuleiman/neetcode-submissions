import sys
input = sys.stdin.readline

n = int(input())
scores = [0, 0]
leadTimeHome = 0
tieTime = 0
previousTime = 0

for i in range(n):
    T, p, time = map(str, input().split())
    m, s = map(int, time.split(":"))
    time = 60*m + s
    
    if scores[0] > scores[1]:
        leadTimeHome += time-previousTime
    elif scores[0] == scores[1]:
        tieTime += time-previousTime 
    
    if T == 'H':
        scores[0] += int(p)
    else:
        scores[1] += int(p)
    
    previousTime = time
    
if scores[0] > scores[1]:
    leadTimeHome += 32*60 - previousTime

winner = 'A'
if scores[0] > scores[1]:
    winner = 'H'

leadTimeAway = 32*60 - leadTimeHome - tieTime

leadHomeMin = str(leadTimeHome // 60)
leadHomeSec = str(leadTimeHome % 60)

if len(leadHomeSec) == 1:
    leadHomeSec = '0' + leadHomeSec

leadAwayMin = str(leadTimeAway // 60)
leadAwaySec = str(leadTimeAway % 60)

if len(leadAwaySec) == 1:
    leadAwaySec = '0' + leadAwaySec

print(winner + ' ' + str(leadHomeMin) + ':' + str(leadHomeSec) + ' ' + str(leadAwayMin) + ':' + str(leadAwaySec))


    