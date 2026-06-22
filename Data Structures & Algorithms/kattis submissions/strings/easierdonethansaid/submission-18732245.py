import sys
input = sys.stdin.readline

password = input().strip()
vowels = {'a', 'e', 'i', 'o', 'u'}

while password != 'end':
    nbConsV = 0
    nbConsC = 0
    hasVowel = False
    isValid = True
    prev = ''
    
    for letter in password:
        if letter in vowels:
            nbConsV += 1
            hasVowel = True
            nbConsC = 0
        else:
            nbConsC += 1
            nbConsV = 0
        
        if letter == prev and letter != 'o' and letter != 'e':
            isValid = False
            
        if nbConsV == 3 or nbConsC == 3:
            isValid = False
            
        prev = letter
    
    if isValid and hasVowel:
        print("<" + password + "> is acceptable.")
    else:
        print("<" + password + "> is not acceptable.")
    
    password = input().strip()  
    
    
    