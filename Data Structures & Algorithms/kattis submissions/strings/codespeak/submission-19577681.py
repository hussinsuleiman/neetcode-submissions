n = int(input())
s = input().split()
vowels = {'a', 'e', 'i', 'o', 'u'}
ans = []

for w in s:
    res = []
    curVowel = False
    
    for c in w:
        if c in vowels and not curVowel:
            res.append('ib')
            curVowel = True
        
        res.append(c)
        
        if c not in vowels:
            curVowel = False
    
    ans.append(''.join(res))

print(' '.join(ans))