import sys
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for line in sys.stdin:
    s = line.strip().split()
    words = []
    
    for word in s:
        if word[0] in vowels:
            words.append(word + 'yay')
            continue
        
        i = 0
        
        while word[i] not in vowels:
            i += 1
        
        words.append(word[i:] + word[:i] + 'ay')
    
    print(' '.join(words))