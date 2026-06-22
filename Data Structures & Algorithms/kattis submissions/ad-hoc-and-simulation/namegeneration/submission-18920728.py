N = int(input())
names = []
vowels = {0, 4, 8, 14, 20} 

for i in range(26):
    if i in vowels:
        continue
    
    for j in range(26):
        if j in vowels:
            continue
        
        for k in range(26):
            if k in vowels:
                continue
                
            for l in range(26):
                name = [chr(i+ord('a')), chr(j+ord('a')), 'a', chr(k+ord('a')), chr(l+ord('a'))]
                names.append(name)
                
for i in range(N):
    print(''.join(names[i]))