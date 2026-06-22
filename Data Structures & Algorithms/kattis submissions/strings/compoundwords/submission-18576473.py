import sys
input = sys.stdin.readline

words = []
l = 0

for line in sys.stdin:
    w = line.strip().split()
    
    for word in w:
        words.append(word)
        l += 1
        
seen = set()

for i in range(l):
    for j in range(i+1, l):
        seen.add(words[i] + words[j])
        seen.add(words[j] + words[i])
        
out = list(seen)
out.sort()
print("\n".join(out))
