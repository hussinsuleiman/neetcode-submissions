s = input().upper()
freq = [0]*26
nbLetters = 0

for c in s:
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        freq[ord(c)-ord('A')] += 1
        nbLetters += 1

nbWays = [1,2]
curSum = 3

while curSum < nbLetters:
    nbWays.append(nbWays[-1] + nbWays[-2])
    curSum += nbWays[-1]
        
freq.sort()
total = 0
nbKeys = 0
index = 0

for i in range(25, -1, -1):
    f = freq[i]
    
    if f == 0:
        break
    
    nbKeys += 1
    total += f * (index*2+1)
    
    if nbKeys == nbWays[index]:
        index += 1
        nbKeys = 0
    
print(total + 3*nbLetters - 3)