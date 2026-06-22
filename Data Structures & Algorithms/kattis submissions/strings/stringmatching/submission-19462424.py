import sys

def lps(pattern):
    l = len(pattern)
    lps = [0] * l
    j = 0
    
    for i in range(1, l):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    
    return lps

def kmp(pattern, text):
    arr = lps(pattern)
    res = []
    j = 0
    
    for i in range(len(text)):
        while j > 0 and pattern[j] != text[i]:
            j = arr[j-1]
        
        if text[i] == pattern[j]:
            j += 1
            
            if j == len(pattern):
                res.append(str(i-j+1))
                j = arr[j-1]
    
    return ' '.join(res)

for line in sys.stdin:
    pattern = line.strip()
    text = sys.stdin.readline().strip()
    print(kmp(pattern, text))