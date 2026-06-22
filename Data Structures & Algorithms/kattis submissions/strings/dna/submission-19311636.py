N = int(input())
s = input()
res = 0
i = N-1
cur = s[-1]

while i >= 0:
    c = s[i]
    
    if cur == 'A':
        while i >= 0 and s[i] == c:
            i -= 1
        
        cur = 'B'
    
    else:
        res += 1
        j = i
        
        while i >= 0 and s[i] == c:
            i -= 1
    
        if j-i == 1:
            cur = 'A'
    
print(res)    