N = int(input())
words = input().split()
vowels = {'a', 'e', 'i', 'o', 'u'}
new = []

for i in range(N):
    word = []
    j = 0
    l = len(words[i])
    
    while j < l:
        if words[i][j] in vowels and not (j == 0 or j == l-1):
            j += 1
            continue
        
        word.append(words[i][j])
        
        while j+1 < len(words[i]) and words[i][j] == words[i][j+1]:
            j += 1
        
        j += 1
    
    new.append(''.join(word))

print(' '.join(new))